from django.shortcuts import get_object_or_404, render
from .models import Category, Post
from django.utils import timezone


def index(request):
    template = 'blog/index.html'
    post_list = (
        Post.objects.prefetch_related(
            'category', 'location', 'author'
        )
        .filter(
            category__is_published=True, is_published=True,
            pub_date__lte=timezone.now()
        )[0:5]
    )
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.prefetch_related(
            'category', 'location', 'author'
        ),
        pk=post_id, category__is_published=True,
        is_published=True, pub_date__lte=timezone.now()
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category, slug=category_slug,
        is_published=True
    )
    post_list = (
        Post.objects.prefetch_related(
            'category', 'location', 'author'
        )
        .filter(
            is_published=True, pub_date__lte=timezone.now(),
            category__pk=category.pk
        )
    )
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
