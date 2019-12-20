
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import settings
import utils
import time

perrete_bot = telegram.Bot(token=settings.TG_TOKEN)
perrete_bot_updater = Updater(perrete_bot.token)

def helpme(bot=perrete_bot_updater, update=perrete_bot_updater):
    print("Solicita ayuda")
    bot.sendMessage(chat_id=update.message.chat_id, 
                    text="Commands:\n \
                    /alalista envia el mensaje citado a la lista\n \
                    /help listado de comandos\n \
                    ")

def alalista(bot=perrete_bot_updater, update=perrete_bot_updater):

    print ("Mensaje" + update.message.reply_to_message.text)
    utils.send_mail(  
        update.message.reply_to_message.from_user.first_name + " te recomienda", 
        update.message.reply_to_message.text
        )
    bot.sendMessage(chat_id=update.message.chat_id, text="Enviado, gracias por tu contribucion !!")

dispatcher = perrete_bot_updater.dispatcher

alalista_handler = CommandHandler('alalista', alalista)  
all_handler = CommandHandler('all', alalista)        
help_handler = CommandHandler('help', helpme)

dispatcher.add_handler(alalista_handler)
dispatcher.add_handler(all_handler)
dispatcher.add_handler(help_handler)

perrete_bot_updater.start_polling()

print("Start PErrete")
while True:
    time.sleep(0.3)
    pass
