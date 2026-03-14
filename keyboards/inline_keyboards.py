from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def demo_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Погода', callback_data='btn:news_btn'),
                InlineKeyboardButton(text='test button2', callback_data='btn:test_btn2', style='danger'),
                InlineKeyboardButton(text='test button3', callback_data='btn:test_btn3')
            ],
            [
                InlineKeyboardButton(text='test button4', callback_data='btn:test_btn4', style='success')
            ]
        ]
    )