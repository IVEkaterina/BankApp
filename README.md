# BankApp
## Описание:
 BankApp - это новая фича для личного кабинета клиетна крупного банка. Это виджет, который показывает несколько последних успешных банковских операций клиента.
## Цель проекта:
 Создать новую функцию для личного кабинета
## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
1. Откройте приложение в вашем веб-браузере.
2. Изучить функции
3. Начать пользоваться
## Примеры:
1. Функция `get_mask_card_number`, принимает на вход номер карты и возвращает ее маску
```
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
```
2. Функция `get_mask_account`, принимает на вход номер счета и возвращает его маску
```
73654108430135874305  # входной аргумент
**4305  # выход функции
```
3. Функция `mask_account_card`, обрабатывает информацию как о картах, так и о счетах
```
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```
4. Функция `get_date`, принимает на вход строку с датой и возвращает строку с датой в нужном формате
```
"2024-03-11T02:26:18.671407" # входной аргумент
"11.03.2024" # выход функции
```
5. Функция `filter_by_state`, которая принимает список словарей и опционально значение для ключа state(по умолчанию `EXECUTED`) и возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
```
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
6. Функция `sort_by_date`, которая принимает список словарей и необязательный параметр(по умолчанию — убывание), задающий порядок сортировки и возвращает новый список, отсортированный по дате.
```
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
