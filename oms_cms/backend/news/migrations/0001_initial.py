# Generated by Django 2.2.5 on 2019-09-16 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oms_gallery', '0002_auto_20190714_1348'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('en', 'English'), ('ru', 'Russian')], default='en', max_length=7, verbose_name='Язык')),
                ('slug', models.SlugField(blank=True, help_text='Укажите url', max_length=500, null=True, verbose_name='url')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='', max_length=1000, verbose_name='Описание')),
                ('template', models.CharField(default='news/post_list.html', max_length=500, verbose_name='Шаблон')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('paginated', models.PositiveIntegerField(default=5, verbose_name='Количество новостей на странице')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='news.Category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория новостей',
                'verbose_name_plural': 'Категории новостей',
                'unique_together': {('lang', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тег')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='url')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('en', 'English'), ('ru', 'Russian')], default='en', max_length=7, verbose_name='Язык')),
                ('slug', models.SlugField(blank=True, help_text='Укажите url', max_length=500, null=True, verbose_name='url')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='Под заголовок')),
                ('mini_text', models.TextField(max_length=5000, verbose_name='Краткое содержание')),
                ('text', models.TextField(max_length=10000000, verbose_name='Полное содержание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edit_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата редактирования')),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата публикации')),
                ('template', models.CharField(default='news/post_detail.html', max_length=500, verbose_name='Шаблон')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('viewed', models.IntegerField(default=0, verbose_name='Просмотрено')),
                ('status', models.BooleanField(default=False, verbose_name='Для зарегистрированных')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='Категория')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oms_gallery.Photo', verbose_name='Главная фотография')),
                ('tag', models.ManyToManyField(blank=True, to='news.Tags', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['sort', '-published_date'],
                'unique_together': {('lang', 'slug')},
            },
        ),
    ]
