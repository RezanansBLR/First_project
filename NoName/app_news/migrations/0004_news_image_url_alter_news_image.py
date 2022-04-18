# Generated by Django 4.0.3 on 2022-04-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=' Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
