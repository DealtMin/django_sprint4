from django.contrib import admin
from .models import Category, Location, Post, Comments

admin.site.register({Category, Location, Post, Comments})
