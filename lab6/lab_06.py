 
from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import three_steps

TOKEN: Final = '6945576738:AAF0qdI6CL4MGYJmKEHgulKjndUiH2DkbWw'
BOT_USERNAME: Final = '@Kashimaahmed_bot'

# # ... (other functions remain the same)
# async def start_command(update: Update, context) -> None:
#     await update.message.reply_text('Hello, thank you!')
# async def stafgfdgrt_command(update: Update, context) -> None:
#     await update.message.reply_text('Hello, thank you!')

async def help_command(update: Update, context) -> None:
    await update.message.reply_text('Help command is not implemented yet.')

async def custom_command(update: Update, context) -> None:
    await update.message.reply_text('Custom command is not implemented yet.')

def send_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='button1'),
         InlineKeyboardButton("Кнопка 2", callback_data='button2')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

def send_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='button1'),
         InlineKeyboardButton("Кнопка 2", callback_data='button2')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

async def send_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_path = '/home/ahmedkashima/Desktop/iu5_3sem_paradig/lab5/pp.img'
    chat_id = update.message.chat_id

    await context.bot.send_photo(chat_id=chat_id, photo=InputFile(open(photo_path, 'rb')))

# ... 
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Yooo, wassup maa nigga!'
    
    if 'how are you' in processed:
        return 'I\'m fine, thank you!'
    
    if 'do you love me' in processed:
        return 'No one loves you -_-'
    
    if 'what kind of help can you do?' in processed:
        return 'Nothing -_-'
    
    return 'I don\'t understand that.'

async def handle_message(update: Update, context) -> None:
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

async def error(update: Update, context) -> None:
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', three_steps.start_command),
                      CommandHandler('help', help_command),
                      CommandHandler('custom', custom_command),
                      CommandHandler('sendbuttons', send_buttons)],
        states={
            three_steps.FIRST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, three_steps.set_first_name)],
            three_steps.LAST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, three_steps.set_last_name)],
            three_steps.AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, three_steps.set_age)],
        },
        fallbacks=[],
    )

    # Commands
    app.add_handler(conv_handler)

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error handler
    app.add_error_handler(error)

    # Start polling
    print('Polling...')
    app.run_polling(poll_interval=3)

