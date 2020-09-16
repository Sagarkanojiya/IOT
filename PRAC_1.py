Code:1
import telepot
token = ' 1383450593:AAGnS_SbZbQdgeJCA_dAu7FnSpgmxdxYgo4'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())


Code:2
import telepot
token = '  1383450593:AAGnS_SbZbQdgeJCA_dAu7FnSpgmxdxYgo4'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

TelegramBot.message_loop(handle)


1.https://api.telegram.org/bot1383450593:AAGnS_SbZbQdgeJCA_dAu7FnSpgmxdxYgo4/sendMessage?chat_id=1336458104&text=TestReply 

2.Getme: https://api.telegram.org/bot1383450593:AAGnS_SbZbQdgeJCA_dAu7FnSpgmxdxYgo4/getMe

3.getupdates
https://api.telegram.org/bot1383450593:AAGnS_SbZbQdgeJCA_dAu7FnSpgmxdxYgo4/getUpdates
