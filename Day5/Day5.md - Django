### Day 5
#### Django Template Setting
- mysite > settings.py 파일에서 dir에 디렉토리 추가
```python
'DIRS': [
    'C:/Users/student/Documents/note/Day4-Django/Django/mysite/mytemplates/admin',
    'C:/Users/student/Documents/note/Day4-Django/Django/mysite/mytemplates',
],
```
- admin template을 복사한다
    1. 초기에 Django를 설치한 폴더에
    Lib > site-packages > Django-1.9.1-py3.4.egg > django > contrib > admin > templates
    안에 admin 폴더를 mytemplates 폴더 안으로 복사한다.
- poll 폴더에 urls.py파일 수정
```python
from django.conf.urls import include, url
from . import views # 같은 디렉토리에 views파일을 import

#정규표현식을 통해 요청한 url주소를 함수로 맴핑해서 처리
urlpatterns = [
    url(r'^$', 'polls.views.index'),
    url(r'^(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
]
```
- polls > views.py 파일 작성
```python
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
```

- mytemplates안에 polls폴더 생성, 해당 폴더 안에 index.html파일 생성
```html
# mytemplates > polls > index.html
{%if latest_poll_list%}
<ul>
{%for poll in latest_poll_list%}
<li><a href="/polls/{{poll.id}}/">{{poll.question}}</a></li>
{%endfor%}
</ul>
{%else%}
<p>No polls are available.</p>
{%endif%}
```


