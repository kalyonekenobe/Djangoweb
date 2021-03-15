from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), is_draft=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_draft_list(request, user_id):
    author = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(created_date__lte=timezone.now(), author=author, is_draft=True).order_by("-created_date")
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.is_draft = False
    post.published_date = timezone.now()
    post.save()
    return redirect('post_draft_list', request.user.pk)


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    is_draft = post.is_draft
    post.delete()
    if is_draft:
        return redirect('post_draft_list', request.user.pk)
    else:
        return redirect('post_list')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not form.cleaned_data['is_draft']:
                post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edit_post.html', {'form': form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not form.cleaned_data['is_draft']:
                post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})
