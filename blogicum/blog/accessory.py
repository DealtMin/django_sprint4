from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator


def get_public_posts():

    posts = Post.objects.prefetch_related(
        'category', 'location', 'author'
    ).filter(
        category__is_published=True, is_published=True,
        pub_date__lte=timezone.now()
    )
    return posts


def get_all_posts(author):

    posts = Post.objects.prefetch_related(
        'category', 'location', 'author'
    ).filter(
        category__is_published=True,
        author=author
    )
    return posts


def pagination(request, query, items=10):
    paginator = Paginator(query, items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
