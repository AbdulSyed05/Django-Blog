import poplib
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Blog, Category, Comment, FeaturedCar
from django.db.models import Q
from django.shortcuts import render
from .forms import CommentForm 


def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)

    # Use get_object_or_404 when you want to show a 404
    # error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')

    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        if comment.comment is not "":
            comment.save()
        else:
            print('form is invalid-----')
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blogs', slug=comment.blog.slug)
    else:
        form = CommentForm(instance=comment)
    return redirect('blogs', slug=comment.blog.slug)


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blog_slug = comment.blog.slug
    if request.method == 'POST':
        comment.delete()
        return redirect('blogs', slug=blog_slug)
    return redirect('blogs', slug=blog_slug)

def home(request):
    featured_cars = FeaturedCar.objects.filter(is_featured=True, status='Published')
    posts = Blog.objects.all()

    # Debug prints
    print("Featured Cars:", featured_cars)

    return render
    (request, 'home.html', {'featured_cars': featured_cars, 'posts': posts})


def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) |
        Q(short_description__icontains=keyword) |
        Q(blog_body__icontains=keyword), status='Published'
    )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)
