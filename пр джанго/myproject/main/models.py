from django.db import models


class Staf(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    email = models.CharField('Почта', max_length=50)
    ind = models.CharField('Индекс', max_length=50)
    program = models.CharField('Должность', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
