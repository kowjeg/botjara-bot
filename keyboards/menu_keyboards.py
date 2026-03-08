from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='⛅ Погода'),
                KeyboardButton(text='📰 Новости')

            ],
            [
                KeyboardButton(text='⚙️ Настройки')
            ],
            [
                KeyboardButton(text='✖️ Закрыть меню')
            ],


        ],
        resize_keyboard=True
    )