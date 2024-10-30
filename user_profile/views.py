from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Comment
from .forms import SignUpForm,  LoginForm, ProfileForm, PostForm, CommentForm, UpdateCommentForm
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def view_home(request):
    return render(request, 'user_profile/home.html')

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('login')
    else:
        signup_form = SignUpForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'user_profile/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
            else:
                login_form.add_error(None, "Invalid username or password.")
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }

    return render(request, 'user_profile/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def profile_view(request):
    return render(request, 'user_profile/user_profile.html')


def id_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'user_profile/user_profile.html', context)


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')

    form = ProfileForm(instance=profile, initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'name': f"{profile.first_name} {profile.last_name}",  # Combine names for the name field

    })

    context = {
        'form': form,

    }

    return render(request, 'user_profile/edit_profile.html', context)




# def PostView(request):
#     post_inside_view = Post.objects.all().order_by('-id')
#     user_profile = None
#     if request.user.is_authenticated:
#         try:
#             user_profile = Profile.objects.get(user=request.user)
#         except Profile.DoesNotExist:
#             user_profile = None  # Handle the case where the profile doesn't exist
#
#     # Paginate the posts
#     paginator = Paginator(post_inside_view, 6)
#     page_number = request.GET.get('page')
#
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)  # If No show the first page
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)  # If the page is out of range, show the last page
#
#     context = {
#         'posts': posts,
#         'user_profile': user_profile,
#     }
#
#     return render(request, 'user_profile/post.html', context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post, Profile


def PostView(request):
    # Get all posts
    post_inside_view = Post.objects.all().order_by('-id')

    # Handle search
    search_query = request.GET.get('search')  # Get the search query from the GET parameters
    if search_query:
        post_inside_view = post_inside_view.filter(post_name__icontains=search_query)

    user_profile = None
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None  # Handle the case where the profile doesn't exist

    # Paginate the posts
    paginator = Paginator(post_inside_view, 6)
    page_number = request.GET.get('page')

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)  # If No show the first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # If the page is out of range, show the last page

    context = {
        'posts': posts,
        'user_profile': user_profile,
        'search_query': search_query,  # Pass the search query to the context
    }

    return render(request, 'user_profile/post.html', context)


def YourPostView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    post_inside_view = Post.objects.all().order_by('-id')
    user_profile = Profile.objects.get(user=request.user)

    context = {
        'post_inside_view': post_inside_view,
        "user_profile": user_profile,
    }

    return render(request, 'user_profile/your_post.html', context)


@login_required
def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_owner = request.user
            post.save()
            return redirect('post')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'user_profile/create_post.html', context)


def ArticleDetailView(request, pk):
    article_detail = get_object_or_404(Post, pk=pk)
    user_profile = article_detail.post_owner.profile
    comments = article_detail.post_comments.all()  # get all comments
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = article_detail
            new_comment.user = request.user
            new_comment.save()
            return redirect('article_detail', pk=article_detail.pk)
    else:
        comment_form = CommentForm()

    context = {
        'article_detail': article_detail,
        'user_profile': user_profile,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'user_profile/article_detail.html', context)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.user in post.post_like.all():
        post.post_like.remove(request.user)  # Unlike the post
        liked = False
    else:
        post.post_like.add(request.user)  # Like the post
        liked = True

    # Return the number of likes and the like status as JSON
    return JsonResponse({
        'total_likes': post.post_like.count(),
        'liked': liked
    })


def delete_your_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.post_owner:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this post.')
    return redirect('post')


@login_required
def update_your_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post')
    else:
        form = PostForm(instance=post)

    return render(request, 'user_profile/update_post.html', {'form': form})


@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = UpdateCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=comment.post.id)  # Adjust the redirect URL accordingly
    else:
        form = UpdateCommentForm(instance=comment)

    return render(request, 'user_profile/comment/update_comment.html', {'form': form, 'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return HttpResponseRedirect(reverse('article_detail', kwargs={'pk': post_id}))
    context = {
        'comment': comment,
    }
    return render(request, 'user_profile/comment/delete_comment.html', context)


def home_view(request):
    top_posts = Post.objects.annotate(like_count=Count('post_like')).order_by('-like_count')[:6]

    context = {
        'top_posts': top_posts,
    }
    return render(request, 'user_profile/home.html', context)