import datetime

from django.db import models


class Cat(models.Model):
    nick = models.CharField(max_length=50, blank=False, null=False, verbose_name='Кличка котэ')
    breed = models.CharField(max_length=80, blank=False, null=False, verbose_name='Порода котэ')
    created = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата публикации')
    owner_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Имя владельца')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Адрес для браузера')
    info = models.TextField(blank=True, verbose_name='Информация о котэ')
    photo = models.ImageField(blank=False, upload_to='%Y/', verbose_name='Фото')

    class Meta:
        ordering = ('-created',)
