from django.db import models

# Create your models here.
class Transaction(models.Model):
    value = models.DecimalField(decimal_places=0, max_digits=10)
    name = models.CharField(max_length=20)
    date = models.DateField()

    #아래의 메서드를 만들어 두면 데이터 표현시에
    #문자열로 리턴해 준다. 
    def __str__(self):
        return self.name 
