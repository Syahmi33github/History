# Generated by Django 3.1.2 on 2021-01-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210107_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodels',
            name='foto1_content1_kelipatan_180pxX230px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='foto1_kelipatan_150pxX200px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='foto2_content1_kelipatan_180pxX230px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='foto2_kelipatan_150pxX200px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='foto3_kelipatan_150pxX200px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='foto_latarbelakang_kelipatan_200pxX300px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='foto_penutup_kelipatan_180pxX230px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='fotokanan_content2_kelipatan_70pxX230px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='fotokiri_content2_kelipatan_70pxX230px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='isi1_content1',
            field=models.TextField(default='content', max_length=310),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='isi2_content1',
            field=models.TextField(default='content', max_length=310),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='isi_content2',
            field=models.TextField(default='content', max_length=320),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='isi_latarbelakang',
            field=models.TextField(default='content', max_length=330),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='isi_penutup',
            field=models.TextField(default='content', max_length=350),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judul_content1_kata_belakang',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judul_content1_kata_depan',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judul_content2_kata_belakang',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judul_content2_kata_depan',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judul_latarbelakang',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judul_penutup_kata_belakang',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judul_penutup_kata_depan',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judulkatabelakang',
            field=models.CharField(default='content', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodels',
            name='judulkatadepan',
            field=models.CharField(default='content', max_length=255),
        ),
    ]
