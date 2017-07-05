from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^Auther/$', AutherSerializerList.as_view()),
    url(r'^Auther/(P<pk>[0-9]/$)', AutherSerializerDetail.as_view()),
    url(r'^Article/$', ArticleSerializerList.as_view()),
    url(r'^Article/(P<pk>[0-9]/$)', ArticleSerializerDetail.as_view()),
    ]