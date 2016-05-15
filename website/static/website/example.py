from telegram.ext import Updater, CommandHandler

def start(bot, update):
    bot.send_message(update.message.chat_id, text='Hello World!')

def hello(bot, update):
    bot.send_message(update.message.chat_id,
                    text='Hello {0}'.format(update.message.from_user.first_name))

updater = Updater('YOUR TOKEN HERE')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
