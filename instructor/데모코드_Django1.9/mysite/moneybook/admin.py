from django.contrib import admin
from moneybook.models import Transaction

# 날짜와 지출금액이 같이 출력될 수 있도록 수정한다.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'value')

# Register your models here.
admin.site.register(Transaction, TransactionAdmin)

