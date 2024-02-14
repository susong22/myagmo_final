# agmo_myfarm

농민을 위한 종합 자율주행 웹 서비스 농작이 

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## 개발환경

framework: Django

언어: Python

OS: Windows

DB: PostgreSQL

## 앱 구조

프로그램 구조도는 [여기](./농작이_프로그램구조도.pdf)에서 확인해주세요!

### 시작하기

장고 가상환경에서 실행할 수 있습니다

## 장고 가상환경 실행

1. 파이썬 설치
2. 장고 설치
  
$ python -m pip install Django
3. 데이터베이스 연결
- postgrsql 다운로드
     https://www.postgresql.org/
- SQL Shell 실행
     이곳에서 데이터베이스 편집 가능
- 데이터베이스 생성, 이름 지정
     https://sujinisacat.tistory.com/5
     기본 데이터베이스 이름은 postgres입니다! pgAdmin이라는 툴로도 편집 가능합니다(별도 설치 필요)
4. config/settings/base.py에서 데이터베이스 입력

DATABASES = {
  "default": env.db(
    "DATABASE_URL",
    default="postgres://postgres:[username]@localhost:5432/[데이터베이스이름]",
    ),
  }
ㄴ default의 username, 데이터베이스 이름을 편집해주시면 됩니다. 5432는 기본 포트이기 때문에 설치 시 default로 설정됩니다.
5. 터미널에서 가상환경 실행
     







