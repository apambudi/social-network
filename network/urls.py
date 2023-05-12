
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"), 

    # API Routes
    path("newpost", views.newpost, name="newpost"),
    path("post", views.post, name="post"),
    path("post/<int:user_id>", views.user_post, name="user-post"),
    path("follow/count/<int:user_id>", views.follow_count, name="follow-count"),
    path("follow/check/<int:user_id>", views.follow_check, name="follow-check"), 
    path("follow/<int:user_id>", views.follow, name="follow"), 
    path("unfollow/<int:user_id>/", views.unfollow, name="unfollow"), 
    path("follow-post", views.follow_post, name="follow-post"), 


    # Profile page route
    path("profile/<int:user_id>", views.profile_view, name="profile"),
]
