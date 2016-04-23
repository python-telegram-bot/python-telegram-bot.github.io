from telegram.ext import Updater, CommandHandler

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World!')

def hello(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello {0}'.format(update.message.from_user.name))

updater = Updater('YOUR TOKEN HERE')

updater.dispatcher.addHandler(CommandHandler('start', start))
updater.dispatcher.addHandler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
