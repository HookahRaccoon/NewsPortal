from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class NewsForm(forms.ModelForm):
    heading = forms.CharField(max_length=128)

    class Meta:
        model = Post
        fields = [
            'author',
            'categoryType',
            'PostCategory',
            'heading',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        text = cleaned_data.get("text")

        if text[0:128] == heading:
            raise ValidationError(
                "Заголовок не должен быть идентичен тексту."
            )
        return cleaned_data


