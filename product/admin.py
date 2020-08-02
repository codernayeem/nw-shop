from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'active')


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ('id', 'name', 'category', 'unit_system', 'price_per_kg', 'price_per_item', 'stock')
    fieldsets = (
        (None, {
            'fields': ('id', 'name', 'description', 'category', 'stock', 'unit_system')
        }),
        ('Unit KG', {
            'fields': ('price_per_kg', 'minimum_buy_in_kg', 'maximum_buy_in_kg'),
        }),
        ('Unit Item', {
            'fields': ('price_per_item', 'minimum_buy_in_item', 'maximum_buy_in_item'),
        }),
        (None, {
            'fields': ('icon_url',)
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
