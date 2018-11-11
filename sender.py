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
    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = "НОВЫЙ ЗАКАЗ!!!"

    body = """
    Сумма: {}
    """.format(sum)
    msg.attach(MIMEText(body, 'plain'))

    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
