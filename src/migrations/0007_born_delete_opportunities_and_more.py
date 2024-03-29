# Generated by Django 5.0.1 on 2024-01-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_alter_compatibility_text_alter_opportunities_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Born',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('born', models.CharField(max_length=4000)),
            ],
        ),
        migrations.DeleteModel(
            name='Opportunities',
        ),
        migrations.RenameField(
            model_name='compatibility',
            old_name='text',
            new_name='compatibility',
        ),
        migrations.RenameField(
            model_name='usage',
            old_name='text',
            new_name='usage',
        ),
        migrations.AlterField(
            model_name='history_first',
            name='hero',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='history_second',
            name='about',
            field=models.CharField(max_length=4000),
        ),
    ]
