nodemon 은 global 설치되어 있어야 함.
확인하려면,
$ npm list -g
확인 후, package.json 이 포함된 현재 프로젝트 디렉토리에서 다음을 실행
$ npm i
$ nodemon server.js

==================================================

2022 07 21
현재 받아올 FE 정보가 없어서 PostMan을 통해 body 전송,
수정할 DB 정보가 없어서 MySQL Workbench를 임의로 생성하여 실험 가동 중

생성한 DB : store, 생성한 Table : market


## DB 사용자 : root
## DB 이름 : sulgorae
## DB 테이블 정보
번호 | DB 명 | DB 이름 | 내용
--|--|--|--
1 | Liquor |주류 DB |  주류에 대한 정보를 저장 <br> 개발자가 내용을 관리
2 | Inventory | 재고 DB | 매장에 있는 주류에 대한 정보를 저장 <br>매장 관리자가 내용을 관리
3 | Member | 회원 정보 DB |웹페이지를 사용하는 매장 관리자의 정보를 저장
4 | Request | 요청 DB | 매장관리자들이 개발자에게 요청한 사항을 저장
5 | Survey | 취향 설문 내용 DB |키오스크에서 사용될 취향 설문 질문 및 답변 저장<br>키오스크에서 취향 설문 조사 요청시 내용을 보내줌
6 | Face | 얼굴 설문 DB | 키오스크에서 얼굴 감정분석 결과로 보여줄 내용을 저장<br> 키오스크에서 얼굴 감정분석 결과 요청시 보내줌


