from telebot import TeleBot, types

bot = TeleBot("6343310798:AAG0ldicp_CGh0pl2juknEE8LFTCPslbA4c")

@bot.message_handler(commands=["start"])

def start(msg: types.Message):

    kv =types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb = types.KeyboardButton(text="Telefon raqamini yuborish",request_contact=True)
    kv.add(kb)


    bot.send_message(msg.from_user.id,"Telefon raqamingizni kiriting",reply_markup=kv)

@bot.message_handler(commands=["location"])

def location(msg: types.Message):

    kv =types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb = types.KeyboardButton(text="Lokatsiyani yuborish",request_location=True)
    kv.add(kb)


    bot.send_message(msg.from_user.id,"joylashuvingizni kiriting",reply_markup=kv)


@bot.message_handler(content_types=["location"])
def sender(msg: types.Message):
    bot.send_message(msg.from_user.id,f"Sizning joylashuvingiz:{msg.location.longitude}x{msg.location.latitude}")



bot.polling()