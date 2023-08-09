from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm, ThreadForm
from .models import Thread, Post


def all_threads(request):
    threads = Thread.objects.all()
    return render(request, 'forum/all_threads.html', {'threads': threads})

# def new_thread(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         if title:
#             thread = Thread(title=title)
#             thread.save()
#             return redirect('thread_detail', thread_id=thread.id)

#     return render(request, 'forum/new_thread.html')

def new_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            thread = Thread(title=title)
            thread.save()
            messages.success(request, 'Your thread has been successfully added!')
            return redirect('forum:thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()

    context = {
        'form': form,
    }
    return render(request, 'forum/new_thread.html', context)

def thread_detail(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts})

def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            messages.success(request, 'Your post has been successfully added!')
            return redirect('forum:thread_detail', thread_id=thread.id)
    else:
        form = PostForm()

    context = {
        'thread': thread,
        'form': form,
    }
    return render(request, 'forum/new_post.html', context)