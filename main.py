from translate import translate
import telebot

TOKEN = "7122971731:AAFXPhUIjahO6oPFysWylqz2Y7mUz5VfIUQ"
tarjimonbot = telebot.TeleBot(token=TOKEN)


@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu alaykum tarjimon botga hush kelibsiz, bu bot tarjima qiladi."
    xabar += '\nMatningizni yuboring'
    tarjimonbot.reply_to(message, xabar)


@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))


tarjimonbot.polling()
