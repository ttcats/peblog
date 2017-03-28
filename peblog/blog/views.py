from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    print(BlogTag.objects.all())
    blogs = Blog.objects.all()
    return render(request, 'index.html',locals())
