
from telebot import TeleBot, types

import btns

bot = TeleBot("6759179840:AAEoOHrldc1CrRsHCMpmsFnG415-9VZKXH0")


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Assalomu aleykum, ushbu bot ma'lum orqliqdagi ma'lum tasodifiy son tanlash imkonini beradi")


bot.infinity_polling(skip_pending=True)
