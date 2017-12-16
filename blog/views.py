from django.shortcuts import render ,get_object_or_404
from .models import BlogArticles

#此类函数称为“视图函数”
def blog_title(request):
    blogs = BlogArticles.objects.all()
    #此语句得到BlogArticles的所有对象实例
    return render(request, "blog/titles.html", {"blogs":blogs})


def blog_article(request, article_id):
    #article = BlogArticles.objects.get(id=article_id)
    article =get_object_or_404(BlogArticles , id=article_id)
    #可以促发Http404错误，而不是模型的DoesNotExist 异常
    pub= article.publish
    return render(request, "blog/content.html", { "article":article , "publish":pub})


# Create your views here.
