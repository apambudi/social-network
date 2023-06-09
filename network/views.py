import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import User, Post, Follow

def index(request):
    return render(request, "network/index.html")

def profile_view(request, user_id):
    return render(request, "network/profile.html", {
        "user_id": user_id,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    

@csrf_exempt
@login_required    
def newpost(request):

    # Composing a new post must be via POST
    if request.method == "POST":
    
        # Get the post data
        data = json.loads(request.body)

        # Get the post content
        content = data.get("content", "")

        # Save the content to the database
        newpost = Post(user=request.user, content=content)
        newpost.save()

        return JsonResponse({"message": "Posted successfully."}, status=201)
    
    # if request.method == "GET":
    #     posts = Post.objects.filter(user=request.user)

    #     # Return posts in reverse chronologial order
    #     # posts = posts.order_by("-timestamp").all()
    #     return JsonResponse([post.serialize() for post in posts], safe=False)
    
    else:
        return JsonResponse({"error": "POST or GET request required."}, status=400)

@login_required    
def post(request):
    posts = Post.objects.all()

    # Return posts in reverse chronologial order
    posts = posts.order_by("-timestamp").all()
    return JsonResponse([post.serialize() for post in posts], safe=False)

@login_required    
def user_post(request, user_id):
    posts = Post.objects.filter(user=user_id)

    # Return posts in reverse chronologial order
    posts = posts.order_by("-timestamp").all()
    return JsonResponse([post.serialize() for post in posts], safe=False)

@login_required
def follow_count(request, user_id):
    
    number_of_followers = Follow.objects.filter(followed=user_id).count()
    number_of_following = Follow.objects.filter(follower=user_id).count()

    #Return posts in reverse chronological order
    return JsonResponse({'followers_number': number_of_followers, 'following_number': number_of_following}, safe=False)

@login_required
def follow_check(request, user_id):
    user_login_id = request.user.id
    if Follow.objects.filter(follower = user_login_id, followed=user_id).exists():
        return JsonResponse({'test': True}, safe=False)
    else:
        return JsonResponse({'test': False}, safe=False)
    
@login_required
def follow(request, user_id):
    user_login_id = request.user.id
    follower = User.objects.get(pk=user_login_id)
    followed = User.objects.get(pk=user_id)

    # Create a new follow
    new_f = Follow(follower=follower, followed=followed)
    new_f.save()

    return JsonResponse({"message": f"{follower.username} follows {followed.username} successfully"}, status = 201)
    
@login_required
def unfollow(request, user_id):
    user_login_id = request.user.id
    Follow.objects.filter(follower = user_login_id, followed = user_id).delete()
    return JsonResponse({"message": "unfollow successfully"}, status = 201)

@login_required
def following(request):
    return render(request, "network/following.html")

@login_required
def follow_post(request):
    user_login_id = request.user.id
    follows = Follow.objects.filter(follower=user_login_id)
    posts = []
    for follow in follows:
        followed_id = follow.followed.id
        post = Post.objects.filter(user=followed_id)
        posts += post

    # Return posts in reverse chronologial order
    # posts = posts.order_by("-timestamp").all()
    return JsonResponse([post.serialize() for post in posts], safe=False)
