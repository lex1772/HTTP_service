from django.db import models

from users.models import User, NULLABLE


class File(models.Model):
    '''Модель для загружаемого файла с полями пользователя, который загрузил файл, самим файлом и датой загрузки'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='пользователь', **NULLABLE)
    upload_file = models.FileField(upload_to='files')
    upload_date = models.DateTimeField(auto_now_add=True)
