# Generated by Django 5.0.1 on 2024-01-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0010_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageAS',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageAV',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageCS',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageCV',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
