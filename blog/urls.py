from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title") ,
    url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
    #在这里并不明确name属性所指意思
    #构成入口链接，以行使调用，我所知道的调用为HTML中的调用

]

