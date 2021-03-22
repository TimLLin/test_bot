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
        bt_1 = types.InlineKeyboardButton(text='На неделю', callback_data='weekly')
        bt_2 = types.InlineKeyboardButton(text='На день', callback_data='day')
        bt_3 = types.InlineKeyboardButton(text='Назад', callback_data='back')
        markup_reply.add(bt_1, bt_2, bt_3)
        bot.send_message(a.message.chat.id, "Выбирай", reply_markup=markup_reply)
    elif a.data == 'cafedrs':
        bot.send_message(a.message.chat.id, 'В нашем вузе имеются следующие кафедры:\n\n[Бухгалтерский учёт, аудит, статистика](http://www.fa.ru/fil/ufa/org/chair/buas/Pages/Home.aspx)\n\n[Математика и информатика](http://www.fa.ru/fil/ufa/org/chair/mi/Pages/Home.aspx)\n\n[Философия, история и право](http://www.fa.ru/fil/ufa/org/chair/fip/Pages/Home.aspx)\n\n[Финансы и кредит](http://www.fa.ru/fil/ufa/org/chair/fik/Pages/Home.aspx)\n\n[Экономика, менеджмент и маркетинг](http://www.fa.ru/fil/ufa/org/chair/emm/Pages/Home.aspx)', parse_mode='Markdown')
    elif a.data == 'help':
        bot.send_message(a.message.chat.id, "*Контакты Уфимского Филиала Финуниверситета:*\n\nТелефон: (347) 251-08-23\n\ne-mail: ufa@fa.ru\n\nАдрес: 450015, г. Уфа, ул. Мустая Карима 69/1", parse_mode='Markdown')

    elif a.data == 'back':
        return handle_command(a.message)

    elif a.data == 'weekly':
        poop = main.schedule("130_BD.txt")
        bot.send_message(a.message.chat.id,poop[:])
    elif a.data == 'day':
        bot.send_message(a.message.chat.id, "Представь что здесь ваше расписание")

bot.polling()
