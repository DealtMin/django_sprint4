from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.create_post, name='create_post'),
    path('profile/<str:user_name>/', views.create_post, name='profile'),    
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts')
]
