from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-views')[:5]
    context = {'posts': posts}
    return render(request, 'index.html', context)
