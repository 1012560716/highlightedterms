
#coding:utf-8
from django.db import models
from DjangoUeditor.models import UEditorField


class userinfo(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()

class newsinfo(models.Model):

    title = models.TextField()                  # 标题
    content = models.TextField()                # 正文
    people = models.CharField(max_length=255)   # 人名
    toponymy = models.CharField(max_length=255) # 地名
    organization =models.CharField(max_length=255)  #机构

    people_num = models.IntegerField() # 人名数
    toponymy_num = models.IntegerField() # 地名数
    organization_num = models.IntegerField() # 机构数

    people_error = models.CharField(max_length=255)  # 错误人名
    people_error_num = models.IntegerField()  # 错误人名数
    people_miss = models.CharField(max_length=255)  # 漏掉人名
    people_miss_num = models.IntegerField()  # 漏掉人名数

    toponymy_error = models.CharField(max_length=255)  # 错误地名
    toponymy_error_num = models.IntegerField()  # 错误地名数
    toponymy_miss = models.CharField(max_length=255)  # 漏掉地名
    toponymy_miss_num = models.IntegerField()  # 漏掉地名数

    organization_error = models.CharField(max_length=255)  # 错误机构
    organization_error_num = models.IntegerField()  # 错误机构数
    organization_miss = models.CharField(max_length=255)  # 漏掉机构
    organization_miss_num = models.IntegerField()  # 漏掉机构数






