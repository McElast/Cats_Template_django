from django.contrib import admin

from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = ['nick', 'created']


# Надо исправить: Обе модели регистрируем в админке
admin.site.register(Cat, CatAdmin)
