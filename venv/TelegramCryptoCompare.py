from apscheduler.schedulers.background import BackgroundScheduler
import cryptocompare
import telegram
import time
import pandas as pd
from telegram.ext import Updater, CommandHandler

ID = 123456789
TOKEN = '1234567890:ABCDEF1234567890ABCDEF1234567890ABC'
dataFrame = []  # dataframe
bot = telegram.Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher # 디스패처 생성
scheduler = BackgroundScheduler(timezone='Asia/Seoul')  # 스케줄러 생성


def start(update, context):
    scheduler.start()


def check(dataframe):
    price = format(int(cryptocompare.get_price('BTC', currency='KRW')['BTC']['KRW']), ',')
    curr = time.strftime('%y-%m-%d %H:%M')
    dataframe.append([curr, price])
    text = '({}) KRW-BTC price: {}'.format(curr, price)
    bot.send_message(chat_id=ID, text=text)
    return dataframe


def stop(update, context):
    context.bot.send_message(chat_id=ID, text='Bye')
    scheduler.shutdown()  # 스케줄러 종료
    updater.dispatcher.stop()  # 디스패처 종료


scheduler.add_job(check, 'interval', seconds=60, args=[dataFrame], id='check')  # 60초에 한번씩 check 함수에 dataFrame을 인자로 전달
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()

while True:
    time.sleep(1)
    if scheduler.get_job('check') is None:  # 스케줄러에 check 함수가 없으면
        break  # while문 종료

df = pd.DataFrame(dataFrame, columns=['time', 'price'])
df.to_csv('./BTC.csv', index=False)
