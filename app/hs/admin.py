from app.hs.models import *
from django.contrib import admin

class RegistrationAdmin(admin.ModelAdmin):
  list_filter = ('course', 'gender')
  list_display = ('full_name', 'email', 'level', 'gender', 'highschool', 'laptop')
  #actions = []

admin.site.register(Course)
admin.site.register(Registration, RegistrationAdmin)
