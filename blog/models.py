# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class UserInfo(AbstractUser):
#     nick_name=models.CharField(max_length=15,verbose_name='昵称')
#     gender=models.CharField(max_length=5,choices=(('male',u'男'),('fomale',u'女')),default='male',verbose_name='性别')
#     image=models.ImageField(max_length=50,upload_to='image/%Y/%m',default='image/default.png')
class Post(models.Model):
    author=models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200,verbose_name='标题')
    text=models.TextField(verbose_name='内容')
    created_time=models.DateTimeField(default=timezone.now(),verbose_name='创建时间')
    published_date=models.DateTimeField(blank=True,null=True,verbose_name='发布时间')

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name
