import asyncio
from aiogram import Bot, Dispatcher, types
from aiohttp import web
import json

API_TOKEN = '....'
bot = Bot(token='1393668330:AAGpfdN4_W5Se5mCz3RHfsYnVF2CDViDfcY')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


async def myupdate():
    update = {"update_id": 960323333,
              "message": {"message_id": 3846, "from": {"id": 20936078, "is_bot": False,
                                                       "first_name": "ᴅᴀᴠʟᴀᴛᴊᴏɴ🐼",
                                                       "username": "davlatjon_1",
                                                       "language_code": "ru"},
                          "chat": {"id": 20936078,
                                   "first_name": "ᴅᴀᴠʟᴀᴛᴊᴏɴ🐼",
                                   "username": "davlatjon_1", "type": "private"},
                          "date": 1602509595, "text": "/start",
                          "entities": [{"offset": 0, "length": 6, "type": "bot_command"}]}}
    # mydict = {k: v.encode("utf-8") for k, v in update.items()}
    # update = json.dumps(update)
    update = types.Update(**update)

    Bot.set_current(dp.bot)
    Dispatcher.set_current(dp)
    await dp.process_updates([update])


loop = asyncio.get_event_loop()
tasks = [loop.create_task(myupdate())]
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)