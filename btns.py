from telebot import types

asosiykv = types.ReplyKeyboardMarkup(row_width=2)

asosiykb1 = types.KeyboardButton(text="0-10")
asosiykb2 = types.KeyboardButton(text="0-50")
asosiykb3 = types.KeyboardButton(text="0-100")
asosiykb4 = types.KeyboardButton(text="0-500")
asosiykb5 = types.KeyboardButton(text="0-1000")
asosiykb6 = types.KeyboardButton(text="0-5000")


asosiykv.add(
    asosiykb1,
    asosiykb2,
    asosiykb3,
    asosiykb4,
    asosiykb5,
    asosiykb6,

)