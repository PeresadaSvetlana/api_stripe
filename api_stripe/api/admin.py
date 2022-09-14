from django.contrib import admin
from .models import Item


@admin.register(Item)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    search_fields = ('name', 'description', 'price')
    empty_value_display = '-пусто-'
