from aiogram.fsm.state import State, StatesGroup


class RegistrationProfile(StatesGroup):
    user_name = State()
    user_age = State()
    user_city = State()