# Generated by Django 5.0.1 on 2024-01-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_alter_history_second_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compatibility',
            name='text',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='opportunities',
            name='text',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='usage',
            name='text',
            field=models.CharField(max_length=4000),
        ),
    ]