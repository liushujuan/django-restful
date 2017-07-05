# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.
class AutherSerializerList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AutherSerializer
    
class AutherSerializerDetail(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AutherSerializer
    
class ArticleSerializerList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleSerializerDetail(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
