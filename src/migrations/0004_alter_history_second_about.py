# Generated by Django 5.0.1 on 2024-01-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_rename_first_history_first_hero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_second',
            name='about',
            field=models.CharField(max_length=1000),
        ),
    ]
