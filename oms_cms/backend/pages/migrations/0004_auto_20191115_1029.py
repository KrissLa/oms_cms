# Generated by Django 2.2.5 on 2019-11-15 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oms_gallery', '0002_auto_20190714_1348'),
        ('pages', '0003_pages_sub_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockpage',
            name='slider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oms_gallery.Gallery', verbose_name='Слайдер'),
        ),
        migrations.AddField(
            model_name='blockpage',
            name='video_link',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ссылка на видео'),
        ),
        migrations.AddField(
            model_name='blockpage',
            name='video_up',
            field=models.FileField(blank=True, null=True, upload_to='block_page/video/', verbose_name='Видео'),
        ),
    ]