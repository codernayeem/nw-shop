from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'active')


admin.site.register(Category, CategoryAdmin)
