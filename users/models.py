from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=30, **NULLABLE,verbose_name='Имя')
    second_name = models.CharField(max_length=30, **NULLABLE, verbose_name='Фамилия')

    phone = models.CharField(max_length=20, unique=True, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', **NULLABLE, verbose_name='Аватар')
    country = models.CharField(max_length=20, **NULLABLE, verbose_name='Страна')
    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
