from app.news.models import *
from django.contrib import admin

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
