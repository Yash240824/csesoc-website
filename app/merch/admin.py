from django.contrib import admin
from app.merch.models import Hoodie

class HoodieAdmin(admin.ModelAdmin):
  list_filter = ('size','gender', 'payment_status')
  list_display = ('full_name', 'email_address', 'contact_number', 'gender', 'size','payment_status')

admin.site.register(Hoodie, HoodieAdmin)