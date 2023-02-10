import openai
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from environs import Env

env = Env()
env.read_env()


token = env.str("BOT_TOKEN")

openai.api_key = os.environ.get('OPENAI_API_KEY')


bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hello! I'm a bot that can talk with you. \n"
                         "Send me a message and I'll try to answer it as best I can")


    


@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    wait = await message.answer("I am thinking...")
    await message.answer(response['choices'][0]['text'], caption="Join our support group: https://t.me/chatgpt4sub_chat")
    await wait.delete()

executor.start_polling(dp, skip_updates=True)
