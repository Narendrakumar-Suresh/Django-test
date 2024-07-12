from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404

# Create your views here.
posts = Post.objects.all()
def index(request):
    #Getting data from post model
    return render(request, 'index.html', {'Blog_title': "Naren' s Blog", 'posts': posts })


def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')

    # logger = logging.getLogger('testing')
    # logger.debug(f'post variable is {post}')
    return render(request, 'detail.html', {'post': post})


def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse('Tis is new url redirect.')