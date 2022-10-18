# TelegramCryptoCompare
A. cryptocompare.com에서 제공하는 http request api를 이용해 매분마다 비트코인의 가격을 요청

B. 텔레그램 챗봇으로 메세지 전송

C. 텔레그램 챗봇에서 명령을 받음

Part A. 비트코인의 가격은 KRW로 표기, 매 분마다 리퀘스트를 보내기 위해 AP스케쥴러 사용, 모인 정보들은 BTC.csv 파일로 저장

Part B. 텔레그램 챗봇을 이용해 매 분마다 가격 등락 알림

Part C. "/stop" 명령어를 만들어서 메세지 수신을 중단
