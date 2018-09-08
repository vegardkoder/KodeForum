from django.shortcuts import render, redirect
from .forms import PostForm
from django.views.generic import TemplateView
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime

class createPost(TemplateView):
    template_name = 'forum/createPost.html'
    
    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if(form.is_valid()):

            posting = Post(person=request.user, tittel=form.cleaned_data['tittel'], innhold=form.cleaned_data['innhold'], date=datetime.now())
            posting.save()
            
            return redirect('/forum')

def add_comment(request, pk):
    lol = get_object_or_404(Post, pk=pk)
    if(request.method == 'POST'):
        form = CommentForm(request.POST)
        if(form.is_valid()):
            
            comment = Comment(post=lol, com_innhold=form.cleaned_data['kommentar'], user = request.user)
            comment.save()
            
            return redirect('/forum/' + pk)
    else:
        form = CommentForm()
    template = 'forum/addComment.html'
    context = {'form': form}
    return render(request, template, context)
        

    
            
            
        



        

