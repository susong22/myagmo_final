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

📦 myagmo			# (1) repository_root

└─ my_project			# (2) project_root

   ├─ agmo_myfarm	# (3) configuration_root
   
   │  ├─ users                      #사용자 정보
   
   │   │  ├─ init.py
   
   │   │  ├─ admin.py
   
   
   │   │  ├─ apps.py
   
   │   │  ├─ forms.py
   
   │   │  ├─ models.py           #databse
   
   │   │  ├─ urls.py
   
   |   |  └─ views.py
   
   │  ├─ farm                      #경작지 정보
   
   │   │  ├─ init.py
   
   │   │  ├─ admin.py
   
   │   │  ├─ apps.py
   
   │   │  ├─ forms.py
   
   │   │  ├─ models.py
   
   │   │  ├─ urls.py
   
   |   |  └─ views.py
   
   │  ├─ work                      #작업 관리
   
   │   │  ├─ init.py
   
   │   │  ├─ admin.py
   
   │   │  ├─ apps.py
   
   │   │  ├─ forms.py
   
   │   │  ├─ models.py
   
   │   │  ├─ urls.py
   
   |   |  └─ views.py
   
   │  ├─ workdiary                #작업일지 관리
   
   │   │  ├─ init.py
   
   │   │  ├─ admin.py
   
   │   │  ├─ apps.py
   
   │   │  ├─ forms.py
   
   │   │  ├─ models.py
   
   │   │  ├─ urls.py
   
   |   |  └─ views.py
   
   │  ├─ home                      #홈 화면
   
   │   │  ├─ init.py
   
   
   │   │  ├─ admin.py
   
   
   │   │  ├─ apps.py
   
   │   │  ├─ path.py
   
   │   │  ├─ models.py
   
   │   │  ├─ urls.py
   
   |   |  └─ views.py
   
   │  └─ summary
   
   |   |  └─ init.py
   
   └─ config                      #설정파일 관리
   
   │   │  ├─ init.py
   
   │   |   │  ├─ base.py
   
   |   |   |  └─ urls.py
   
   │   │  ├─ init.py
   
   |   |  └─ urls.py
   
   └─ manage.py



[프로그램 구조도 파일도 첨부합니다](./농작이_프로그램구조도.pdf)







