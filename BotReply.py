import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.INFO)

# Replace with your bot token
TOKEN = '6824227205:AAGGM26UK5TddpoMTKXuzD06OUXsM_F2qCg'

# Enter sender Telegram Chat ID (Target TG Chat I'D)
SENDER_ID = 6541281150

# Enter receiver Telegram Chat ID (My TG Chat I'D)
RECEIVER_ID = 6541281150

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Hello, Buddy! How Can I Help You?')

def send_message(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=RECEIVER_ID, text=message)

def receive_message(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=SENDER_ID, text=message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_message))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
