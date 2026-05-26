#!/usr/bin/env python3


import argparse
import os
import sys
import json
from datetime import datetime
from typing import List

# Зависимости:
# 1. colorama - для цветного вывода (требует установки)
# 2. python-dotenv - для работы с .env файлами
# 3. requests - для демонстрации сетевого запроса (опционально)

try:
    from colorama import init, Fore, Style
    init(autoreset=True)  # Инициализация colorama
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False
    # Заглушка, если colorama не установлена
    class Fore:
        RED = GREEN = YELLOW = CYAN = RESET = ''
    Style = type('Style', (), {'BRIGHT': '', 'RESET_ALL': ''})()

try:
    from dotenv import load_dotenv
    HAS_DOTENV = True
except ImportError:
    HAS_DOTENV = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def check_dependencies():
    """Проверка установленных зависимостей и окружения"""
    print(f"{Fore.CYAN}=== Проверка окружения ==={Style.RESET_ALL}")
    print(f"Python версия: {sys.version}")
    print(f"ОС: {sys.platform}")
    
    # Проверка зависимостей
    deps_status = {
        "colorama": HAS_COLORAMA,
        "python-dotenv": HAS_DOTENV,
        "requests": HAS_REQUESTS
    }
    
    missing = [dep for dep, installed in deps_status.items() if not installed]
    
    if missing:
        print(f"{Fore.RED}[ОШИБКА] Отсутствуют зависимости: {', '.join(missing)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[ИНФО] Установите их командой:{Style.RESET_ALL}")
        print(f"pip install {' '.join(missing)}")
        return False
    else:
        print(f"{Fore.GREEN}[OK] Все зависимости установлены{Style.RESET_ALL}")
        return True


def load_env_config():
    """Загрузка конфигурации из .env файла"""
    if HAS_DOTENV:
        load_dotenv()
    
    config = {
        "max_players": int(os.getenv("MAX_PLAYERS", "100")),
        "output_format": os.getenv("OUTPUT_FORMAT", "json"),
        "enable_validation": os.getenv("ENABLE_VALIDATION", "true").lower() == "true",
        "validation_api": os.getenv("VALIDATION_API", "")
    }
    
    print(f"{Fore.CYAN}[КОНФИГ] Конфигурация из .env:{Style.RESET_ALL}")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    return config


def validate_player_id(player_id: str, config: dict) -> bool:
    """Валидация ID игрока (может использовать внешний API)"""
    if not config["enable_validation"]:
        return True
    
    # Простая валидация: ID должен быть числом или UUID
    if player_id.isdigit():
        return True
    elif len(player_id) == 36 and player_id.count('-') == 4:
        # Простейшая проверка UUID формата
        return True
    
    # Демонстрация использования requests для валидации через API
    if HAS_REQUESTS and config.get("validation_api"):
        try:
            response = requests.get(
                f"{config['validation_api']}/validate/{player_id}",
                timeout=2
            )
            return response.status_code == 200
        except:
            pass
    
    print(f"{Fore.YELLOW}[ПРЕДУПРЕЖДЕНИЕ] ID '{player_id}' не соответствует стандартному формату{Style.RESET_ALL}")
    return True


def save_to_file(players: List[str], config: dict):
    """Сохранение массива ID в файл"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if config["output_format"] == "json":
        filename = f"players_{timestamp}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                "timestamp": timestamp,
                "count": len(players),
                "players": players
            }, f, indent=2, ensure_ascii=False)
    else:
        filename = f"players_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Список ID игроков ({timestamp})\n")
            f.write(f"# Всего: {len(players)}\n")
            for player_id in players:
                f.write(f"{player_id}\n")
    
    print(f"{Fore.GREEN}[СОХРАНЕНО] Массив ID сохранен в файл: {filename}{Style.RESET_ALL}")


def main():
    """Основная функция скрипта"""
    parser = argparse.ArgumentParser(
        description="Прием ID игроков из аргументов командной строки",
        epilog="Пример: python player_ids.py --ids 12345 67890 99999 --max 50"
    )
    
    parser.add_argument(
        '--ids', '-i',
        nargs='+',  # Принимает один или более аргументов
        required=True,
        help='Список ID игроков (через пробел)'
    )
    
    parser.add_argument(
        '--max', '-m',
        type=int,
        default=None,
        help='Максимальное количество ID (по умолчанию из .env или 100)'
    )
    
    parser.add_argument(
        '--output', '-o',
        choices=['json', 'txt'],
        help='Формат выходного файла'
    )
    
    parser.add_argument(
        '--no-save',
        action='store_true',
        help='Не сохранять в файл, только вывести на экран'
    )
    
    args = parser.parse_args()
    
    # Проверка окружения и зависимостей
    if not check_dependencies():
        sys.exit(1)
    
    # Загрузка конфигурации
    config = load_env_config()
    
    # Переопределение параметров из аргументов командной строки
    max_players = args.max if args.max is not None else config["max_players"]
    if args.output:
        config["output_format"] = args.output
    
    # Получение ID игроков
    player_ids = args.ids
    
    # Ограничение количества ID
    if len(player_ids) > max_players:
        print(f"{Fore.YELLOW}[ПРЕДУПРЕЖДЕНИЕ] Получено {len(player_ids)} ID, но ограничение {max_players}. Будет взято первые {max_players}{Style.RESET_ALL}")
        player_ids = player_ids[:max_players]
    
    # Валидация ID
    print(f"{Fore.CYAN}[ВАЛИДАЦИЯ] Проверка ID игроков...{Style.RESET_ALL}")
    valid_ids = []
    for pid in player_ids:
        if validate_player_id(pid, config):
            valid_ids.append(pid)
        else:
            print(f"{Fore.RED}[ОШИБКА] Неверный ID: {pid}{Style.RESET_ALL}")
    
    if not valid_ids:
        print(f"{Fore.RED}[ОШИБКА] Нет валидных ID для обработки{Style.RESET_ALL}")
        sys.exit(1)
    
    # Вывод результата
    print(f"\n{Fore.CYAN}=== РЕЗУЛЬТАТ ==={Style.RESET_ALL}")
    print(f"Получено ID игроков: {len(valid_ids)}")
    print(f"Массив ID: {valid_ids}")
    
    # Сохранение в файл (если не указан флаг --no-save)
    if not args.no_save:
        save_to_file(valid_ids, config)
    else:
        print(f"{Fore.YELLOW}[ИНФО] Сохранение в файл пропущено (флаг --no-save){Style.RESET_ALL}")
    
    print(f"{Fore.GREEN}[ГОТОВО] Скрипт успешно завершил работу{Style.RESET_ALL}")


if __name__ == "__main__":
    main()