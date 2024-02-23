from django import forms
from .models import Post, Comment

from markdownx.fields import MarkdownxFormField

class PostForm(forms.ModelForm):
    STATUS_CHOICES = [('draft', 'Draft'), ('published', 'Published')]
    
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = MarkdownxFormField()
    tags = forms.TextInput(attrs={'class': 'form-control'}),
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'status', 'publish']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
