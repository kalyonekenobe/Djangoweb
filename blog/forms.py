from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'is_draft', )
        labels = {
            "title": "Заголовок",
            "text": "Текст",
            "is_draft": "Чернетка",
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', )
        labels = {
            'author': "Автор",
            'text': "Текст",
        }