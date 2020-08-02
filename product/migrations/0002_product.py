# Generated by Django 2.1 on 2020-08-02 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(default=1001, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('unit_system', models.CharField(choices=[('kg', 'KG'), ('item', 'Item'), ('both', 'KG & Item')], max_length=255)),
                ('price_per_kg', models.FloatField(default=0)),
                ('price_per_item', models.FloatField(default=0)),
                ('minimum_buy_in_kg', models.FloatField(default=1)),
                ('maximum_buy_in_kg', models.FloatField(default=10)),
                ('minimum_buy_in_item', models.FloatField(default=5)),
                ('maximum_buy_in_item', models.FloatField(default=20)),
                ('icon_url', models.CharField(max_length=2083)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
    ]