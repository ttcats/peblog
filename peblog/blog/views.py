# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.conf import settings

from django.core.mail import send_mail
from collections import Counter


# 按时间归档
def archives_info():
    alltimes = [blog.timestamp.strftime('%Y-%m')
                for blog in Blog.objects.all()]
    f_archives = dict(Counter(alltimes))
    sort_archives = [(key, f_archives[key])
                     for key in sorted(f_archives.keys())]
    sort_archives.reverse()
    archives = dict(sort_archives[:12])
    return archives


# 按标签分类
def tags_info():
    alltags = BlogTag.objects.all()
    return list( tags.tag for tags in alltags )


# 分页
def pages_info(page_id, allblogs):
    articlenumber = settings.ARTICLE_NUMBER
    page_id = (page_id, None)[int(page_id) == 0]
    if page_id is None and len(allblogs) <= int(articlenumber):
        blogs = allblogs
        nextpage_id = None
    elif page_id is None and len(allblogs) > int(articlenumber):
        blogs = allblogs[:int(articlenumber)]
        nextpage_id = 1
    else:
        last_id = int(page_id) * int(articlenumber)
        next_id = (int(page_id) + 1) * int(articlenumber)
        blogs = allblogs[last_id:next_id]
        nextpage_id = int(page_id) + 1
        if next_id >= len(allblogs):
            nextpage_id = None
    return [page_id, nextpage_id, blogs]

def index(request):
    page_id = request.GET.get('page', 0)
    allblogs = Blog.objects.order_by('-timestamp')

    list_tags = tags_info()
    [page_id, nextpage_id, blogs] = pages_info(page_id, allblogs)
    archives = archives_info()
    return render(request, 'index.html', locals())


def blog(request, number):
    list_tags = tags_info()
    archives = archives_info()
    blog_id = int(number) - 1000
    try:
        articles = Blog.objects.get(id=blog_id)
        last_blog = Blog.objects.filter(
            timestamp__lt=articles.timestamp).order_by('timestamp').last()
        next_blog = Blog.objects.filter(
            timestamp__gt=articles.timestamp).order_by('timestamp').first()
        print(last_blog, next_blog)
    except Exception as e:
        print(e)
    return render(request, 'blog.html', locals())


def archive(request, times):
    page_id = request.GET.get('page', 0)
    list_tags = tags_info()
    archives = archives_info()

    allblogs = [blog for blog in Blog.objects.order_by(
        '-timestamp') if blog.timestamp.strftime('%Y-%m') == times]
    print(pages_info(page_id, allblogs))
    [page_id, nextpage_id, blogs] = pages_info(page_id, allblogs)
    return render(request, 'archives.html', locals())


def tag(request, tag):
    page_id = request.GET.get('page', 0)
    archives = archives_info()
    list_tags = tags_info()

    allblogs = Blog.objects.filter(
        tag=BlogTag.objects.get(
            tag=tag).id).order_by('-timestamp')
    [page_id, nextpage_id, blogs] = pages_info(page_id, allblogs)
    return render(request, 'tags.html', locals())


def search(request):
    # print(request.GET)
    archives = archives_info()
    list_tags = tags_info()
    page_id = request.GET.get('page', 0)
    search_info = request.GET.get('search', '')

    allblogs = Blog.objects.filter(title__icontains=search_info)
    [page_id, nextpage_id, blogs] = pages_info(page_id, allblogs)
    return render(request, 'search.html', locals())


@csrf_exempt
def comment(request, blogid):
    blog_id = int(blogid) - 1000
    title = Blog.objects.get(id=blog_id)
    comment, critic = request.POST.get('comment'), request.POST.get('critic')
    # print(comment,critic,title)
    BlogComment.objects.create(title=title, intro=comment, randomname=critic)

    send_title = '评论: ' + title.title
    send_content = '来自: ' + critic + '\n' + '内容: ' + comment
    send_tomail = title.email
    if send_tomail:
        try:
            send_mail(send_title,send_content,'pemonkey@sina.com',[send_tomail])
        except Exception as e:
            print(e)

    return HttpResponse("ok")
