# Generated by Django 5.0.1 on 2024-01-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0012_graphs'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitySalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('text', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='CitySalaryCpp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('text', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('text', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyRateCpp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('text', models.CharField(max_length=4000)),
            ],
        ),
        migrations.RenameField(
            model_name='graphs',
            old_name='city_salary',
            new_name='graphsCS',
        ),
        migrations.RenameField(
            model_name='graphs',
            old_name='city_salary_cpp',
            new_name='graphsCSC',
        ),
        migrations.RenameField(
            model_name='graphs',
            old_name='vacancy_rate',
            new_name='graphsVR',
        ),
        migrations.RenameField(
            model_name='graphs',
            old_name='vacancy_rate_cpp',
            new_name='graphsVRC',
        ),
    ]