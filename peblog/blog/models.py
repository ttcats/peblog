#coding: utf-8
from django.db import models


from ckeditor.fields import RichTextField

# Create your models here.


#from ckeditor_uploader.fields import RichTextUploadingField
#class Entry(models.Model):
#    body = RichTextUploadingField() #RichTextField()

#from ckeditor.fields import RichTextField
#class Post(models.Model):
#    content = RichTextField()




class BlogTag(models.Model):
    tag = models.CharField(max_length = 30)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'



class Blog(models.Model):
    title = models.CharField(max_length = 150)
    tag = models.ManyToManyField(BlogTag,)
    author = models.CharField(max_length = 30)
    #body = models.TextField()
    body = RichTextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = u'博客'


class BlogComment(models.Model):
    title = models.ForeignKey(Blog,related_name="title_id")
    intro = models.CharField(max_length = 800)
    randomname = models.CharField(max_length = 30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = u'评论'
