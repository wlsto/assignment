from django.urls import path
from . import views

urlpatterns = [
    path("v1/tweets/", views.get_all_tweets),
    path("v2/tweets/", views.TweetView.as_view()),
]
