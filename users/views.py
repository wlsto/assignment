from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView


# Create your views here.
class UsersView(APIView):
    # GET /api/v1/users/
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(
            users,
            many=True,
        )
        return Response(serializer.data)


class UserDetailView(APIView):
    # GET /api/v1/users/<int:pk>
    def get(self, request, pk):
        return Response(
            UserSerializer(get_object(self, pk)).data,
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
