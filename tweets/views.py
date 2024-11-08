from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tweet
from .serializers import TweetSerializer

from rest_framework.views import APIView


# Create your views here.
class TweetView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_all_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
