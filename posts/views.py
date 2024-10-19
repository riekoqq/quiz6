from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.forms import PostForm, ReportForm
from posts.models import Post


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save it yet
            post.User = request.user  # Assign the logged-in user to the post
            post.save()  # Now save the post
            messages.success(request, 'Post created successfully!')
            return redirect('home')  # Redirect to home or wherever you want
    else:
        form = PostForm()

    return render(request, 'create.html', {'form': form})

@login_required
def report_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.post = post
            report.save()
            messages.success(request, 'Report submitted successfully!')
            return redirect('home')
    else:
        form = ReportForm()

    return render(request, 'report_post.html', {'form': form, 'post': post})

from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all().order_by('-Created_at')  # Get all posts, ordered by creation date
    paginator = Paginator(posts, 3)  # Show 3 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})
