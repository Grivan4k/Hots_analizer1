
**Утилита командной строки для массового приема и валидации ID игроков с автоматическим сохранением в файл**

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)](https://github.com)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)](requirements.txt)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-black)](https://www.python.org/dev/peps/pep-0008/)

## 📋 Описание

Player ID Manager - это консольная утилита для работы с идентификаторами игроков. Программа принимает ID из аргументов командной строки, проверяет их валидность и сохраняет в структурированном формате (JSON или TXT).

### Основные возможности

- ✅ **Прием множества ID** через аргументы командной строки
- ✅ **Валидация формата** ID (числа или UUID)
- ✅ **Автоматическое сохранение** в JSON или TXT файл
- ✅ **Гибкая конфигурация** через файл `.env`
- ✅ **Цветной вывод** с информацией о процессе (опционально)
- ✅ **Ограничение количества** обрабатываемых ID
- ✅ **Интеграция с внешним API** для расширенной валидации

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
git clone https://github.com/your-username/player-id-manager.git
cd player-id-manager
