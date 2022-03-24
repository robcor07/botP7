"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://git.io/JOmFw.
"""
from array import array
import logging
from re import X

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


arreglo=( "aula1", "aula2", "aula3")



for n in arreglo:
    print(n)



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Aula", callback_data='Aula'),
            InlineKeyboardButton("Departamento", callback_data='Departamento'),
        ],

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Bienvenido al Bot de soporte de P7:', reply_markup=reply_markup)

def respuesta1(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    #query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton("MODULO A", callback_data='Aula'),
            InlineKeyboardButton("MODULO B", callback_data='Departamento'),
        ],
        InlineKeyboardButton("MODULO C", callback_data='Aula'),
        InlineKeyboardButton("MODULO D", callback_data='Departamento'),

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Bienvenido al Bot de soporte de P7:', reply_markup=reply_markup)


def respuesta (update, context):
    query= update.callback_query
    if (query == "Aula"):
        query.answer()

    query.edit_message_text(text=f"usted entro al menu  : {query.data}")

        


def button(update: Update, context: CallbackContext) -> int:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    
    
    query.edit_message_text(text=f"Usted entreo al menu: {query.data}")
    return 1




def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    # updater = Updater("5208486108:AAGvp0OyrjH7Ld8H828VQoo6F04WAiyY_V0")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    x=updater.dispatcher.add_handler(CallbackQueryHandler(button))
    print(x)

    
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()