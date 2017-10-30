from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64,unique=True)
    brief = models.CharField(max_length=256,verbose_name='简介',blank=True,null=True)
    sex_choices = ((0,'女'),(1,'男'))
    sex = models.IntegerField(choices=sex_choices)
    followed_list = models.ManyToManyField('UserProfile',verbose_name='我的关注')
    head_img = models.ImageField("Tags",blank=True)

    def __str__(self):
        return self.name

class Weibo(models.Model):

    content = models.CharField(max_length=160)
    user = models.ForeignKey(UserProfile)
    wb_type_choices = (
        (0,'new'),
        (1,'forward'), #转发
        (2,'collect'),  #收藏
    )
    wb_type = models.IntegerField(choices=wb_type_choices,default=0)