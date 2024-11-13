from django.urls import path
from . import views

urlpatterns = [
    path("v1/users", views.UsersView.as_view()),
    path("v1/users/password", views.UserChangePassword.as_view()),
    path("v1/users/login", views.UserLogInView.as_view()),
    path("v1/users/logout", views.UserLogOutView.as_view()),
    path("v1/users/<int:pk>", views.UserDetailView.as_view()),
    path("v1/users/<int:pk>/tweets", views.UsersTweetsView.as_view()),
    path("v2/users/<int:pk>/tweets", views.get_tweets_by_user),
]
