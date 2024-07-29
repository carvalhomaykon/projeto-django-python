from django.contrib import admin
from contact import models

@admin.register (models.Contact)
# Register your models here.
class ContactAdmin (admin.ModelAdmin):
    ...