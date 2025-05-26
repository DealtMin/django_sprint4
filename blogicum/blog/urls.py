from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/create/', views.work_with_post, name='create_post'),
    path('posts/<int:post_id>/edit/', views.work_with_post, name='edit_post'),
    path('posts/<int:post_id>/delete/',
         views.work_with_post, name='delete_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/comment/',
         views.work_with_comment, name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.work_with_comment, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/',
         views.work_with_comment, name='delete_comment'),
    path('profile/<str:user_name>/', views.view_profile, name='profile'),
    path('profile/<str:user_name>/edit_profile>/',
         views.view_profile, name='profile'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
]
