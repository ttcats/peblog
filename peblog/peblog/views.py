#coding=utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseRedirect

import time


@csrf_exempt
def uploadimg(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.GET)
        callback = request.GET.get('CKEditorFuncNum')
        path = "static/upload/" + time.strftime("%Y%m%d%H%M%S",time.localtime())
        f = request.FILES["upload"]
        file_name = path + "_" + f.name
        with open(file_name,'wb+') as s:
            for info in f:
                s.write(info)
        res = r"<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"','success');</script>"
        return HttpResponse(res)
        print(res)
    
