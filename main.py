import telebot
from telebot import types
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🐓"))
    bot.send_message(
        message.chat.id,
        f"здорово, кладОвщик {message.from_user.first_name},"
        f" посчитаем баллы?\n Нажми на петуха",
        reply_markup=markup
    )
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAEBUMxlHmKJsybze4CLlXU1yZs0vHSU8QACgQADRA3PF8jAOMgk_BkZMAQ"
    )


a = None
b = None
c = None
d = None
e = None
f = None


@bot.message_handler(content_types=["text"])
def calc(message):
    if message.text == "🐓":
        calc = bot.send_message(message.chat.id, "Сборка")
        bot.register_next_step_handler(calc, next_func)


def next_func(message):
    global a
    a = message.text
    calc2 = bot.send_message(message.chat.id, "Приемка")
    bot.register_next_step_handler(calc2, next_func2)


def next_func2(message):
    global b
    b = message.text
    calc3 = bot.send_message(message.chat.id, "Разнос")
    bot.register_next_step_handler(calc3, next_func3)


def next_func3(message):
    global c
    c = message.text
    calc4 = bot.send_message(message.chat.id, "Инвент")
    bot.register_next_step_handler(calc4, next_func4)


def next_func4(message):
    global d
    d = message.text
    calc5 = bot.send_message(message.chat.id, "выдача Н")
    bot.register_next_step_handler(calc5, next_func5)


def next_func5(message):
    global e
    e = message.text
    calc6 = bot.send_message(message.chat.id, "выдача Б/У")
    bot.register_next_step_handler(calc6, res)


def res(message):
    try:
        global f
        f = message.text
        res = ((int(b) + int(f)) * 0.8 +
               (int(a) + int(c) + int(d) + int(e)) * 0.5)
        bot.send_message(message.chat.id, f"У тебя {res} баллов")
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUNZlHmOwYndrYRwlDajrQTpSFquFFgAChgADRA3PF5hySbZkSauxMAQ"
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            f"Цифры вводи, {message.from_user.first_name},"
            f" совсем Ебанько???"
        )
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUNRlHmOX6atHGhb4QbTbPlGDccS5TgACgwADRA3PF-t8ZIYBnSqzMAQ"
                         )


bot.infinity_polling()
