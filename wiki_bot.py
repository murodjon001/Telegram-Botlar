import logging
from aiogram.types import ContentTypes, Message

from aiogram import Bot,Dispatcher,executor,types
API_TOKEN = "bu yerda API token turadi"


logging.basicConfig(level=logging.INFO)

bot = Bot(token= API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands= "start")
async def send_welcome(message: Message):

    await message.reply(f"Salom wikipedia botimizga xush kelibsiz!")


@dp.message_handler()

async def surov(message: Message):
 
    try:
        import wikipedia
        wikipedia.set_lang("uz")
        wiki = wikipedia.summary(message.text)
        await message.answer(wiki)

    except:
        await message.answer("Kechirasiz bunday natijani topa olmadik !")
        

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
