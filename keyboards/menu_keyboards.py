from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='⛅ Погода'),
                KeyboardButton(text='📰 Новости')

            ],
            [
                KeyboardButton(text='⚙️ Настройки', style='danger')
            ],
            [
                KeyboardButton(text='✖️ Закрыть меню')
            ],


        ],
        resize_keyboard=True
    )

def weather_get_location():
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='Отправить геологацию', request_location=True)
        ]],
        resize_keyboard=True,
        one_time_keyboard=True
    )