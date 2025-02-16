# Проект: Сортировка транзакций по дате

## Цель проекта
Цель данного проекта — разработать функцию для сортировки списка транзакций, представленных в виде словарей, по дате. Функция позволяет задавать порядок сортировки (по возрастанию или убыванию) и возвращает новый отсортированный список.

## Установка
1. Склонируйте репозиторий:
```
git clone https://github.com/kufi-xx/skypro_git_tasks
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование
### Импорт функции
Для использования функции `sort_by_date`, импортируйте её в вашем Python-скрипте:
```
from processing import sort_by_date
```
### Пример работы функции
Вот пример использования функции `sort_by_date`:
```python
# Пример входных данных
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).