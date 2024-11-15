# from django.test import TestCase
from rest_framework.test import APITestCase
from . import models
from users.models import User


# Create your tests here.
class TestTweets(APITestCase):

    URL = "/api/v1/tweets/"
    PAYLOAD = "Test Tweet"

    def setUp(self):
        testUser = User.objects.create(
            username="test",
        )
        testUser.set_password("gg")
        testUser.save()
        self.user = testUser

        models.Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_get_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "NOT HTTP_200_OK",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            data[0]["user"],
            1,
        )

    def test_create_tweet(self):
        response = self.client.post(
            self.URL,
            data={
                "payload": "Create Tweet Test",
                "user": 1,
            },
        )
        data = response.json()
        # print(data)

        self.assertEqual(
            response.status_code,
            200,
            "NOT HTTP_200_OK",
        )
        self.assertEqual(
            data["payload"],
            "Create Tweet Test",
        )

        response = self.client.post(self.URL)
        self.assertEqual(
            response.status_code,
            400,
            "NOT HTTP_400_BAD_REQUEST",
        )


class TestTweetDetail(APITestCase):
    URL = "/api/v1/tweets/1"
    PAYLOAD = "Test Tweet Detail"
    PAYLOAD_PUT = "Test Tweet Detail for put"

    def setUp(self):
        testUser = User.objects.create(
            username="test",
        )
        testUser.set_password("gg")
        testUser.save()
        self.user = testUser

        models.Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_get_tweetDetail(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "NOT HTTP_200_OK",
        )
        self.assertIsInstance(
            data,
            dict,
        )
        self.assertEqual(
            data["user"],
            1,
        )

    def test_put_tweetDetail(self):
        response = self.client.put(
            self.URL,
            data={
                "payload": self.PAYLOAD_PUT,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "NOT HTTP_200_OK",
        )
        self.assertEqual(
            data["payload"],
            self.PAYLOAD_PUT,
        )

        response = self.client.put(
            self.URL,
            data={
                "user": 2,
            },
        )
        self.assertEqual(
            response.status_code,
            400,
            "NOT HTTP_400_BAD_REQUEST",
        )

    def test_delete_tweetDetail(self):
        response = self.client.delete(self.URL)

        self.assertEqual(
            response.status_code,
            204,
            "NOT HTTP_204_NO_CONTENT",
        )
