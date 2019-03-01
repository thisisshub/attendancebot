import telebot
import parser

TOKEN = "709939332:AAEKXDHCEJgqGLyIaqvAZu8aybrNf6j9nfw"
bot = telebot.TeleBot(TOKEN)

@ bot.message_handler (commands = ['start', 'go'])
def start_handler (message):
    bot.send_message (message.chat_id "Hello this is the attendance bot")
    bot.polling()

    
