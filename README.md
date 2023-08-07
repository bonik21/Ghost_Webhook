# 스크립트 설명
고스트의 Webhook을 이용한 어플입니다.
고스트에서 새글이 발행되거나 기존 글이 업데이트 되었을 때, 텔레그램 및 디스코드로 알립니다.

# 파이썬 모듈 설치
```
pip install -r requirements.txt
```

# 최초 Ghost_Webhook.ini 파일 작성
- Ghost_Webhook-example.ini 복사 후 Ghost_Webhook.ini로 파일명 변경

# 스크립트가 실행되는 서버의 IP와 포트 확인
- ini파일에서 IP_AUTO_DETECT(아이피 자동 탐색 기능) 사용여부 작성 (Y or N)
- 기본 포트는 5000번(ini파일에서 변경가능)
- 외부 아이피나 특수한 네트워크 일 경우 ini파일의 IP_AUTO_DETECT값을 N으로 적고, 아이피 직접 입력 (e.g: 123.123.123.123)

# 텔레그램 및 디스코드 설정
- 텔레그램 토큰 및 챗아이디 생성(인터넷 검색) 및 메모
- 디스코드 WEBHOOKURL 생성(인터넷 검색) 및 메모

# Ghost_Webhook.ini 파일에 텔레그램 디스코드 정보 입력
- 텔레그램, 디스코드 기능 사용여부 작성 (Y 또는 N)
- 디스코드 유저명과 아바타 이미지는 원하는 대로 작성

# 고스트 웹훅 설정
## 웹훅 설정으로 이동
- 고스트 관리자 - Integrations - CUSTOM INTEGRATIONS - Configure
## 웹훅 설정
- 새 글 알림만 이용하고 싶으면 Post Published만 설정하면 됩니다.
### Post Published
- 새 글 발행시 발동되는 웹훅
- Event : Post published 선택
- Target URL : 본인의 스크립트 실행 서버 IP를 사용해서 `http://123.123.123.123:5000/post_published`와 같은 형태로 입력
### Post Updated
- 글 업데이트시 발동되는 웹훅
- Event : Post updated 선택
- Target URL : 본인의 스크립트 실행 서버 IP를 사용해서 `http://123.123.123.123:5000/post_updated`와 같은 형태로 입력
