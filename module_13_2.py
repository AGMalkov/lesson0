from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ""
bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет! Я бот помогающий твоему здоровью.")
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message):
    await message.reply("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
