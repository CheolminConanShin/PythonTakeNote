from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class PollAdmin(admin.ModelAdmin):
    fieldsets=[('설문 관련 내용',{'fields':['question']}), \
        ('날짜 관련 내용',{'fields':['pub_date'], 'classes':['collapse']}), ]
    inlines=[ChoiceInline] 
    list_display=('question', 'pub_date', 'was_published_recently')
    list_filter=['pub_date']
    search_fields=['question']
    
# Register your models here.
admin.site.register(Poll, PollAdmin)

