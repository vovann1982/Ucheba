from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    tekst = forms.CharField(min_length=40)

    class Meta:
        model = Post
        fields = ['author', 'zagolovok', 'tekst', 'category']

    def clean(self):
        cleaned_data = super().clean()
        tekst = cleaned_data.get("tekst")
        zagolovok = cleaned_data.get("zagolovok")

        if zagolovok == tekst:
            raise ValidationError(
                "Текст не должен быть идентичен заголовку."
            )

        return cleaned_data





