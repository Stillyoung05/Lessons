from aiogram import Bot, Dispatcher, types, executor
import openai
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot('6225217255:AAFWOAxwuz5NKr2lbc9JXqIpz5fOG5ceWO4')
# openai.api_key = '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'
Dp = Dispatcher(bot)


# text = [{'role': 'system',
#          'content': ''},
#         {'role': 'user',
#          'content': ''},
#         {'role': 'assistant', 'content': ''}]


# def update(text, role, content):
#     text.append({'role': role, 'content': content})
#     return text


@Dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Assalomu alaykum")


@Dp.message_handler(commands='ask')
async def send_response(message: types.Message):
    await message.answer('Send your question...')

    # update(text, 'user', message.text)

    @Dp.message_handler()
    async def send_answer(message: types.Message):
        # ai = openai.ChatCompletion.create(
        #     model='gpt-3.5-turbo',
        #     messages=text
        # )
        # await message.answer(ai['choices'][0]['message']['content'])
        await message.answer('')


if __name__ == '__main__':
    executor.start_polling(Dp, skip_updates=True)
