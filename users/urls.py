from django.urls import path
from . import views

urlpatterns = [
    path("v1/users/<int:pk>/tweets", views.get_tweets_by_user),
    path("v2/users/<int:pk>/tweets", views.UsersView.as_view()),
]
