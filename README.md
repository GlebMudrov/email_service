# email_service


### Описание проекта:
Функционал для отправки электронных писем email_service позволяет настроить автоматическую отправку сообщений в вашем проекте. Данный функционал подойдет в первую очередь для тех, кому необходимо автоматизировать рассылку писем с вложенными файлами. 

### Технологии :
- Python 3.10
- smtplib 

### Запуск проекта (на примере почтового сервера gmail):
1. Клонировать репозиторий по ssh (при необходимости перенести файлы из репозитория в свой проект):
```
git@github.com:GlebMudrov/email_service.git
```
2. Настроить конфигурацию в файле email.ini:
```
server = smtp.gmail.com
port = 587
email = your_email@gmail.com
```
Для получения пароля для вашего приложения включить двухфакторную аутентификацию на gmail:
```
Ваша почта на gmail -> Аккаунт -> Безопасность -> Раздел "Вход в Google" -> Двухэтапная аутентификация
```
После подключения двухфакторной аутентификации "провалиться" в этот раздел и выбрать в самом низу страницы "Пароли приложений"
Создать пароль для приложения (16 латинских букв) и вставить его в password. Пример заполнения:
```
password = abcdabcdabcdabcd
```
3. Настраиваем параметры письма в файле message.py:
TO_EMAIL - В единственном элементе списка в виде строки указываем адреса получателей через "," (При необходимости можно указать всего 1 адрес). Пример:
```
TO_EMAIL = ['your_friend_first@yandex.ru, your_friend_second@gmail.com']
```
COPY_EMAIL - Эмэилы кого поставить в копию, указываем в единственном элементе списка в виде строки через ",". Для отсутствии получателей в копии оставить список пустым: 
```
COPY_EMAIL = []
```
SUBJECT - Тема письма. Пустая строка - без темы.
```
SUBJECT = 'Тема 1'
```
TEXT - Текст письма. Пустая строка - без текста.
```
TEXT = 'Привет!'
```
FILES - Полный адрес к файлу (с расширением). Каждый последующий - новый элемент списка в виде строки. Пустой список - Без файлов. Пример: 
```
FILES = ['files/file_1.xlsx', 'files/file_2.png']
```
4. Файлы, которые указаны в FILES message.py обязательно должны находиться в соотв. директории ("/files")
5. Из директории проекта отправляем письмо командой:
```
python send.py
```
6. ???????
7. PROFIT

### Автор проекта:  <a href= "https://github.com/GlebMudrov">__Мудров Глеб__<a/>
