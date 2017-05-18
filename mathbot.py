#!/usr/bin/env python3
# python-telegram-bot https://python-telegram-bot.org/
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import operator

updater = Updater(token='389834819:AAEQuzY3VDqpp6P4ipr3om6bf8ggb64nYfs')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, I can perform arithmetic operations!") # Welcome message

# /help command
def help(bot, update):
    # Menu options
    keyboard = [[InlineKeyboardButton("Valid operators", callback_data='1')],
                [InlineKeyboardButton("Examples", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup) # Menu title

# Function that prints information according to the selected option
def button(bot, update):
    query = update.callback_query
    if query.data == '1':
        text = "Operators: \n + Addition \n - Subtraction \n * Multiplication \n / Division \n ** Exponentiation" # Valid operators
    elif query.data == '2':
        text = "Examples: \n Addition: 5+4 \n Subtraction: 10-3 \n Multiplication: 7*5 \n Division: 45/9 \n Exponetiation: 5**3 \n Other: 5*6+5, (6*4)-6" # Examples
    bot.editMessageText(text = text,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

# Function that validates operation introduced and print the result
def op(bot, update):
    num = update.message.text
    try:
        op = eval(num)
    except (NameError, SyntaxError):
        op = 'Error'
    bot.send_message(chat_id=update.message.chat_id, text=op)

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
op_handler = MessageHandler(Filters.text, op)
button_handler = CallbackQueryHandler(button)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(op_handler)

updater.start_polling()
