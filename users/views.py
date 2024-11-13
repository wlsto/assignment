from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from . import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class UsersView(APIView):
    # GET /api/v1/users/
    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UserSerializer(
            users,
            many=True,
        )
        return Response(serializer.data)

    # POST /api/v1/users/
    # Create a user account with password
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError

        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(password)
            new_user.save()
            return Response(
                serializers.UserSerializer(new_user).data,
            )
        else:
            return Response(serializer.errors)


class UserDetailView(APIView):
    # GET /api/v1/users/<int:pk>
    def get(self, request, pk):
        return Response(
            serializers.UserSerializer(get_object(self, pk)).data,
        )


class UsersTweetsView(APIView):
    # GET /api/v1/users/<int:pk>/tweets
    def get(self, request, pk):
        user = get_object(self, pk)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(
            tweets,
            many=True,
        )
        return Response(serializer.data)


class UserChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    # PUT /api/v1/users/password: Edit logged in user password
    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


class UserLogInView(APIView):

    # POST /api/v1/users/login: Log a user in
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response({"error": "Wrong password"})


class UserLogOutView(APIView):

    permission_classes = [IsAuthenticated]

    # POST /api/v1/users/logout: Log a user out
    def post(self, request):
        logout(request)
        return Response({"ok": "bye!"})


def get_object(self, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    return user


@api_view(["GET"])
def get_tweets_by_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
