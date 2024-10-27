from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ''

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
#
bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.add(button)
kb.add(button2)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Выберите действие:", reply_markup=kb)

@dp.message_handler(lambda message: message.text=="Рассчитать")
async def set_age(message: types.Message):
    await UserState.age.set()
    await message.answer("Введите свой возраст:")

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите свой рост:")

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите свой вес:")

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
