import logging
from db import database,database2
from config import API_TOKEN

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}! \n 🌐 Wikipedia botiga xush kelibsiz \n✅Marhamat endi Wikipediadan foydalanishingiz mumkin ")
    file1 = open('balans.txt', 'r')
    tt = file1.readline()
    t = int(tt)
    t1 = t+1
    file = open('balans.txt', 'w')
    file.write(str(t1))
    file.close()
    
@dp.message_handler()
async def send_wiki(message: types.Message):
    text = message.text
    if len(text.split()) > 1:
        await message.reply(database(text))
    elif text == 'balans':
        file1 = open('balans.txt', 'r')
        tt = file1.readline()
        await message.answer(f"Faydalanuchilar: {tt}")
    else:
        try:
            await message.reply(database2(text)['definitions'])
        except:
            await message.answer(database(text))



        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)