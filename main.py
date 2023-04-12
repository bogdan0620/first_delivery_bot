from aiogram import Bot, Dispatcher, executor
import buttons
from states import Registration, GetProduct, Cart, Order
from token2 import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_command(message):
    user_id = message.from_user.id
    start_text = 'Это бот доставки еды\nЧтобы начать процесс регистрации введите свое имя'
    await message.answer(start_text, reply_markup=ReplyKeyboardRemove())
    await Registration.getting_name_state.set()

@dp.message_handler(state=Registration.getting_name_state, content_types=['text'])
async def get_user_name(message):
    if '/' in message.text:
        await message.answer('Введите имя', reply_markup=ReplyKeyboardRemove())

    else:
        user_name = message.text
        await message.answer(f'Привет, {user_name}\nОтправь свой контакт', reply_markup=buttons.phone_number_kb())
        await Registration.getting_phone_number_state.set()

@dp.message_handler(state=Registration.getting_phone_number_state, content_types=['contact'])
async def get_contact(message):
    user_phone_number = message.contact
    await message.answer('Отправь свою локацию', reply_markup=buttons.location_kb())
    await Registration.getting_location.set()

@dp.message_handler(state=Registration.getting_location, content_types=['location'])
async def get_location(message):
    user_location = (message.location.latitude, message.location.longitude)
    await message.answer('Выбери свой пол', reply_markup=buttons.gender_kb())
    await Registration.getting_gender.set()
@dp.message_handler(state=Registration.getting_gender, content_types=['text'])
async def get_gender(message):
    user_gender = message.text
    await message.answer('Вы успешно зарегистрировались')






if __name__ == '__main__':
    executor.start_polling(dp)