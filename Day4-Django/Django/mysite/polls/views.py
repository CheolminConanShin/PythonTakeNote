from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
from django.template import Context, loader

# Create your views here.
def index(request):
    # DB에 있는 Poll 데이터를 호출
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    # html template을 load해서
    t = loader.get_template('polls/index.html')
    # html template에 데이터를 populate
    c = Context({'latest_poll_list':latest_poll_list,})
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    return HttpResponse('보고 있는 설문: %s' % poll_id)

def results(request, poll_id):
    return HttpResponse('설문 결과: %s' % poll_id)

def vote(request, poll_id):
    return HttpResponse('투표하기: %s' % poll_id)