import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text("Hola, Geeks!")
    return "Hola, Geeks!"

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    men = "Ayudame!"
    update.message.reply_text(men)
    return men

def mayus(update, context):
    result = []
    for word in context.args:
        result.append(word.upper())

    final_res = ' '.join(result)
    update.message.reply_text(final_res)
    return final_res

def alreves(update, context):
    """Repite el mensaje del usuario."""
    result = []
    user_message = update.message.text
    user_message = user_message.replace('/alreves ', '')[::-1]
    # print(user_message)
    # user_message = user_message.split(' ')
    # tmp = user_message[1]
    # final_res = tmp[::-1]
    # final_res = ' '.join(user_message)[::-1]
    update.message.reply_text(user_message)
    return user_message

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("1266332022:AAEu-KvzfwlSbiiBN0-Jo1tNxkcu5w7xSWA", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = []

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('mayus', mayus))
    updater.dispatcher.add_handler(CommandHandler('alreves', alreves))
    

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    # 
    
    # Y este espera al error
    # dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
