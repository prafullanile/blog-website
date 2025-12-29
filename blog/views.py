from django.shortcuts import render, get_object_or_404, redirect
from .models import blog, category,Comment
from django.db.models import Q
from django.http import HttpResponseRedirect



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
    if request.method == 'POST':
        comment=Comment()
        comment.user=request.user
        comment.blogg=single_blog
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    #comments
    comments =Comment.objects.filter(blogg=single_blog)
    comment_count = comments.count()

    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
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
