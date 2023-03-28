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

# Обработчик команды /start
@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f'Приветствую!')
    await state.reset_state()

# Обработчик текстовых сообщений в состоянии waiting_for_work
@dp.message_handler(state='waiting_for_work')
async def handle_text_messages(message: types.Message, state: FSMContext):
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
    executor.start_polling(dp, on_startup=cmd_start)
