# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

 
# Create your models here.
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    addr = models.TextField()
    qq = models.IntegerField()
    def __str__(self):
        return self.name
    
@python_2_unicode_compatible
class Article(models.Model):
    STATUS_CHOICES = (
        ('e','edit'),
        ('p','published'),
        )
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=300)
    context = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    category = models.ForeignKey('Category',verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-last_modified_time'] 
           
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name