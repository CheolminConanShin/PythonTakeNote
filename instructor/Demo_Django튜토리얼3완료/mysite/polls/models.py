# encoding:utf-8
from django.db import models
import datetime 
from django.utils import timezone 

# Create your models here.
class Poll(models.Model):
    question=models.CharField('설문 내용', max_length=200)
    pub_date=models.DateTimeField('설문 저장날짜')
    def __str__(self):
        return self.question 
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='최근 발행?'    

class Choice(models.Model):
    poll=models.ForeignKey(Poll)
    choice=models.CharField('설문 보기', max_length=200)
    votes=models.IntegerField()
    def __str__(self):
        return self.choice
