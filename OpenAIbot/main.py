import openai
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()
storage = MemoryStorage()
openai.api_key = os.getenv('TOKEN')
bot = Bot(os.getenv('TOKENbot'))
dp = Dispatcher(bot=bot, storage=storage)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Приветствую!')
    context = dp.current_state(chat=message.chat.id)
    await context.set_state('waiting_for_work')

@dp.message_handler(state='waiting_for_work')
async def handle_text_messages(message: types.Message):
    text = message.text
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=text,
      temperature=0.5,
      max_tokens=1500,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.3,
      stop=["You:"]
    )
    await message.answer(response['choices'][0]['text'])

if __name__ == '__main__':
    executor.start_polling(dp)