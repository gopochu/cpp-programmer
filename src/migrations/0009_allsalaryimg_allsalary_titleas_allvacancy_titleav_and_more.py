# Generated by Django 5.0.1 on 2024-01-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_allsalary_allvacancy_cppsalary_cppvacancy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllSalaryImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_salary_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='allsalary',
            name='titleAS',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allvacancy',
            name='titleAV',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='born',
            name='titleB',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compatibility',
            name='titleC',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cppsalary',
            name='titleCS',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cppvacancy',
            name='titleCV',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='demandheader',
            name='titleDH',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history_first',
            name='titleF',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history_second',
            name='titleS',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usage',
            name='titleU',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]