from config import Config
from telegram.ext import Updater, CommandHandler

#print()

def greet_user(bot, update):
    #print(f'Вызван /start {update}')
    text = ('Вызван /start')
    update.message.reply_text(text)


def main():
    mybot = Updater(Config.TOKEN, request_kwargs=Config.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
	main()



