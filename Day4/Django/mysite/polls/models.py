from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
    question = models.CharField('설문내용', max_length=200)
    pub_date = models.DateTimeField('설문 저장 날짜')
    def __str__(self): # 문자열을 리턴하는 메서드
        return self.question
    # 최근에 발행된 설문인지 여부를 리턴
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "최근 발행 여부"

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField('설문 보기', max_length=200)
    votes = models.IntegerField()
    def __str__(self):
        return self.choice