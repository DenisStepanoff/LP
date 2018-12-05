from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem

PLANETS = {'mars':ephem.Mars, 'mercury':ephem.Mercury, 'pluto':ephem.Pluto}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

#print()

def greet_user(bot, update):
    #print(f'Вызван /start {update}')
    text = ('Вызван /start')
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = (f'Привет, {update.message.chat.first_name}. Ты написал: {update.message.text}')
    #print(update.message)
    logging.info(f'User: {update.message.chat.first_name} {update.message.chat.last_name}, Chat ID: {update.message.chat.id}, Message: {update.message.text}')
    update.message.reply_text(user_text)

def planet_constell(bot, update):
    planet = update.message.text.split(' ')[1]
    #print(planet)
    planet_now = PLANETS[planet.lower()](ephem.now())
    user_text = ephem.constellation(planet_now)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(Config.TOKEN, request_kwargs=Config.PROXY)

    logging.info('Bot starting')

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constell))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
	main()



