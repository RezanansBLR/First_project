from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

