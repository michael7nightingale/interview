# Тестовое задание для первого собеседования в логистическую компанию.
Сервис для работы в данными о людях в формате csv и генерации поздравлений с днём рождения с помощью ChatGPT API.

## Структура
 - src - Пакет с классами, менеджерами, функциями API. Реализованы классы CsvTableManager и PandasTableManager (позваляют работать с разными модулями для csv). 
 - data_ - Пакет с файлами конфигурация для всех приложений. Рекомендуется все служебные переменные и константы изменять именно здесь (important!!!), например: токен API, названия столбцов, хост и порт, а также шаблон сообщения для GPT.
 - app - Пакет с приложением flask. Я понимаю это сервис именно как одностраничную полу-rest страницу. Но поле для расширения функционала работа с csv представлено в ...TableManager.
 
## Запуск
 - pip install -r requirements.txt
 ### Введите, пожалуйста, свои данные в файле data_/settings.py, в частности API-TOKEN (мой удаляется). 
 ### API работает медленно, тут поделать нечего.
 1) Через main.py. Необходимо ввести корректный путь до файла .csv при инициализации экземпляра класса ...TableManager. Результат при успешной работе = сохранение файла с дополнительной колонкой.
 2) Через src/app/app.py - запуск Flask-приложения на тестовом веб-сервере.
 
 
 P.S. Надеюсь, не over-engineering, пытался реализовать как можно шире, как вижу эту систему.
