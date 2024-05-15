from django.contrib import admin

# Register your models here.
from .models import Event, Comment

admin.site.register(Event)
admin.site.register(Comment)