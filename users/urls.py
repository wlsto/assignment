from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/tweets", views.get_tweets_by_user),
]
