from django.urls import path
from . import views

urlpatterns = [
    path("v1/tweets/", views.TweetView.as_view()),
    path("v1/tweets/<int:pk>", views.TweetDetailView.as_view()),
    path("v2/tweets/", views.get_all_tweets),
]
