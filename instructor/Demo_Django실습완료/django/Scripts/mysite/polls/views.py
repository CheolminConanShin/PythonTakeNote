from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice,Poll


# Create your views here.
def index(request):
    latest_poll_list=Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', \
                              {'latest_poll_list':latest_poll_list})

def detail(request,poll_id):
    p=get_object_or_404(Poll,pk=poll_id)
    return render_to_response('polls/detail.html', \
                              {'poll':p},context_instance=RequestContext(request))

def results(request,poll_id):
    p=get_object_or_404(Poll,pk=poll_id)
    return render_to_response('polls/results.html',{'poll':p})

def vote(request,poll_id):
    p=get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        # 투표 폼을 다시 보여주기.
        return render_to_response('polls/detail.html',{ \
            'poll':p, \
            'error_message':"You didn't select a choice.", \
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 전송된 POST 자료를 성공적으로 처리한 뒤에는
        #항상 HttpResponseRedirect를 반환합니다.
        # 자료가 두 번 전송되는 경우를 막아줍니다.
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
