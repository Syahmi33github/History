# Generated by Django 3.1.2 on 2021-01-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_postmodels_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodels',
            name='isi_penutup',
            field=models.TextField(default='content', max_length=500),
        ),
    ]