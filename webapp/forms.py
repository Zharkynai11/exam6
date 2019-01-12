from webapp.models import *
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['phone', 'image']
