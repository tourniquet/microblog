from django.shortcuts import render

from .models import Post

def index(request):
  posts = Post.objects.order_by('-date')
  context = {'posts': posts}
  print(context)
  return render(request, 'post/index.html', context)


def post(request, post_id):
  post = Post.objects.get(id=post_id)
  context = {'post': post}
  return render(request, 'post/post.html', context)
