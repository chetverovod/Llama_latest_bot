import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from datetime import datetime
from aiogram import F
from aiogram.types import Message
from aiogram import html
import ollama

help_info = f"/p type your prompt.\n\nExample:\n/p Why sky is blue?"

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота. Для создания этого объекта вам нужно получить токен.
# токена зайдите в Телеграм-канал @BotFather и зарегистрируйте своего
# уникального бота. 
bot = Bot(token="")

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply(help_info)

# Хэндлер на команду /p
@dp.message(Command("p"))
async def cmd_p(message: types.Message):
    prompt = message.text.strip()[2:]
    response = ollama.chat(model='llama3.1', messages=[
    {
       'role': 'user',
       'content': prompt,
    },
    ])
    # print(response['message']['content'])
    print(prompt)
    await message.reply(response['message']['content'])

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello it is LLAMA3.1-8B based chat!\n\nHow to:\n{help_info}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


