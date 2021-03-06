from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView
# events
from .forms import EventForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #filter
    query = request.GET.get("q")
    if query:
        posts = posts.filter(category__icontains=query)
    query = request.GET.get("qu")
    if query:
        posts = posts.filter(platform__icontains=query)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# events

def event_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-eventdate')
    return render(request, 'blog/event_list.html', {'posts': posts})

def event_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/event_detail.html', {'post': post})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('event_detail', pk=post.pk)
    else:
        form = EventForm()
    return render(request, 'blog/event_edit.html', {'form': form})

def event_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('event_detail', pk=post.pk)
    else:
        form = EventForm(instance=post)
    return render(request, 'blog/event_edit.html', {'form': form})