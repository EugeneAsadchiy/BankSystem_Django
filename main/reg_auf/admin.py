from django.contrib import admin, messages
from django.db.models import QuerySet
# Register your models here.
from .models import User

# admin.site.register(Director)
# admin.site.register(Actor)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "password"]

