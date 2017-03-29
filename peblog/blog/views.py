from django.shortcuts import render
from .models import *


from collections import Counter
# Create your views here.


# archives
def archives_info():
    alltimes = [ blog.timestamp.strftime('%Y-%m') for blog in Blog.objects.all() ]
    f_archives = dict(Counter(alltimes))
    sort_archives = [ (key,f_archives[key]) for key in sorted(f_archives.keys()) ]
    sort_archives.reverse()
    archives = dict(sort_archives[:12])
    return archives



def index(request):
    page_id = request.GET.get('page')

    allblogs = Blog.objects.order_by('-timestamp')
    page_id = (page_id,None)[int(page_id)==0]

    if page_id == None :
        blogs = allblogs[:2]
    else:
        last_id = int(page_id) * 2
        next_id = ( int(page_id) + 1 ) * 2
        blogs = allblogs[last_id:next_id]
        if next_id >= len(allblogs):
            next_id = None

    archives = archives_info()
    return render(request, 'index.html',locals())

def page(request,pageid):
    page_id = pageid
    last_id = int(pageid) * 2
    next_id = ( int(pageid) + 1 ) * 2

    allblogs = Blog.objects.order_by('-timestamp')
    blogs = allblogs[last_id:next_id]

    if len(blogs) <= 2:
        next_page = ''
    archives = archives_info()
    return render(request, 'index.html',locals())


def blog(request,number):
    archives = archives_info()

    blog_id = int(number) - 1000
    try:
        articles = Blog.objects.get(id=blog_id)
        naxt_blog = Blog.objects.filter(timestamp__gt=articles.timestamp).first()
        last_blog = Blog.objects.filter(timestamp__lt=articles.timestamp).last()
        print(last_blog,naxt_blog)
    except Exception as e:
        print(e)

    return render(request, 'blog.html',locals())


def archive(request,times):
    archives = archives_info()
    
    blogs = [ blog for blog in Blog.objects.order_by('-timestamp') if blog.timestamp.strftime('%Y-%m') == times ]
    print(blogs)
    return render(request, 'index.html',locals())


def tag(request,tag):
    archives = archives_info()

    blogs = Blog.objects.filter(tag=BlogTag.objects.get(tag=tag).id).order_by('-timestamp')
    return render(request, 'index.html',locals())

