from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    phone = models.CharField(max_length=200, null=False, blank=False, verbose_name='Телефон')
    image = models.ImageField(blank=True, null=True,verbose_name = "Аватарка")
    user = models.OneToOneField(User, on_delete=models.PROTECT,related_name='Пользователь')
    friend = models.ManyToManyField(User)
class Post(models.Model):
    title = models.CharField(max_length=75, null=False, blank=False,verbose_name='Заголовок')
    text = models.TextField(max_length=1000, null=True, blank=True,verbose_name='Текст')
    author = models.ForeignKey(User,on_delete=models.PROTECT,related_name='Автор')
    date = models.DateTimeField(auto_now=True,verbose_name = "Дата")
