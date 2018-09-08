from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    tittel = forms.CharField(max_length=140)
    innhold = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('tittel', 'innhold')

class CommentForm(forms.ModelForm):
    kommentar = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Comment
        fields = ('kommentar',)
