# Generated by Django 3.1.2 on 2021-01-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210107_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodels',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]