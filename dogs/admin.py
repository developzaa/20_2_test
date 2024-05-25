from django.contrib import admin
from dogs.models import Dog, Bread


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "bread")
    list_filter = ("bread",)
    search_fields = ("name",)


@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
