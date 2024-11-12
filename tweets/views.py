from .models import Tweet
from .serializers import TweetSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT


# Create your views here.
class TweetView(APIView):
    # GET /api/v1/tweets/
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(
            tweets,
            many=True,
        )
        return Response(serializer.data)

    # POST /api/vi/tweets/
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            tweet = serializer.save()
            return Response(
                TweetSerializer(tweet).data,
            )
        else:
            return Response(serializer.errors)


class TweetDetailView(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    # GET /api/v1/tweets/<int:pk>
    def get(self, request, pk):
        return Response(
            TweetSerializer(self.get_object(pk)).data,
        )

    # PUT /api/v1/tweets/<int:pk>
    def put(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(
            tweet,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(
                TweetSerializer(updated_tweet).data,
            )
        else:
            return Response(serializer.errors)

    # DELETE /api/v1/tweets/<int:pk>
    def delete(self, reqeust, pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_all_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
