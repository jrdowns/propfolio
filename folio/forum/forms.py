from django import forms
from .models import Post, Thread

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'email', 'subject', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'subject': forms.TextInput(attrs={'required': True}),
            'body': forms.Textarea(attrs={'required': True}),
        }

# class ThreadForm(forms.ModelForm):
#     class Meta:
#         model = Thread
#         fields = ['title']
#         widgets = {
#             'title': forms.TextInput(attrs={'required': True}),
#         }

class ThreadForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, required=True)