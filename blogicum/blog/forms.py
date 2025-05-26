from .models import Post, Comments
from django import forms


class PostsForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'
