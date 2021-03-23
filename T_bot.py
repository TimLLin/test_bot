import telebot
import main
from telebot import types

bot = telebot.TeleBot(main.token)

@bot.message_handler(commands=['start'])
def handle_command(message):
    markup_inline = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text = 'Расписание',callback_data = 'schedule')
    bt_2 = types.InlineKeyboardButton(text = 'Кафедры',callback_data = 'cafedrs')
    bt_3 = types.InlineKeyboardButton(text = 'Помощь',callback_data = 'help')
    markup_inline.add(bt_1,bt_2,bt_3)
    bot.send_message(message.chat.id, "Привет, что интересует?", reply_markup = markup_inline)

@bot.callback_query_handler(lambda a:True)
def start_answer(a):
    if a.data == 'schedule':
        markup_reply = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='110-БД', callback_data='110-БД')
        bt_2 = types.InlineKeyboardButton(text='110-БМ-1', callback_data='110-БМ-1')
        bt_3 = types.InlineKeyboardButton(text='110-БМ-2', callback_data='110-БМ-2')
        bt_4 = types.InlineKeyboardButton(text='110-БУ', callback_data='110-БУ')
        bt_5 = types.InlineKeyboardButton(text='120-БД', callback_data='120-БД')
        bt_6 = types.InlineKeyboardButton(text='120-БИ', callback_data='120-БИ')
        bt_7 = types.InlineKeyboardButton(text='120-БУ', callback_data='120-БУ')
        bt_8 = types.InlineKeyboardButton(text='120-БМО', callback_data='120-БМО')
        bt_9 = types.InlineKeyboardButton(text='120-БМФ', callback_data='120-БМФ')
        bt_10 = types.InlineKeyboardButton(text='130-БД', callback_data='130-БД')
        bt_11 = types.InlineKeyboardButton(text='130-БМ', callback_data='130-БМ')
        bt_12 = types.InlineKeyboardButton(text='130-БУ', callback_data='130-БУ')
        bt_13 = types.InlineKeyboardButton(text='140-БД', callback_data='140-БД')
        bt_14 = types.InlineKeyboardButton(text='140-БМ', callback_data='140-БМ')
        bt_15 = types.InlineKeyboardButton(text='140-БУ', callback_data='120-БУ')
        bt_16 = types.InlineKeyboardButton(text='140-ЭБ', callback_data='140-ЭБ')
        bt_17 = types.InlineKeyboardButton(text='Назад', callback_data='back')
        markup_reply.add(bt_1, bt_2, bt_3,bt_4,bt_5,bt_6,bt_7,bt_8,bt_9,bt_10,bt_11,bt_12,bt_13,bt_14,bt_15,bt_16,bt_17)
        bot.send_message(a.message.chat.id, "Выбирай", reply_markup=markup_reply)

    elif a.data == 'cafedrs':
        bot.send_message(a.message.chat.id, 'В нашем вузе имеются следующие кафедры:\n\n[Бухгалтерский учёт, аудит, статистика](http://www.fa.ru/fil/ufa/org/chair/buas/Pages/Home.aspx)\n\n[Математика и информатика](http://www.fa.ru/fil/ufa/org/chair/mi/Pages/Home.aspx)\n\n[Философия, история и право](http://www.fa.ru/fil/ufa/org/chair/fip/Pages/Home.aspx)\n\n[Финансы и кредит](http://www.fa.ru/fil/ufa/org/chair/fik/Pages/Home.aspx)\n\n[Экономика, менеджмент и маркетинг](http://www.fa.ru/fil/ufa/org/chair/emm/Pages/Home.aspx)', parse_mode='Markdown',disable_web_page_preview='true')
    elif a.data == 'help':
        bot.send_message(a.message.chat.id, "*Контакты Уфимского Филиала Финуниверситета:*\n\nТелефон: (347) 251-08-23\n\ne-mail: ufa@fa.ru\n\nАдрес: 450015, г. Уфа, ул. Мустая Карима 69/1", parse_mode='Markdown')
    elif a.data == 'back':
        return handle_command(a.message)

    elif a.data in list(main.data):
        bot.send_message(a.message.chat.id, main.data[a.data],disable_web_page_preview="false")
        markup_reply2 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        bt_2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        markup_reply2.add(bt_1,bt_2)
        bot.send_message(a.message.chat.id,"Могу ли я вам еще чем-нибудь помочь?", reply_markup=markup_reply2)

    elif a.data == 'yes':
        return handle_command(a.message)
    elif a.data == "no":
        bot.send_message(a.message.chat.id, "Спасибо за кров мой повелитель")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() =='старт' or message.text.lower() =='привет' or message.text.lower() =="start":
        return handle_command(message)


bot.polling()
