from django.db import models

# 创建表
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
