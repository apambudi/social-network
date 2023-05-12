
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("newpost", views.newpost, name="newpost"),
    path("post", views.post, name="post"),
    path("post/<int:user_id>", views.user_post, name="user_post"),
    path("follow/count/<int:user_id>", views.follow_count, name="follow"),
    path("follow/check/<int:user_id>", views.follow_check, name="follow-check"), 
    path("follow/<int:user_id>", views.follow, name="follow-check"), 
    path("unfollow/<int:user_id>/", views.unfollow, name="unfollow"), 

    # Profile page route
    path("profile/<int:user_id>", views.profile_view, name="profile"),
]
