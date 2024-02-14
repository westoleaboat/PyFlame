from django import forms
from .models import Post

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