# Grammarly_Crawl

## Introduce
**Grammarly는 영어문법교정사이트입니다. 본 크롤러는 Selenium기반 Grammarly 자동화 테스트 기능을 제공합니다.**

## Install
- python3 버젼을 사용해주세요.
- Chrome Driver를 설치해주세요. 크롬 버젼에 맞는,OS에 맞는 드라이버를 <br>
http://chromedriver.chromium.org/ <br>
- pip install selenuim <br>
or
- pip install -r requirements.txt<br>

## How to use
- 본인의 Grammaly ID와 비밀번호를 입력해주세요.<br>
ID="YOUR_ID"
PW="YOUR_PW"

- 크롬드라이버를 OS에 맞게 설치한 후 경로를 입력해주세요.<br>
driver_path = r'/home/chanjun/Desktop/Grammarly_Crawl/chromedriver'

- test.txt 파일을 준비해주세요. 테스트할 예문을 작성해주세요.

## Result
- result.txt에 test.txt에 대한 교정결과가 생성됩니다.
