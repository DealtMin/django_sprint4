from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('profile/<str:user_name>/', views.view_profile, name='profile'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
    path('<int:post_id>/add_comment', views.add_comment, name='add_comment')
]
