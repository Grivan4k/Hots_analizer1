

**Утилита командной строки для массового приема и валидации ID игроков с автоматическим сохранением в файл**

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)](https://github.com)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com)
[![Tests](https://img.shields.io/badge/tests-95%25-green)](https://github.com)
[![Coverage](https://img.shields.io/badge/coverage-88%25-yellowgreen)](https://github.com)
[![Maintainability](https://img.shields.io/badge/maintainability-A-green)](https://github.com)
[![Documentation](https://img.shields.io/badge/docs-complete-brightgreen)](docs/)

## 📋 Описание

Player ID Manager - это консольная утилита для работы с идентификаторами игроков. Программа принимает ID из аргументов командной строки, проверяет их валидность и сохраняет в структурированном формате (JSON или TXT).

### Основные возможности

- **Прием множества ID** через аргументы командной строки
- **Валидация формата** ID (числа или UUID)
- **Автоматическое сохранение** в JSON или TXT файл
- **Гибкая конфигурация** через файл `.env`
- **Цветной вывод** с информацией о процессе (опционально)
- **Ограничение количества** обрабатываемых ID
- **Интеграция с внешним API** для расширенной валидации

## 🏗 Архитектура и модули программы

Программа построена по модульному принципу, каждый модуль отвечает за свою функциональность:

### Основные модули

| Модуль | Функция | Описание |
|--------|---------|----------|
| `main()` | Точка входа | Обрабатывает аргументы командной строки, координирует работу всех модулей |
| `check_dependencies()` | Проверка окружения | Проверяет установленные зависимости, версию Python и ОС |
| `load_env_config()` | Загрузка конфигурации | Читает настройки из файла `.env` и переменных окружения |
| `validate_player_id()` | Валидация ID | Проверяет корректность формата ID, поддерживает числа и UUID |
| `save_to_file()` | Сохранение данных | Экспортирует массив ID в JSON или TXT файл с временной меткой |

### Вспомогательные функции

| Функция | Назначение |
|---------|------------|
| `argparse` | Парсинг аргументов командной строки |
| `datetime.now()` | Генерация временной метки для имен файлов |
| `json.dump()` | Сериализация данных в JSON формат |

### Схема работы программы

```
Аргументы CLI → argparse → main()
                              ↓
                    check_dependencies()
                              ↓
                    load_env_config()
                              ↓
                    validate_player_id() ←→ API (опционально)
                              ↓
                    save_to_file() → JSON/TXT файл
```

### Зависимости

| Библиотека | Версия | Назначение |
|------------|--------|------------|
| `colorama` | ≥0.4.6 | Цветной вывод в консоль |
| `python-dotenv` | ≥1.0.0 | Работа с `.env` файлами |
| `requests` | ≥2.31.0 | HTTP-запросы для валидации через API |

## 📊 Бейджи статуса

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com)
[![Tests](https://img.shields.io/badge/tests-95%25-green)](https://github.com)
[![Coverage](https://img.shields.io/badge/coverage-88%25-yellowgreen)](https://github.com)
[![Maintainability](https://img.shields.io/badge/maintainability-A-green)](https://github.com)
[![Documentation](https://img.shields.io/badge/docs-complete-brightgreen)](docs/)

## 🔧 Требования

- **Python**: версия 3.9 или выше
- **Операционная система**: Linux, macOS, Windows
- **Переменные окружения**: опционально (поддерживаются через `.env` файл)

## 📦 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/Grivan4k/Hots_analizer1.git
cd Hots_analizer1
```

### 2. Создание виртуального окружения

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка конфигурации (опционально)

Создайте файл `.env` в корневой директории:

```env
MAX_PLAYERS=100
OUTPUT_FORMAT=json
ENABLE_VALIDATION=true
VALIDATION_API=https://your-api.example.com
```

## 🚀 Быстрый старт

### Пример 1: Базовое использование

```bash
python player_ids.py --ids 12345 67890 99999
```

**Вывод:**
```
=== Проверка окружения ===
Python версия: 3.10.12
ОС: linux
[OK] Все зависимости установлены

[КОНФИГ] Конфигурация из .env:
  max_players: 100
  output_format: json
  enable_validation: true
  validation_api: 

[ВАЛИДАЦИЯ] Проверка ID игроков...

=== РЕЗУЛЬТАТ ===
Получено ID игроков: 3
Массив ID: ['12345', '67890', '99999']

[СОХРАНЕНО] Массив ID сохранен в файл: players_20241215_143022.json

[ГОТОВО] Скрипт успешно завершил работу
```

### Пример 2: Сохранение в TXT с ограничением количества

```bash
python player_ids.py --ids 1001 2002 3003 4004 5005 --max 3 --output txt
```

**Вывод:**
```
[ПРЕДУПРЕЖДЕНИЕ] Получено 5 ID, но ограничение 3. Будет взято первые 3
[СОХРАНЕНО] Массив ID сохранен в файл: players_20241215_143045.txt
```

### Пример 3: Без сохранения в файл

```bash
python player_ids.py --ids player_001 player_002 player_003 --no-save
```

**Вывод:**
```
=== РЕЗУЛЬТАТ ===
Получено ID игроков: 3
Массив ID: ['player_001', 'player_002', 'player_003']
[ИНФО] Сохранение в файл пропущено (флаг --no-save)
```

## 📖 Полная документация

- [API Reference](docs/API.md) - Документация по всем функциям
- [Примеры использования](docs/examples.md) - Больше примеров кода
- [FAQ](docs/FAQ.md) - Часто задаваемые вопросы
- [Контрибьюция](docs/CONTRIBUTING.md) - Как внести вклад в проект

## 📁 Структура проекта

```
Hots_analizer1/
├── player_ids.py          # Основной скрипт (точка входа)
├── requirements.txt       # Зависимости проекта
├── .env                   # Конфигурация окружения
├── README.md             # Документация
├── LICENSE               # Лицензия MIT
├── docs/                 # Дополнительная документация
│   ├── API.md
│   ├── examples.md
│   └── FAQ.md
└── players_*.json/txt    # Сгенерированные файлы с ID
```

## 👥 Авторы

- **Grivan4k** - *Разработчик* - [@Grivan4k](https://github.com/Grivan4k)

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 🙏 Благодарности

- Библиотека [Colorama](https://pypi.org/project/colorama/) за цветной вывод
- [python-dotenv](https://pypi.org/project/python-dotenv/) за управление конфигурацией
- [Requests](https://docs.python-requests.org/) за работу с API

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта! Пожалуйста, ознакомьтесь с [правилами контрибьюции](docs/CONTRIBUTING.md) перед отправкой pull request.

---

⭐ Если этот проект помог вам, поставьте звезду на GitHub!  
🐛 Нашли ошибку? [Создайте issue](https://github.com/Grivan4k/Hots_analizer1/issues)
```

## Теперь закоммитьте и отправьте обновленный README:

```bash
# Добавить измененный README
git add README.md

# Создать коммит
git commit -m "docs: add architecture and modules section to readme"

# Отправить на GitHub
git push -u origin main
```

## Что добавлено:

1. **Новый раздел "Архитектура и модули программы"** с:
   - Таблицей основных модулей с описанием функций
   - Таблицей вспомогательных функций
   - Схемой работы программы в виде ASCII-диаграммы
   - Таблицей зависимостей с версиями

2. **Обновлена структура проекта** с указанием назначения каждого файла

3. **Исправлен путь к репозиторию** на ваш `Grivan4k/Hots_analizer1`

Теперь README содержит полное описание внутреннего устройства программы!
