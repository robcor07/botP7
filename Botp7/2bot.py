#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""Simple inline keyboard bot with multiple CallbackQueryHandlers.
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined as callback query handler. Then, those functions are
passed to the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
import logging
from telegram import InlineKeyboardButton,ReplyKeyboardMarkup, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler,
    Filters
    
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THIRD, FOURTH, VERIF = range(5)
# Callback data
ONE, TWO, THREE, FOUR = range(4)



A, B, C, D, E, F, G, H, I, J = range(10)#edificios y aulas

codigo="1234567"
x=""



def start(update: Update, context: CallbackContext):
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    #update.message.reply_text("Bienvenido. Por favor ingresa el codigo institucional:", reply_markup=reply_markup)
    #reply_keyboard=''
    update.message.reply_text(
    'Hola! Bienvenido\n '
        'Por favor ingresa el codigo Institucional.\n\n',
      #  reply_markup=ReplyKeyboardMarkup(
       #     one_time_keyboard=True, input_field_placeholder='Codigo' ,
        #    x=reply_keyboard
            
            
       # ),
       
    )
    user_input = update.message.text
    '''updater = Updater("TOKEN", use_context=True)
    dp = updater.dispatcher
    x=dp.add_handler(MessageHandler(Filters.text))
    print("aqui")
    print (x)'''

    '''if (len(codigo) > 7):
        return SECOND
    else:'''
    print (user_input)
    return VERIF

def saludo(update: Update, context: CallbackContext) -> int:
    
    keyboard = [
    [
    InlineKeyboardButton("Aula", callback_data=str(ONE)),
    InlineKeyboardButton("Departamento", callback_data=str(TWO)),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    #update.message.reply_text("Bienvenido. Selecciona el area donde se necesita el soporte:", reply_markup=reply_markup)
    update.message.reply_text("Bienvenido. Ingresa tu codigo:", reply_markup=reply_markup)
    #dp.add_handler(MessageHandler(Filters.text, echo))    
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

      

def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Aula", callback_data=str(ONE)),
            InlineKeyboardButton("Departamento", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="Bienvenido. Selecciona el area donde se necesita el soporte:", reply_markup=reply_markup)
    return FIRST


def edificio(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data=str(A)),
            InlineKeyboardButton("B", callback_data=str(B)),
            InlineKeyboardButton("C", callback_data=str(C))
        ],
        [
            
            InlineKeyboardButton("D", callback_data=str(D)),
            InlineKeyboardButton("E", callback_data=str(E)),
            InlineKeyboardButton("F", callback_data=str(F))
        ],
        [
            InlineKeyboardButton("G", callback_data=str(G)),
            InlineKeyboardButton("H", callback_data=str(H)),
            InlineKeyboardButton("I", callback_data=str(I)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige el edificio:", reply_markup=reply_markup
    )
    return THIRD

def aula(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("A", callback_data=str(A)),
            InlineKeyboardButton("B", callback_data=str(B))
            
        ],
        [
            InlineKeyboardButton("C", callback_data=str(C)),
            InlineKeyboardButton("D", callback_data=str(D))
        ],
        [
            InlineKeyboardButton("E", callback_data=str(E)),
            InlineKeyboardButton("F", callback_data=str(F))
        ],
        [
            InlineKeyboardButton("G", callback_data=str(G)),
            InlineKeyboardButton("H", callback_data=str(H))
            
        ],
        [   
            InlineKeyboardButton("I", callback_data=str(I)),
            InlineKeyboardButton("J", callback_data=str(J))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Elige el aula:", reply_markup=reply_markup
    )
    return FIRST

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)





def two(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Second CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return FIRST


def three(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Yes, let's do it again!", callback_data=str(ONE)),
            InlineKeyboardButton("Nah, I've had enough ...", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Third CallbackQueryHandler. Do want to start over?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SECOND


def four(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("2", callback_data=str(TWO)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Fourth CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return FIRST


def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5208486108:AAGvp0OyrjH7Ld8H828VQoo6F04WAiyY_V0")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(edificio, pattern='^' + str(A) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(B) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(C) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(D) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(E) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(F) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(G) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(H) + '$'),
                CallbackQueryHandler(edificio, pattern='^' + str(I) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
            ],
            THIRD:[
                CallbackQueryHandler(aula, pattern='^' + str(A) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(B) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(C) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(D) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(E) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(F) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(G) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(H) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(I) + '$'),
                CallbackQueryHandler(aula, pattern='^' + str(J) + '$'),
            ],
            FOURTH:[
                CallbackQueryHandler(saludo, pattern='^' + str(A) + '$'),
                
            ],
            VERIF:[
                
            ]
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()