# Generated by Django 3.1.2 on 2021-01-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210120_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodels',
            name='penulis',
            field=models.CharField(default='Sam', max_length=50),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='slide',
            field=models.CharField(default='5', max_length=5),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='sumber',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]