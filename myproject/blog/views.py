from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post

class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post
# Create your views here.
