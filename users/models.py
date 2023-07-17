from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    '''Модель пользователя с переопределенным username на почту и полями ФИО, почта и блокировка пользователя'''
    username = None

    full_name = models.CharField(max_length=255, verbose_name='ФИО', **NULLABLE)
    email = models.EmailField(max_length=254, unique=True, verbose_name='email')
    is_active = models.BooleanField(default=True, verbose_name='активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'