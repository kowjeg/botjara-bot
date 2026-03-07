import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.states import RegistrationProfile

router = Router()


@router.message(Command('registration'))
async def registration_command(message: Message, state: FSMContext):
    await state.set_state(RegistrationProfile.user_name)
    await message.answer('Привет! Начнем процесс регистрации\n\nШаг 1 из 3: Как тебя зовут?')


@router.message(RegistrationProfile.user_name)
async def registration_command(message: Message, state: FSMContext):
    await message.answer(f'Шаг 2 из 3 \n\nПривет, {message.text}! Сколько тебе лет?')
    await state.update_data(name=message.text)
    await state.set_state(RegistrationProfile.user_age)


@router.message(RegistrationProfile.user_age)
async def registration_command(message: Message, state: FSMContext):
    await message.answer(f'Шаг 3 из 3 \n\n Отлично, тебе {message.text} лет. Из какого ты города?')
    await state.update_data(age=message.text)
    await state.set_state(RegistrationProfile.user_city)


@router.message(RegistrationProfile.user_city)
async def registration_command(message: Message, state: FSMContext):
    await message.answer(f'Ты из {message.text}. Регистрация завершена.')
    await state.update_data(city=message.text)
    data = await state.get_data()
    await message.answer(f'Регистрация пройдена успешно, твои данные {data}')
    await state.clear()



@router.message(Command("cancel"))
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Отменено.")


