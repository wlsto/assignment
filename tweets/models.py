from django.db import models
from common.models import CommonModel


# Create your models here.
class Tweet(CommonModel):

    payload = models.TextField(max_length=180)

    def __str__(self):
        return f"Tweet-{self.payload}"


class Like(CommonModel):

    tweet = models.ManyToManyField(
        "tweets.Tweet",
    )

    def __str__(self):
        return f"Like-{self.user.username}"
