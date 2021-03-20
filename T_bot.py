import telebot
import main
from telebot import types

bot = telebot.TeleBot(main.token)

@bot.message_handler(commands=['start'])
def handle_command(message):
    markup_inline = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text = 'Расписание',callback_data = 'schedule')
    bt_2 = types.InlineKeyboardButton(text = 'Помощь',callback_data = 'help')
    markup_inline.add(bt_1,bt_2)
    bot.send_message(message.chat.id, "Hello", reply_markup = markup_inline)

@bot.callback_query_handler(lambda a:True)
def start_answer(a):
    if a.data == 'schedule':
        markup_reply = types.InlineKeyboardMarkup()
        bt_3 = types.InlineKeyboardButton(text='На неделю', callback_data='weekly')
        bt_4 = types.InlineKeyboardButton(text='На день', callback_data='day')
        bt_5 = types.InlineKeyboardButton(text='Назад', callback_data='back')
        markup_reply.add(bt_3, bt_4, bt_5)
        bot.send_message(a.message.chat.id, "Choose", reply_markup=markup_reply)
        @bot.callback_query_handler(lambda b: True)
        def start_answer2(b):
            if b.data == 'weekly':
                pass
            elif b.data == 'day':
                pass
    elif a.data == 'help':
        pass
    elif a.data == 'back':
        return handle_command(a.message)


bot.polling()
