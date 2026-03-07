import logging

from aiogram import Router, html
from aiogram.filters import Command
from aiogram.types import Message


logger = logging.getLogger(__name__)
router = Router()

@router.message(Command('start'))
async def start_handler(message: Message) -> None:
    logger.info('пришло сообщение от %s %s с текстом %s', message.from_user.id, message.from_user.full_name,
                message.text)
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!', parse_mode="HTML")


@router.message(Command('help'))
async def help_handler(message: Message) -> None:
    logger.info('Пользователь %s вызвал команду %s', message.from_user.id, message.text)
    help_text = '''
    Список команд:
/start - Приветствие
/help - Список команд
/whoami - Информация о тебе
    '''
    await message.answer(help_text)


@router.message(Command('whoami'))
async def whoami_handler(message: Message) -> None:
    logger.info('Пользователь %s вызвал команду %s', message.from_user.id, message.text)
    user = message.from_user or 'Не указано'
    last_name = user.last_name or 'Не указана'

    await message.answer(
        f'Твой id: {user.id}\n'
        f'Имя: {user.first_name}\n'
        f'Фамилия: {last_name}'
    )