from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products

initiate_db()

api = '7796297757:AAGu2Uh6THkb3UctSKWjYsuN0g5cJMbniiE'

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button3 = KeyboardButton(text="Купить")
kb.add(button)
kb.add(button2)
kb.add(button3)

product_kb = InlineKeyboardMarkup(row_width=2)
products = ['Product1', 'Product2', 'Product3', 'Product4']
for i, product in enumerate(products, start=1):
    product_button = InlineKeyboardButton(text=product, callback_data='product_buying')
    product_kb.add(product_button)

in_kb = InlineKeyboardMarkup(row_width=2)
in_button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
in_button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
in_kb.add(in_button, in_button2)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Выберите действие:", reply_markup=kb)

@dp.message_handler(lambda message: message.text=="Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=in_kb)

@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()
    if products:
        for product in products:
            product_info = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]} руб."
            await message.answer(product_info)
            try:
                await message.answer_photo(open(f'{product[1]}.jpg', 'rb'))
            except FileNotFoundError:
                await message.answer("Изображение для данного продукта отсутствует.")

        await message.answer("Выберите продукт для покупки:", reply_markup=product_kb)
    else:
        await message.answer("Продуктов нет в базе данных.")

@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")

@dp.callback_query_handler(lambda call: call.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    formula = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5\n"
        "Для женщин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) - 161"
    )
    await call.message.answer(formula)

@dp.callback_query_handler(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")

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
