from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'is_draft', )
        labels = {
            "title": "Заголовок",
            "text": "Текст",
            "is_draft": "Чернетка",
        }