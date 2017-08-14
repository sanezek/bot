import sys
import time
import telepot
import os
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton




def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type!='text':
        print(content_type, chat_type, chat_id)

    if content_type=='text':
        print(content_type, chat_type, chat_id,'"',msg['text'],'"')
        if msg['text']=='/help':
            bot.sendMessage(chat_id,"Список команд: \nКоманд нет")
        elif msg['text']=='/but':
            content_type, chat_type, chat_id = telepot.glance(msg)

            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                           [InlineKeyboardButton(text='Press me', callback_data='press')],
                       ])

            bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
        else:
            bot.sendMessage(chat_id,msg['text'])

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')

TOKEN = '435160768:AAHR0gVgmrXlhkCV1NDZvftj_EBRSd8P-uU'  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')


while 1:
    time.sleep(10)