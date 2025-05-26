from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.shortcuts import get_object_or_404, render
from .accessory import get_public_posts, pagination, get_all_posts
from .models import Category, Comments, Post
from .forms import CommentsForm, PostsForm
from django.contrib.auth.decorators import login_required


def index(request):
    template = 'blog/index.html'
    page_obj = pagination(request, get_public_posts())
    context = {'page_obj': page_obj}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    data = {'author': get_user(request).pk, 'post': post_id}
    form = CommentsForm(initial=data)
    post = get_object_or_404(
        get_public_posts(),
        pk=post_id
    )
    context = {'post': post,
               'form': form}
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


def work_with_post(request, post_id=None):
    if post_id is not None:
        instance = get_object_or_404(Post, pk=post_id)
        data = None
    else:
        instance = None
        data = {'author': get_user(request).pk}
    form = PostsForm(
        request.POST or None,
        files=request.FILES or None,
        initial=data,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        form.save()
    template = 'blog/create.html'
    return render(request, template, context)


def view_profile(request, user_name):
    template = 'blog/profile.html'
    profile = get_object_or_404(User, username=user_name)
    if profile.pk == get_user(request).pk:
        page_obj = get_all_posts(profile.pk)
    else:
        page_obj = get_public_posts().filter(author=profile.pk)
    context = {'profile': profile,
               'page_obj': page_obj
               }
    return render(request, template, context)


@login_required
def work_with_comment(request, post_id, comment_id=None):
    if comment_id is not None:
        instance = get_object_or_404(Comments, pk=comment_id)
    else:
        instance = None
    form = CommentsForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    template = 'blog/comment.html'
    return render(request, template, context)
