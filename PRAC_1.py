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



