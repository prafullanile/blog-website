from django.shortcuts import render, get_object_or_404, redirect
from .models import blog, category
from django.db.models import Q


def posts_by_category(request, category_id):
    # get single category safely
    category_obj = get_object_or_404(category, pk=category_id)

    # fetch posts for that category
    featured_posts = blog.objects.filter(
        category=category_obj,
        status='Published',
        is_featured=True
    )

    context = {
        'featured_posts': featured_posts,
        'category': category_obj,   # ✅ singular
    }

    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(blog, slug=slug, status='Published')

    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blog.html',context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) |  Q(blog_boy__icontains=keyword),status='Published')

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)
