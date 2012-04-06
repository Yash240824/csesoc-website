from app.news.models import *

from django.contrib import admin


class NewsItemInline(admin.TabularInline):
	model = NewsItem
	extra = 1

class PostAdmin(admin.ModelAdmin):
	inlines = [NewsItemInline]

admin.site.register(Post, PostAdmin)

class NewsItemAdmin(admin.ModelAdmin):
	list_display = ('headline','tag','post')
admin.site.register(NewsItem, NewsItemAdmin)


class TagAdmin(admin.ModelAdmin):
	list_display = ('name','colour')

admin.site.register(Tag, TagAdmin)



