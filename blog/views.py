from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
all_posts = Post.objects.all()


def index(request):
    paginatior = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginatior.get_page(page_number)
    #Getting data from post model
    return render(request, 'index.html', {'Blog_title': "Naren' s Blog", 'page_obj': page_obj})


def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')

    # logger = logging.getLogger('testing')
    # logger.debug(f'post variable is {post}')
    return render(request, 'detail.html', {'post': post, 'related_posts': related_posts})


def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse('Tis is new url redirect.')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger('testing')
        if form.is_valid():
            logger.debug(f"post data is {form.cleaned_data['name']} and {form.cleaned_data['email']} and {form.cleaned_data['message']}")
            succ_msg = 'Successfully created.'
            return render(request, 'contact.html', {'form': form,'message': succ_msg})
        else:
            logger.debug('validation failed')

        return render(request, 'contact.html', {'form': form, 'name':name, 'email':email, 'message':message})

    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')