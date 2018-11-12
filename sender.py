# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import db


def send_post(chat_id):
    FROM = 'archieruin@gmail.com'
    TO = 'seg4wq@gmail.com'
    username = 'archieruin@gmail.com'
    password = 'ktjxvzodnstgotkf'
    server = smtplib.SMTP('smtp.gmail.com:587')

    id = db.get_cache(chat_id)
    sum = db.get_reg_order_by_id(chat_id, id)[0][3]
    desc = db.get_reg_order_by_id(chat_id, id)[0][2].replace(';', '\n\n')
    phone_number = db.get_reg_order_by_id(chat_id, id)[0][4]

    if int(db.get_reg_order_by_id(chat_id, id)[0][6]) == 1:
        delivery = 'Нет'
    else:
        delivery = 'Да'

    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = "НОВЫЙ ЗАКАЗ!!!"

    body = 'Сумма заказа: {} руб.\n\n' \
           'Номер телефона: {}\n\n' \
           'Доставка: {}\n\n' \
           'Товар:\n' \
           '{}\n\n' \
           ''.format(sum, phone_number, delivery, desc)
    msg.attach(MIMEText(body, 'plain'))

    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
