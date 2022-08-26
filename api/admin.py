from django.contrib import admin
from .models import *
# Register your models here.

class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "company", "phone", "status")
    search_fields = ("id", "email", "name", "company", "phone", "status")
    
admin.site.register(Recipient,RecipientAdmin)