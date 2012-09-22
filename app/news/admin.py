from app.news.models import *
from django.contrib import admin

class CommonMedia:
  js = (
	'https://ajax.googleapis.com/ajax/libs/dojo/1.7.1/dojo/dojo.js',
	'/assets/js/editor.js',
  )
  css = {
	'all': ('/assets/css/editor.css',),
  }

class ItemInline(admin.TabularInline):
	model = Item
	extra = 1

class PostAdmin(admin.ModelAdmin):
	inlines = [ItemInline]

admin.site.register(Post, PostAdmin)

class ItemAdmin(admin.ModelAdmin):
	list_display = ('headline','tag','post')
#admin.site.register(Item, ItemAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ('name','colour')
admin.site.register(Tag, TagAdmin)
