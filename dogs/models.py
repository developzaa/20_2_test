from django.db import models


class Bread(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название породы', help_text='Введите название породы')
    description = models.TextField(verbose_name='Описание порода', help_text='Введите описание породы', blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кличка', help_text='Введите кличку')
    bread = models.ForeignKey(Bread, on_delete=models.SET_NULL, verbose_name='Порода', help_text='Введите породу',
                              blank=True,
                              null=True, related_name='dogs')
    photo = models.ImageField(upload_to='dogs/photo', blank=True, null=True, verbose_name='Фото',
                              help_text='Вставьте фото')
    date_born = models.DateField(blank=True, null=True, verbose_name='Дата рождения',
                                     help_text='Укажите дату рождения')

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ['bread', 'name']

    def __str__(self):
        return self.name
