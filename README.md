# TelegramCryptoCompare
A. cryptocompare.com에서 제공하는 http request api를 이용해 매분마다 비트코인의 가격을 요청
B. 텔레그램 챗봇으로 메세지 전송
C. 텔레그램 챗봇에서 명령을 받음

Part A. 비트코인의 가격은 Bitfinex에서 USD로 표시 (upbit에서 KRW도 가능)
https://upbit.com/service_center/open_api_guide
http://docs.python-requests.org/en/master/user/quickstart

매 분마다 리퀘스트를 보내기 위해 AP스케쥴러, crontab, threading timer 사용\n
모인 정보들은 .csv 파일로 저장

Part B. 텔레그램 챗봇을 이용해 메세지를 보냄 매 분마다 가격 등락 알림을 보내는 챗봇을 만들기
https://core.telegram.org/bots
http://telepot.readthedocs.io/en/latest/

Part C. "/stop" 명령어를 만들어서 메세지 수신을 중단할 수 있어야 한다.
