# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
from django.template import Context, loader

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c=Context({'latest_poll_list':latest_poll_list, })
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    return HttpResponse('보고 있는 설문: %s'%poll_id)

def results(request, poll_id):
    return HttpResponse('설문의 결과 보기: %s'%poll_id)

def vote(request, poll_id):
    return HttpResponse('설문 투표: %s'%poll_id)