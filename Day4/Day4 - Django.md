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