# Generated by Django 5.0.1 on 2024-02-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_featuredcar_is_featured_featuredcar_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredcar',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]