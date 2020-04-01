from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hospital(models.Model):
    """"医院方"""
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    last_login=models.DateField(auto_now=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name[:20]+'...'


class M_material(models.Model):
    """医疗物资的情况"""

    #定义模板常量
    mask='mask'
    protective_suit='protective_suit'
    goggles='goggles'
    bloodbag='bloodbag'

    #医疗物资名称的元组
    MATERIAL_CHOICE=((mask,'mask'),(protective_suit,'protective_suit'),
                     (goggles,'goggles'),(bloodbag,'bloodbag'),)

    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,choices=MATERIAL_CHOICE)
    need_num=models.IntegerField()
    urgency=models.IntegerField()

    def __str__(self):
        return self.name + str(self.need_num)




