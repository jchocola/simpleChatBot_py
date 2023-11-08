import telebot
TOKEN = "6563038898:AAE5tK3lRHNbxuSegbRKn8iKYugKA5VJkcE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(messge):
    bot.send_message(messge.chat.id,'dit me may')

bot.polling(non_stop=True)