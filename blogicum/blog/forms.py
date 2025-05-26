from .models import Post, Comments
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class PostsForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%d %H:%M',
                attrs={'type': 'datetime-local'}
            )
        }


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        # fields = '__all__'
        fields = ('text',)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
