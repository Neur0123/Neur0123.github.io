import datetime
from aiogram import Bot, Dispatcher,executor, types

TOKEN = '6822308633:AAGHmvTSwj3NNIZE9IoO7pEeW10zZWUBxMI'


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  await message.answer(
      "Привет! отправь мне любое сообщение, а я дам тебе отчётность.")


@dp.message_handler()
async def week(message: types.Message):
  today = datetime.datetime.today()
  week = today.isocalendar()[1]
  if week % 2 == 0:
    await message.answer(
        f'Текущая дата: {today.year, today.month, today.day}\nТекущий номер недели: {week}\nНеделя чётная.'
    )
  else:
    await message.answer(
        f'Текущая дата: {today.year, today.month, today.day}\nТекущий номер недели: {week}\nНеделя нечётная.'
    )


if __name__ == '__main__':
  executor.start_polling(dp)
