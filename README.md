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
- 해당 폴더로 이동
  
     py -m venv agmo_myfarm

     agmo_myfarm\Scripts\activate.bat
  
- manage.py가 있는 폴더로 이동, runserver

  py manage.py runserver


## 화면 소개

1. login
   
   ![KakaoTalk_Photo_2024-02-14-19-12-21 001](https://github.com/susong22/myagmo/assets/65169271/467c4136-f00b-49aa-9858-bf00e10fe7fb)

   가능한 작업: login 성공 시 home으로 이동, login 실패 시 해당 페이지에 머무름
   추가할 작업: 성공 및 실패에 따른 팝업 알림

2. signup
   
   ![KakaoTalk_Photo_2024-02-14-19-12-21 002](https://github.com/susong22/myagmo/assets/65169271/72389b67-b7ac-4668-95d4-744deb18c6e6)

   가능한 작업: 회원가입
   추가할 작업: area 선택지 확대

3. Home

   
   ![Home-ezgif com-video-to-gif-converter](https://github.com/susong22/myagmo/assets/65169271/33c34c75-9af5-44d2-8ec8-768a85d0c417)

   가능한 작업: 주행경로 및 예상경로 출력, (버튼누르면) 주행 시작 (실제로 트랙터의 주행현황을 받아올 수 없기 때문에, 최대한 비슷하게 구현했습니다)
   개선 사항: 현재 xlsx 파일에서 정보를 읽어 경위도 좌표로 변환하고 구글맵에 보내는 식으로 작업 중인데, 파일의 크기가 너무 크다보니(10만행) 로딩이 매우 느립니다(2분정도)ㅜㅜ 미리 downsampling을 해서 로딩시간을 줄이는 방향으로 생각하고 있습니다!

4. 경작지 추가

   
   ![KakaoTalk_Photo_2024-02-14-19-12-21 003](https://github.com/susong22/myagmo/assets/65169271/8606cac1-26fd-40e6-a857-981fc992f6fd)
   ![KakaoTalk_Photo_2024-02-14-19-12-21 004](https://github.com/susong22/myagmo/assets/65169271/38662e8e-b4f7-4044-897e-6ec720d866ed)

   가능한 작업: 경작지 이름 설정, 마커로 경작지 경계 설정, 상세 메모
   추가할 작업: 마커로 경계 설정 시 polyline 형성, 위치 데이터베이스 업로드
   오류 사항: 현재 위치 검색이 잘 되고 있지 않습니다ㅜㅜ

5. 작업관리 및 추가

    
   ![KakaoTalk_Photo_2024-02-14-19-12-21 006](https://github.com/susong22/myagmo/assets/65169271/d463930e-305a-40e2-9464-3499a40cda47)
   ![KakaoTalk_Photo_2024-02-14-19-12-22 007](https://github.com/susong22/myagmo/assets/65169271/63d685fa-187d-4d66-b0a2-865f9cc1b26d)
   ![KakaoTalk_Photo_2024-02-14-19-12-22 008](https://github.com/susong22/myagmo/assets/65169271/f4277320-bcb1-4293-a346-dc6c3852a6c2)

   가능한 작업: 오늘 날씨 출력, 작업 추가
   추가할 작업: start point/end point가 아닌 시작점+방향으로 작업경로 설정, 추천 경로 다양화

6. 작업일지

    
   ![KakaoTalk_Photo_2024-02-14-19-12-22 009](https://github.com/susong22/myagmo/assets/65169271/f8eec6a6-c279-4106-baf1-301e723ffb5d)

  가능한 작업: 날짜 선택 시 오늘 작업 보여주기
  추가할 작업: 밤 10시가 되면 자동으로 작업 저장, 작업 진행률 보여주기, 과거/미래 작업 보여주기
  

7. 요약

- 해당 부분은 아직 구현을 하지 못했습니다.
- 아래는 구현 예정인 내용입니다.


1. 농작이 솔루션
    
    → 작년에 나는 000을 했어요, 올해 계획은 000 추천해요
    
    → 다음주 날씨가 이래요, 작업을 서두르세요, 미세먼지 예상치
    
    → 더 알아보기: [농진청] ~~~(유튜브 제목)
    
    - 상세페이지
        
        → 05월
        
        2023년: xxx를 했어요
        
        올해는 000를 추천해요!
        
        → 2/20일 30mm 강수예정! 작업을 서두르세요
        
        2/23일 미세먼지 나쁨! 살충제를 준비하세요
        
        → 더 알아보기
        
        링크로 유튜브, 칼럼
        
2. 내 경작지 토양특성
    
    → 내 경작지는 <논>이고, pH가<높>으므로 ()비료를 추천합니다.
    
    - 상세페이지
        
        → (흙토람) 지역 토양 특성
        
        → pH
        
        → 비료 사용량
        
3. 경사도, 강우량, 지면높이를 이용한 토양 유실 위험
    
    → 토양 침식 <위험>입니다
    
    - 상세페이지
        
        → 강수량, 1일차, 2일차, 3일차 저장강수률, 토양수분, 물을 얼마나 주세요
        
        → 토양저장강수율 계산(알고리즘 구현)
        
        → 지면 기울기맵을 이용해 어느 부분이 침식 위험인지 맵으로(캡쳐)
        
4. 내 작물
    
    → 현재 그 작물의 시장가(**시세**), 풀린 물량
    
    - 상세페이지
        
        → 현재 <벼>는 <0000원>이고 시장에서 <000kg> 거래되고 있어요
        
        → https://www.kamis.or.kr/customer/main/main.do
        
        → <벼>의 평균 재배과정은 다음과 같아요 (농진청 링크)
        
5. 대리점 위치
    
    → 가까운 곳에 000 대리점이 있어요
    
    - 상세페이지
        
        → 얀마 대리점 위치 맵으로 (캡쳐)






