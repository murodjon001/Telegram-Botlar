import logging
import requests
from aiogram import Bot,Dispatcher,executor,types

logging.basicConfig(level=logging.INFO)

API_TOKEN = '5210143277:AAEKW2Obcl6eWy5Vd7wFaIkw4GsJfp37pqM'
url = "https://v6.exchangerate-api.com/v6/d82107e52cea749851e8ce6d/latest/USD"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer(f"Assalomu aleykum {message.from_user.first_name}! Valyuta kursalri botimizga xush kelibsiz!\nValyuta kursini ko'rmoqchi bo'lsangiz (/uzs_usd),(/usd_rub) komandasini bosing! ")
@dp.message_handler(commands='uzs_usd')
async def exchange(message:types.Message):


    responce = requests.get(url)

    data = responce.json()
    uzb = data['conversion_rates']['UZS']

    await message.answer(f"1 AQSH dollari {uzb} so'mga teng!")


@dp.message_handler(commands='usd_rub')
async def rus_usa(message:types.Message):
    responce = requests.get(url)

    data = responce.json()
    rus = data['conversion_rates']['RUB']
    await message.answer(f"1 AQSH dollari {rus} rublga teng!")




if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)



#