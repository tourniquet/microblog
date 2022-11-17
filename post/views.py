from django.shortcuts import render

from .models import Post

def index(request):
  posts = Post.objects.order_by('-date')
  context = {'posts': posts}
  print(context)
  return render(request, 'post/index.html', context)

