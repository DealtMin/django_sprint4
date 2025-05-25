from django.shortcuts import get_object_or_404, render
from .models import Category
from .accessory import get_public_posts, pagination
from django.contrib.auth.models import User


def index(request):
    template = 'blog/index.html'
    page_obj = pagination(request, get_public_posts())
    context = {'page_obj': page_obj}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_public_posts(),
        pk=post_id
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
        get_public_posts()
        .filter(
            category__pk=category.pk
        )
    )
    page_obj = pagination(request, post_list)
    context = {'category': category,
               'page_obj': page_obj
               }
    return render(request, template, context)


def create_post(request):
    template = 'blog/create.html'
    return render(request, template)


def view_profile(request, user_name):
    template = 'blog/profile.html'
    profile = get_object_or_404(User, username=user_name)
    page_obj = get_public_posts().filter(author=profile.pk)
    context = {'profile': profile,
               'page_obj': page_obj
               }
    return render(request, template, context)


def add_comment(request, post_id):
    pass
