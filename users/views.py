from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer

from rest_framework.views import APIView


# Create your views here.
class UsersView(APIView):

    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
        return user

    def get(self, request, pk):
        tweets = Tweet.objects.filter(user=pk)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_tweets_by_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
