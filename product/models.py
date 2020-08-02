from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=True, null=True)
    icon_url = models.CharField(max_length=2083, blank=True, null=True)
    active = models.BooleanField(default=False, help_text='If not active, this category will be hidden in category page.')

    def __str__(self):
        return self.name
