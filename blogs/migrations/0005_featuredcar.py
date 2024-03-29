# Generated by Django 5.0.1 on 2024-02-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('main_traits', models.TextField(max_length=500)),
                ('price_range', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='featured_cars/%Y/%m/%d')),
                ('description', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
