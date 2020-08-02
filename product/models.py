from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=True, null=True)
    icon_url = models.CharField(max_length=2083, blank=True, null=True)
    active = models.BooleanField(default=False, help_text='If not active, this category will be hidden in category page.')

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(primary_key=True, default=1001, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    unit_system = models.CharField(max_length=255, choices=(('kg', 'KG'), ('item', 'Item'), ('both', 'KG & Item'), ))
    price_per_kg = models.FloatField(default=0)
    price_per_item = models.FloatField(default=0)
    minimum_buy_in_kg = models.FloatField(default=1)
    maximum_buy_in_kg = models.FloatField(default=10)
    minimum_buy_in_item = models.FloatField(default=5)
    maximum_buy_in_item = models.FloatField(default=20)
    icon_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
