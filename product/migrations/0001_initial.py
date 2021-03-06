# Generated by Django 2.1 on 2020-08-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('icon_url', models.CharField(blank=True, max_length=2083, null=True)),
                ('active', models.BooleanField(default=False, help_text='If not active, this category will be hidden in category page.')),
            ],
        ),
    ]
