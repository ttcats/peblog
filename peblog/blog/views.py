#coding=utf-8
from django.shortcuts import render
from .models import *
from django.conf import settings

from collections import Counter
# Create your views here.


# 按时间归档
def archives_info():
    alltimes = [ blog.timestamp.strftime('%Y-%m') for blog in Blog.objects.all() ]
    f_archives = dict(Counter(alltimes))
    sort_archives = [ (key,f_archives[key]) for key in sorted(f_archives.keys()) ]
    sort_archives.reverse()
    archives = dict(sort_archives[:12])
    return archives


# 分页
def pages_info(page_id,allblogs):
    articlenumber = settings.ARTICLE_NUMBER
    
    page_id = (page_id,None)[int(page_id)==0]
    if page_id == None and len(allblogs) <= int(articlenumber):
        blogs = allblogs
        nextpage_id = None
    elif page_id == None and len(allblogs) > int(articlenumber):
        blogs = allblogs[:int(articlenumber)]
        nextpage_id = 1
    else:
        last_id = int(page_id) * int(articlenumber)
        next_id = ( int(page_id) + 1 ) * int(articlenumber)
        blogs = allblogs[last_id:next_id]
        nextpage_id = int(page_id) + 1
        if next_id >= len(allblogs):
            nextpage_id = None

    return [page_id,nextpage_id,blogs]



def index(request):
    page_id = request.GET.get('page',0)
    allblogs = Blog.objects.order_by('-timestamp')

    [page_id,nextpage_id,blogs] = pages_info(page_id,allblogs)
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
    page_id = request.GET.get('page',0)
    archives = archives_info()
    
    allblogs = [ blog for blog in Blog.objects.order_by('-timestamp') if blog.timestamp.strftime('%Y-%m') == times ]
    print(pages_info(page_id,allblogs))
    [page_id,nextpage_id,blogs] = pages_info(page_id,allblogs)
    return render(request, 'archives.html',locals())


def tag(request,tag):
    page_id = request.GET.get('page',0)
    archives = archives_info()

    allblogs = Blog.objects.filter(tag=BlogTag.objects.get(tag=tag).id).order_by('-timestamp')
    [page_id,nextpage_id,blogs] = pages_info(page_id,allblogs)
    return render(request, 'tags.html',locals())

