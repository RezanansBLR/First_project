from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta():
       verbose_name = "Категория"
       verbose_name_plural = "Категории" 

    def __str__(self):
        return self.title
       

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статьи")
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Содержание")
    datetime = models.DateTimeField(verbose_name="Дата публикации")
    url_source = models.CharField(max_length=200, verbose_name="Источник")
    image = models.ImageField(verbose_name="Изображение")

    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
        

