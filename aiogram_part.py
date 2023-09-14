from aiogram import Bot, Dispatcher, F
import os
from aiogram.types import Message
import asyncio
from dotenv import load_dotenv
from keyboard import kb_markup
from benefit_utils import handler
load_dotenv()
bot = Bot(os.getenv('TOKEN'))

dp = Dispatcher()

@dp.message(F.text == '/start')
async def say_hello(message : Message):
    await bot.send_message(message.chat.id, text='Чтобы начать работу с ботом напишите "Рандом" или нажмите на кнопку', reply_markup=kb_markup)

@dp.message()
async def msg_handler(message : Message):
    if message.text.title() == 'Рандом':
        data_from_db = handler(True)
        await bot.send_message(message.chat.id, text=f'{data_from_db["Имя"][0]}\n\n'
                                                     f'{data_from_db["Описание"][0]}\n\n'
                                                     f'{data_from_db["Ссылка"][0]}')
    else:
        await bot.send_message(message.chat.id, text='Я тебя не понимаю')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')