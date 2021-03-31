import telebot
import main
from telebot import types

bot = telebot.TeleBot('1782052770:AAEuTYmwFszzA97utccxH4ZXoKfXeXf3TXI')


@bot.message_handler(commands=['start'])
def handle_command(message):
    markup_inline = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text='Расписание', callback_data='schedule')
    bt_2 = types.InlineKeyboardButton(text='Кафедры', callback_data='cafedrs')
    bt_3 = types.InlineKeyboardButton(text='Помощь', callback_data='help')
    bt_4 = types.InlineKeyboardButton(text='Новости', callback_data='news')
    bt_5 = types.InlineKeyboardButton(text='Курсы валют ЦБ', callback_data='currency')
    bt_6 = types.InlineKeyboardButton(text='Ключевая ставка', callback_data='stake')
    markup_inline.add(bt_1, bt_2, bt_3,bt_4,bt_5, bt_6)
    bot.send_message(message.chat.id, 'Что тебе показать?', reply_markup=markup_inline)


@bot.callback_query_handler(lambda a: True)
def start_answer(a):
    if a.data == 'schedule':
        markup_reply = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='110-БД', callback_data='110-БД.docx')
        bt_2 = types.InlineKeyboardButton(text='110-БМ-1', callback_data='110-БМ-1.docx')
        bt_3 = types.InlineKeyboardButton(text='110-БМ-2', callback_data='110-БМ-2.docx')
        bt_4 = types.InlineKeyboardButton(text='110-БУ', callback_data='110-БУ.docx')
        bt_5 = types.InlineKeyboardButton(text='120-БД', callback_data='120-БД.docx')
        bt_6 = types.InlineKeyboardButton(text='120-БИ', callback_data='120-БИ.docx')
        bt_7 = types.InlineKeyboardButton(text='120-БУ', callback_data='120-БУ.docx')
        bt_8 = types.InlineKeyboardButton(text='120-БМО', callback_data='120-БМО.docx')
        bt_9 = types.InlineKeyboardButton(text='120-БМФ', callback_data='120-БМФ.docx')
        bt_10 = types.InlineKeyboardButton(text='130-БД', callback_data='130-БД.docx')
        bt_11 = types.InlineKeyboardButton(text='130-БМ', callback_data='130-БМ.docx')
        bt_12 = types.InlineKeyboardButton(text='130-БУ', callback_data='130-БУ.docx')
        bt_13 = types.InlineKeyboardButton(text='140-БД', callback_data='140-БД.docx')
        bt_14 = types.InlineKeyboardButton(text='140-БМ', callback_data='140-БМ.docx')
        bt_15 = types.InlineKeyboardButton(text='140-БУ', callback_data='140-БУ.docx')
        bt_16 = types.InlineKeyboardButton(text='140-ЭБ', callback_data='140-ЭБ.docx')
        bt_17 = types.InlineKeyboardButton(text='Назад', callback_data='back')
        bt_18 = types.InlineKeyboardButton(text='тест', callback_data='test')
        markup_reply.add(bt_1, bt_2, bt_3, bt_4, bt_5, bt_6, bt_7, bt_8, bt_9, bt_10, bt_11, bt_12, bt_17)
        bot.send_message(a.message.chat.id, "Выбирай", reply_markup=markup_reply)

    elif a.data == 'cafedrs':
        markup_reply2 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        markup_reply2.add(bt_1)
        bot.send_message(a.message.chat.id,
                         'В нашем вузе имеются следующие кафедры:\n\n[Бухгалтерский учёт, аудит, статистика](http://www.fa.ru/fil/ufa/org/chair/buas/Pages/Home.aspx)\n\n[Математика и информатика](http://www.fa.ru/fil/ufa/org/chair/mi/Pages/Home.aspx)\n\n[Философия, история и право](http://www.fa.ru/fil/ufa/org/chair/fip/Pages/Home.aspx)\n\n[Финансы и кредит](http://www.fa.ru/fil/ufa/org/chair/fik/Pages/Home.aspx)\n\n[Экономика, менеджмент и маркетинг](http://www.fa.ru/fil/ufa/org/chair/emm/Pages/Home.aspx)',
                         parse_mode='Markdown', disable_web_page_preview='true', reply_markup=markup_reply2)

    elif a.data == 'help':
        markup_reply3 = types.InlineKeyboardMarkup()
        bt_2 = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        markup_reply3.add(bt_2)
        bot.send_message(a.message.chat.id,
                         "*Контакты Уфимского Филиала Финуниверситета:*\n\nТелефон: (347) 251-08-23\n\ne-mail: ufa@fa.ru\n\nАдрес: 450015, г. Уфа, ул. Мустая Карима 69/1",
                         parse_mode='Markdown', reply_markup=markup_reply3)

    elif a.data == 'back':
        return handle_command(a.message)

    elif a.data in list(main.data):
        schedule = main.download_data(a.data,main.data[a.data])
        try:
            week_schedule = main.w_schedule(a.data)
            for elem in week_schedule:
                del1 = elem[0]
                del2 = elem[1]
                date = elem[1] + '\t' + elem[0] + '\n'
                for i in range(len(elem)):
                    if (len(elem[i])==3 and elem[i]!="РБС") or (elem[i]=='спорт' and elem[i-1]!="и"):
                        elem.insert(i+1,'\n\n')
                    if elem[i]==del1 or elem[i]==del2:
                        elem[i] = str()
                sub = ' '.join(elem)
                mes = date + '\t\n\t' + sub
                bot.send_message(a.message.chat.id, mes)
        except ValueError:
            bot.send_document(a.message.chat.id,schedule)
        markup_reply4 = types.InlineKeyboardMarkup()
        bt_3 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        bt_4 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        markup_reply4.add(bt_3, bt_4)
        bot.send_message(a.message.chat.id, "Могу быть ещё чем-то полезен?", reply_markup=markup_reply4)

    elif a.data == 'yes':
        return handle_command(a.message)
    elif a.data == "no":
        markup_reply5 = types.InlineKeyboardMarkup()
        bt_5 = types.InlineKeyboardButton(text='Тык', callback_data='yes')
        markup_reply5.add(bt_5)
        bot.send_message(a.message.chat.id, "Как только понадоблюсь - тыкни!", reply_markup=markup_reply5)

    elif a.data == 'news':
        test = main.news()
        sus = "\t".join(test)
        bot.send_message(a.message.chat.id, "[Новости Филиала](http://www.fa.ru/fil/ufa/News/Forms/AllPages.aspx)",
                         parse_mode='Markdown', disable_web_page_preview='true')
        markup_reply6 = types.InlineKeyboardMarkup()
        bt_6 = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        markup_reply6.add(bt_6)
        bot.send_message(a.message.chat.id, sus, disable_web_page_preview='true', reply_markup=markup_reply6)
    
    elif a.data =='currency':
        test = main.currency()
        sus ="\t". join(test)
        bot.send_message(a.message.chat.id, sus, disable_web_page_preview='true')
    
    elif a.data =='stake':
        test = main.stake()
        sus = "\t". join(test)
        bot.send_message(a.message.chat.id, sus, disable_web_page_preview='true')





@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'старт' or message.text.lower() == 'привет' or message.text.lower() == "start":
        return handle_command(message)

bot.polling()