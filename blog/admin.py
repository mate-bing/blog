from django.contrib import admin
from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fileds = ('title', "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish', 'author']


admin.site.register(BlogArticles , BlogArticlesAdmin)
#将该类(BlogArticles)注册到admin中
#将类BlogArticlesAdmin注册到admin中

# Register your models here.
