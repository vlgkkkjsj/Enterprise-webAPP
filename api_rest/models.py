from django.db import models

class User(models.Model):

    nickname = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=100, default='')
    age = models.CharField(max_length=100, default='')
    login = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    
    def __str__(self) :
        return f'nickname: {self.nickname} | name:{self.name}'


    
    