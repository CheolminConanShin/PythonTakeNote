from django.conf.urls import include, url
from . import views # 같은 디렉토리에 views파일을 import

#정규표현식을 통해 요청한 url주소를 함수로 맴핑해서 처리
urlpatterns = [
    url(r'^$', 'polls.views.index'),
    url(r'^(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
]