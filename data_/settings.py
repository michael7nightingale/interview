"""
Файл с конфигурациями.
"""

import os
import logging


# настройка логирования
logger = logging.Logger(name='system_log', level='INFO')
fileHandler = logging.FileHandler(filename='system_log.log',
                                  encoding='utf-8')
formatter_ = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s")
fileHandler.setFormatter(formatter_)
logger.addHandler(fileHandler)


# строго для src/tables.py
TABLES = {
    "ALLOWED_EXTENSIONS": frozenset(("csv", )),
    "LOGGER_LEVEL": "DEBUG",

}

# строго для src/celebration_generator.py
CELEBRATION_GENERATOR = {
    "MESSAGE": """Напиши поздравление для человека __name__ в день рождения, который родился 
    __birthday__. Сделай это душевно, всё таки это день рождения. Не забудь упомянуть дату рождения. Добавь юмора.""",
    "TOKEN": "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", # ВВЕДИТЕ РАБОЧИЙ API-КЛЮЧ!!! МОЙ БЛОКИРУЕТСЯ СПУСТЯ 30 МИНУТ ИЗ-ЗА ГЕОЛОКАЦИИ
    "NAME_COLUMN": "name",
    "BIRTHDAY_COLUMN": 'birthday',

}

# строго для app/app.py
APP = {
    "UPLOAD_FOLDER": os.path.join(os.path.abspath(os.path.dirname(__file__)).replace('data_', 'app', -1), 'corridor/'),
    "ALLOWED_EXTENSIONS": frozenset(("csv", )),
    "SECRET_KEY": "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",

}

SERVER = {
    "HOST": "localhost",
    "PORT": 5000,
}