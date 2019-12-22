from django.contrib import admin

from .models import News, NewsCategory

admin.site.register(News)
admin.site.register(NewsCategory)

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}