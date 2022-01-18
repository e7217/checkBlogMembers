# 네이버 블로그 좋아요 유저 검증 프로그램
## 목적
특정 그룹이 네이버 블로그 게시물에 '좋아요'를 눌렀는지 검증
## 사용방법
1. targetList.xlsx의 서식에 맞추어 post 주소와 검증대상 그룹을 입력한다.
2. main.exe를 실행시킨다. (pyinstaller로 .exe 파일 생성)
3. results.xlsx가 생성되며 이 파일을 열어 결과를 확인한다.
    + 이미 파일이 있는 경우 덮어쓰기 수행됨
#### .exe 파일 생성
```
pyinstaller --onefile main.py
```
## 추후 보완사항
+ 성능 최적화
+ pull 과정에서 소스 충돌 발생
+ post 관련 항목은 requests 모듈만으로는 처리 불가
