import telebot
import main
from telebot import types
from datetime import datetime

bot = telebot.TeleBot(main.token)


@bot.message_handler(commands=['start'])
def handle_command(message):
    markup_inline = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text='Расписание', callback_data='schedule')
    bt_2 = types.InlineKeyboardButton(text='Кафедры', callback_data='cafedrs')
    bt_3 = types.InlineKeyboardButton(text='Помощь', callback_data='help')
    bt_4 = types.InlineKeyboardButton(text='Новости', callback_data='news')
    bt_5 = types.InlineKeyboardButton(text='Данные ЦБ', callback_data='cb')
    bt_6 = types.InlineKeyboardButton(text='Абитуриенту', callback_data='abi')
    markup_inline.add(bt_1, bt_2, bt_3, bt_4, bt_5)
    markup_inline.add(bt_6)
    bot.send_message(message.chat.id, 'Что тебе показать?', reply_markup=markup_inline)
    with open("Data.txt","a",encoding='utf-8',errors='ignore') as f:
        if message.from_user.username != 'FinUfa_bot':
            context = "{} {} {} {} {}\n".format(message.chat.id, message.from_user.username, message.chat.first_name, message.chat.last_name, message.text)
            f.write(context)
        else:
            context = "{} {} {} {} Message_by_bot\n".format(message.chat.id, message.from_user.username, message.chat.first_name, message.chat.last_name)
            f.write(context)

@bot.message_handler(commands=['mailing'])
def mailing(message):
    sent = bot.send_message(message.chat.id, 'Введите сообщение которое будет отправлено')
    bot.register_next_step_handler(sent, mail)



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
        bt_17 = types.InlineKeyboardButton(text='Назад', callback_data='yes')
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


    elif a.data in list(main.data):
        main.var = a.data
        markup_reply4 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='На неделю', callback_data='week')
        bt_2 = types.InlineKeyboardButton(text='На сегодня', callback_data='today')
        bt_3 = types.InlineKeyboardButton(text='На завтра', callback_data='tommorow')
        markup_reply4.add(bt_1,bt_2,bt_3)
        bot.send_message(a.message.chat.id, "Выбирай", reply_markup=markup_reply4)


    elif a.data == "week":
        schedule = main.download_data(main.var,main.data[main.var])
        try:
            week_schedule = main.w_schedule(main.var)
            for elem in week_schedule:
                try:
                    mes = main.list_edit(elem)
                    bot.send_message(a.message.chat.id, mes)
                except IndexError:
                    bot.send_message(a.message.chat.id, "-")
        except ValueError:
            bot.send_document(a.message.chat.id, schedule)


        markup_reply5 = types.InlineKeyboardMarkup()
        bt_3 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        markup_reply5.add(bt_3)
        bot.send_message(a.message.chat.id, "Вернуться в главное меню?", reply_markup=markup_reply5)

    elif a.data == "today":
        schedule = main.download_data(main.var, main.data[main.var])
        try:
            week_schedule = main.w_schedule(main.var)
            weekday = datetime.weekday(datetime.now())
            try:
                if weekday in [5,6]:
                    bot.send_message(a.message.chat.id, "Бип боп расписание обновляется.\nИспользуйте расписание на неделю.")
                else:
                    mes = main.list_edit(week_schedule[weekday])
                    bot.send_message(a.message.chat.id, mes)
            except IndexError:
                bot.send_message(a.message.chat.id,
                                 "Данных нет. \nИспользуйте расписание на неделю или обратитесь к старосте вашей группы.")
        except ValueError:
            bot.send_document(a.message.chat.id,schedule)
        markup_reply5 = types.InlineKeyboardMarkup()
        bt_3 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        markup_reply5.add(bt_3)
        bot.send_message(a.message.chat.id, "Вернуться в главное меню?", reply_markup=markup_reply5)

    elif a.data == "tommorow":
        schedule = main.download_data(main.var, main.data[main.var])
        try:
            week_schedule = main.w_schedule(main.var)
            weekday = datetime.weekday(datetime.now())+1
            try:
                if weekday in [5,6]:
                    bot.send_message(a.message.chat.id, "Бип боп расписание обновляется.\nИспользуйте расписание на неделю.")
                elif weekday ==7:
                    weekday = 0
                    mes = main.list_edit(week_schedule[weekday])
                    bot.send_message(a.message.chat.id, mes)
                else:
                    mes = main.list_edit(week_schedule[weekday])
                    bot.send_message(a.message.chat.id, mes)
            except IndexError:
                bot.send_message(a.message.chat.id,
                                 "Данных нет. \nИспользуйте расписание на неделю или обратитесь к старосте вашей группы.")
        except ValueError:
            bot.send_document(a.message.chat.id, schedule)

        markup_reply5 = types.InlineKeyboardMarkup()
        bt_3 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        markup_reply5.add(bt_3)
        bot.send_message(a.message.chat.id, "Вернуться в главное меню?", reply_markup=markup_reply5)

    elif a.data == 'yes':
        return handle_command(a.message)


    elif a.data == 'news':
        test = main.news()
        sus = "\t".join(test)
        bot.send_message(a.message.chat.id, "[Новости Филиала](http://www.fa.ru/fil/ufa/News/Forms/AllPages.aspx)",
                         parse_mode='Markdown', disable_web_page_preview='true')
        markup_reply7 = types.InlineKeyboardMarkup()
        bt_6 = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        markup_reply7.add(bt_6)
        bot.send_message(a.message.chat.id, sus, disable_web_page_preview='true', reply_markup=markup_reply7)

    elif a.data == 'cb':
        markup_reply8 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Курсы валют', callback_data='currency')
        bt_2 = types.InlineKeyboardButton(text='Ключевые показатели', callback_data='stake')
        bt_3 = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        markup_reply8.add(bt_1, bt_2)
        markup_reply8.add(bt_3)
        bot.send_message(a.message.chat.id, "Выбирай", reply_markup=markup_reply8)


    elif a.data == 'stake':
        markup_reply9 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        bot.send_message(a.message.chat.id, main.stake())
        markup_reply9.add(bt_1)
        bot.send_message(a.message.chat.id, "Вернуться в главное меню?", reply_markup=markup_reply9)

    elif a.data == 'currency':
        markup_reply10 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        bot.send_message(a.message.chat.id, main.currency())
        markup_reply10.add(bt_1)
        bot.send_message(a.message.chat.id, "Вернуться в главное меню?", reply_markup=markup_reply10)

    elif a.data == 'abi':
        markup_reply11 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Бакалавриат', callback_data='bak')
        bt_2 = types.InlineKeyboardButton(text='Магистратура', callback_data='mag')
        bt_3 = types.InlineKeyboardButton(text='CПО', callback_data='cpo')
        bt_4 = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        markup_reply11.add(bt_1, bt_2, bt_3, bt_4)
        bot.send_message(a.message.chat.id, "Могу быть ещё чем-то полезен?", reply_markup=markup_reply11)

    elif a.data == "bak":
        markup_reply12 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Направления', callback_data='b_nap')
        bt_2 = types.InlineKeyboardButton(text='Сроки', callback_data='b_deadline')
        bt_3 = types.InlineKeyboardButton(text='Вступительные экзамены', callback_data='exam_bak')
        bt_4 = types.InlineKeyboardButton(text='Мин. баллы', callback_data='prohod_bak')
        bt_5 = types.InlineKeyboardButton(text='Контрольные цифры приема', callback_data='kcp_bak')
        bt_6 = types.InlineKeyboardButton(text='Назад', callback_data='back_abi')
        markup_reply12.add(bt_1, bt_2,bt_4)
        markup_reply12.add(bt_3)
        markup_reply12.add(bt_5)
        markup_reply12.add(bt_6)
        bot.send_message(a.message.chat.id, "Могу быть ещё чем-то полезен?", reply_markup=markup_reply12)

    elif a.data == 'b_nap':
        bot.send_message(a.message.chat.id, '''В нашем университете имеются следующие направления подготовки бакалавров:
            38.03.01 Экономика 
            38.03.02 Менеджмент 
            38.03.05 Бизнес-информатика
            
Ознакомиться с программами обучения вы можете по [ссылке](http://www.fa.ru/fil/ufa/pk/bak/Pages/progs.aspx)''',
                         parse_mode="Markdown", disable_web_page_preview='true')

    elif a.data == 'b_deadline':
        bot.send_document(a.message.chat.id,open("Сроки приемной комиссии Бак.pdf",'rb'))

    elif a.data == 'exam_bak':
        bot.send_document(a.message.chat.id,open("Перечень вступительных испытаний БАК.pdf",'rb'))

    elif a.data == 'prohod_bak':
        bot.send_document(a.message.chat.id, open("Минимальные баллы приема_бак.pdf",'rb'))

    elif a.data == 'kcp_bak':
        bot.send_document(a.message.chat.id, open("Контрольные цифры приема_бак.pdf", 'rb'))


    elif a.data == 'back_abi':
        a.data = 'abi'
        return start_answer(a)

    elif a.data == 'mag':
        markup_reply13 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Направления', callback_data='m_nap')
        bt_2 = types.InlineKeyboardButton(text='Сроки', callback_data='m_deadline')
        bt_3 = types.InlineKeyboardButton(text='Вступительные экзамены', callback_data='exam_mag')
        bt_5 = types.InlineKeyboardButton(text='Контрольные цифры приема', callback_data='kcp_mag')
        bt_4 = types.InlineKeyboardButton(text='Назад', callback_data='back_abi')
        markup_reply13.add(bt_1, bt_2)
        markup_reply13.add(bt_3)
        markup_reply13.add(bt_5)
        markup_reply13.add(bt_4)
        bot.send_message(a.message.chat.id, "Могу быть ещё чем-то полезен?", reply_markup=markup_reply13)

    elif a.data == 'm_nap':
        markup_reply_mag = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Назад', callback_data='back_mag')
        markup_reply_mag.add(bt_1)
        bot.send_message(a.message.chat.id, '''В нашем университете имеются следующие направления подготовки магистров:
            38.04.01 Экономика 
            38.04.02 Менеджмент
            
Ознакомиться с программами обучения вы можете по [ссылке](http://www.fa.ru/fil/ufa/pk/mag/Pages/progs.aspx)''',
                         parse_mode="Markdown", disable_web_page_preview='true', reply_markup=markup_reply_mag)

    elif a.data == 'exam_mag':
        markup_reply_mag = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Назад', callback_data='back_mag')
        markup_reply_mag.add(bt_1)
        bot.send_document(a.message.chat.id, open("Перечень вступительных испытаний_магистратура.pdf", 'rb'), reply_markup=markup_reply_mag)

    elif a.data == 'm_deadline':
        markup_reply_mag = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Назад', callback_data='back_mag')
        markup_reply_mag.add(bt_1)
        bot.send_document(a.message.chat.id, open("Сроки приемной кампании_магистратура.pdf", 'rb'), reply_markup=markup_reply_mag)

    elif a.data == 'kcp_mag':
        bot.send_document(a.message.chat.id, open("Контрольные цифры приема_магистратура.pdf", 'rb'))

    elif a.data == 'back_mag':
        a.data = 'mag'
        return start_answer(a)

    elif a.data == 'cpo':
        markup_reply14 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Специальности', callback_data='spec_spo')
        bt_2 = types.InlineKeyboardButton(text='Сроки', callback_data='spo_deadline')
        bt_3 = types.InlineKeyboardButton(text='Контрольные цифры приема', callback_data='spo_kcp')
        bt_4 = types.InlineKeyboardButton(text='Назад', callback_data='back_abi')
        markup_reply14.add(bt_1, bt_2)
        markup_reply14.add(bt_3)
        markup_reply14.add(bt_4)
        bot.send_message(a.message.chat.id, "Могу быть ещё чем-то полезен?", reply_markup=markup_reply14)

    elif a.data == 'spec_spo':
        markup_reply_cpo = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Назад', callback_data='back_spo')
        markup_reply_cpo.add(bt_1)
        bot.send_message(a.message.chat.id, '''В нашем университете имеются следующие направления подготовки специалистов:
                    38.02.07 Банковское дело
                    38.02.06 Финансы
                    38.02.01 Экономика и бухгалтерский учет  (по отраслям)
                    38.02.02 Страховое дело  (по отраслям)
                    09.02.05 Прикладная информатика (по отраслям)
                    40.02.01 Право и организация социального обеспечения

Ознакомиться с программами обучения вы можете по [ссылке](http://www.fa.ru/fil/ufa/pk/spo/Pages/specs.aspx)''',
                         parse_mode="Markdown", disable_web_page_preview='true', reply_markup = markup_reply_cpo)

    elif a.data == "spo_deadline":
        markup_reply_cpo = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Назад', callback_data='back_spo')
        markup_reply_cpo.add(bt_1)
        bot.send_document(a.message.chat.id, open("Сроки приемной кампании 2021 года_СПО.pdf", 'rb'),reply_markup=markup_reply_cpo)

    elif a.data == "spo_kcp":
        markup_reply_cpo = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Назад', callback_data='back_spo')
        markup_reply_cpo.add(bt_1)
        bot.send_document(a.message.chat.id, open("Контрольные цифры приема_СПО.PDF", 'rb'),reply_markup=markup_reply_cpo)

    elif a.data == "back_spo":
        a.data = 'cpo'
        return start_answer(a)








        


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'старт' or message.text.lower() == 'привет' or message.text.lower() == "start":
        return handle_command(message)
    elif message.text.lower()== "housekeepers":
        try:
            bot.send_message(message.chat.id,main.users())
            f = open("Data.txt", "rb")
            bot.send_document(message.chat.id, f)
        except UnicodeDecodeError:
            bot.send_message(message.chat.id,":(((")
    elif message.text.lower() == "house of spam":
        try:
            f = open("Data_mailing.txt", 'r')
            bot.send_document(message.chat.id, f)
        except:
            bot.send_message(message.chat.id, "Error code: 400. Description: Bad Request: file must be non-empty :(((")
    with open("Data.txt","a",encoding='utf-8',errors='ignore') as f:
        context = "{} {} {} {} {}\n".format(message.chat.id, message.from_user.username, message.chat.first_name, message.chat.last_name, message.text)
        f.write(context)



def mail(message):
    in_text = message.text
    sum = 0
    file_mailing = open("Data_mailing.txt", 'w', encoding="utf-8", errors='ignore')
    for elem in main.mailing():
        info = "{} 🔄".format(elem)
        file_mailing.write(info)
        try:
            bot.send_message(elem, in_text)
            status = "✅ \n"
            file_mailing.write(status)
            sum += 1

        except:
            status = "❌ \n"
            file_mailing.write(status)
    file_mailing.close()
    message_for_user = "Message :\n\n{}\n\n received  {} users.".format(in_text, sum)
    bot.send_message(message.chat.id, message_for_user)

    with open("Data_mailing.txt", 'rb') as f:
        bot.send_document(message.chat.id, f)

   

bot.polling()
