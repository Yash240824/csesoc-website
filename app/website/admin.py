from app.website.models import *
from django.contrib import admin


# we define our resources to add to admin pages
class CommonMedia:
  js = (
	'https://ajax.googleapis.com/ajax/libs/dojo/1.7.1/dojo/dojo.js',
	'/assets/js/editor.js',
  )
  css = {
	'all': ('/assets/css/editor.css',),
  }

# let's add it to this model
admin.site.register(About,
  Media = CommonMedia,
)

# admin.site.register(About)
admin.site.register(FunStuff)
admin.site.register(Team)
admin.site.register(Slug)
admin.site.register(Sponsor)
