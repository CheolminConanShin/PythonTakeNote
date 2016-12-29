### 본격 Django 가이드
#### Installation
- 먼저 [Django.tar.gz](Django/Django-1.9.1.tar.gz) 파일을 다운 받는다
- 원하는 경로에 압축을 푼다
- 환경변수 Setting
	1. C:\Python34와 C:\Python34\Scripts를 path에 추가
	2. C:\django\Lib\site-packages를 PYTHONPATH에 추가
- 필요한 디렉토리 설정
	1. C:\ 밑에 django 폴더를 생성한다
	2. C:\django\ 밑에 Lib 폴더를 생성한다
	3. C:\django\Lib\ 밑에 site-packages 폴더를 생성한다
- 기존에 Django 압축 해제를 한 폴더로 이동해서 `python setup.py install --prefix=c:\django` 실행

#### Project 생성/실행
- Django가 설치된 디렉토리로 이동해서 `django-admin-script.py startproject mysite` 실행
- mysite 디렉토리로 이동해서 `python manage.py runserver [port]` 실행하면 Test Server가 가동된다
- mysite 프로젝트 내부에 settings.py에서
	1. DATABASES 속성에서 db이름을 'db.sqlite3' -> 'sample.db'로
	2. LANGUAGE_CODE를 'ko-kr'로
	3. TIME_ZONE을 'KST'로 변경
- `python manage.py migrate`명령어로 필요한 테이블을 생성하기 위해 migration을 실행
- `python manage.py createsuperuser --username=admin --email=admin@naver.com`로 superuser 생성
- superuser에 대한 비밀번호 설정 (복잡하게 만들어야 한다....)
- 어플리케이션 실행 `python manage.py startapp polls`

#### Project Model 생성
- polls라는 디렉토리에 models.py 파일에 해당 클래스 생성
	```python
	from django.db import models
	
	class Poll(models.model):
		question = models.CharField('설문내용', max_length=200)
		pub_date = models.DateTimeField('설문 저장 날짜')

	class Choice(models.model):
		poll = models.ForeignKey(Poll)
		choice = models.CharField('설문 보기', max_length=200)
		votes = models.IntegerField()
	```
- mysite 디렉토리 안에 settings.py에 polls를 추가
- 변경 사항을 적용 전 확인 한다 `python manage.py makemigrations`
- 필요한 기본 인프라를 추가 한다 `python manage.py migrate`
- Shell 스크립트로 들어가서 적용된 사항들을 확인한다 `python manage.py shell`
	1. 생성한 model들을 import `from polls.models import Poll, Choice`
	2. 현재 존재하는 poll list 호출 `Poll.objects.all()` => [] 빈 리스트
	3. 샘플 Poll을 생성해 보자
		```python
		from django.utils import timezone
		p = Poll(question="What's new?", pub_date=timezone.now())
		p.save()
		p.id
		# 1 자동 생성된 id
		p.question
		# "What's new?"
		p.pub_date
		# datetime.datetime(2016, 12, 29, 6, 48, 43, 852581, tzinfo=<UTC>)
		```
	4. Poll을 수정해 보자
		```python
		p.question = "What's up?"
		p.save()
		p.question
		# "What's up?" 수정된게 확인된다
		```

#### Poll & Choice Model 수정
- Model에 문자열을 리턴하는 함수 정의
	1. Poll class에 함수 추가
		def __str__(self): # 문자열을 리턴하는 함수
			return self.question
		def was_published_recently(self): # 발행된지 하루가 지났는지 확인하는 함수
			return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	2. Choice class에 함수 추가
		def __str__(self):
			return self.choice
- Shell 스크립트로 돌아가서 Poll을 확인할 수 있다
	```python
	from polls.models import Poll, Choice
	Poll.objects.all()
	# [<Poll: What's up?>]
	Poll.objects.filter(id=1)
	# [<Poll: What's up?>]
	Poll.objects.get(id=1)
	# <Poll: What's up?>
	```
- 특정 Poll을 참조
	```python
	p = Poll.objects.get(pk=1)
	p.was_published_recently()
	# True
	```
- Choice Set 생성
	```python
	p.choice_set.create(choice='One', votes=0)
	# <Choice: One>
	p.choice_set.create(choice='Two', votes=0)
	# <Choice: Two>
	```