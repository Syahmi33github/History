# Generated by Django 3.1.2 on 2021-01-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20210127_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodels',
            name='isi_penutup',
            field=models.TextField(default='content', max_length=460),
        ),
    ]
