from tabnanny import verbose
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статьи")
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(verbose_name="Содержание")
    datetime = models.DateTimeField(verbose_name="Дата публикации")
    url_source = models.CharField(max_length=200, verbose_name="Источник")
    image = models.ImageField(verbose_name="Изображение")

    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


