import telebot

bot = telebot.TeleBot("7742420433:AAEEQrz9D4vjEeT8EnMKkxX8ls0aOHDe4HQ")

@bot.message_handler(commands=['start'])
def command_start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id,f"Salom {first_name}! Men sizga chatga nima yozsangiz shuni qaytaraman")
    bot.send_sticker(chat_id,"CAACAgIAAxkBAAEDRWJhj0nmkR2iHQg3lRWEj2_qZrx7GwAChwEAAiteUwt4J9ZNhn9pYCIE")
@bot.message_handler(content_types=['text','video','photo','document','audio','sticker','gif','voice'])
def repeat_all_message(message):
    chat_id = message.chat.id
    bot.copy_message(chat_id,chat_id, message.message_id)
bot.polling(none_stop=True)
