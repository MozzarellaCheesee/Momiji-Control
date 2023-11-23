from disnake.ext import commands
from core.settings import events, commands_
from pathlib import Path
import logging

localization_path = Path("./locale/commands")
logging.basicConfig(
    filename='logs/info.log',
    encoding='utf-8',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)


def load_extensions(client: commands.InteractionBot):
    logging.info("Начало загрузки команд")
    for command in commands_:
        try:
            client.load_extension(command)
            logging.info(f"--Модуль {command} был успешно загружен")
        except Exception as e:
            print(
                f"\033[31;1;31m[ERROR] \033[0;0m| Ошибка при загрузке команд: \033[33;1;33m{e}\033[0;0m\n"
                f"----------------------------------------------")
            logging.error(f"++Произошла ошибка при загрузке команд: {e}")
    logging.info("Комманды были успешны загружены")

    logging.info("Начало загрузки ивентов")
    for event in events:
        try:
            client.load_extension(event)
            logging.info(f"--Модуль {event} был успешно загружен")
        except Exception as e:
            print(
                f"\033[31;1;31m[ERROR] \033[0;0m| Ошибка при загрузке ивентов: \033[33;1;33m{e}\033[0;0m\n"
                f"----------------------------------------------")
            logging.error(f"++Произошла ошибка при загрузке ивентов: {e}")
    logging.info("Ивенты были успешно загружены")
