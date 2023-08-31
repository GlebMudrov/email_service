import os, sys
import smtplib
from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

import message as m


def send_email(to_email, copy_email, subject, text, files):
    """
    Отправка электронного письма с вложением
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, 'email.ini')

    # Проверка наличия файла 'email.ini' и извлечение переменных из конфигурации
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
        server = cfg.get('smtp', 'server')
        port = cfg.get('smtp', 'port')
        from_email = cfg.get('smtp', 'email')
        password = cfg.get('smtp', 'password')
    else:
        print('Конфигурация не найдена.')
        sys.exit(1)

    # Формирование тела письма
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)
    if text:
        msg.attach(MIMEText(text))
    msg['To'] = ', '.join(to_email)
    emails = to_email
    if copy_email:
        msg['cc'] = ', '.join(copy_email)
        emails += copy_email

    # Прикрепление файлов к письму
    for file in files:
        attachment = MIMEBase('application', 'octet-stream')
        header = 'Content-Disposition', f'attachment; filename="{file}"'
        try:
            with open(file, 'rb') as fh:
                data = fh.read()
            attachment.set_payload(data)
            encoders.encode_base64(attachment)
            attachment.add_header(*header)
            msg.attach(attachment)
        except IOError:
            print(f'Ошибка при прикреплении файла {file}')

    # Подключение к почтовому серверу и авторизация
    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(from_email, password)
        smtp.sendmail(from_email, emails, msg.as_string())
        print('Письмо успешно отправлено.')
    except smtplib.SMTPException as error:
        print('Ошибка подключения к почтовому серверу.')
        raise error
    finally:
        smtp.quit()

if __name__ == '__main__':
    send_email(m.TO_EMAIL, m.COPY_EMAIL, m.SUBJECT, m.TEXT, m.FILES)
