from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random  # Import the random module

TOKEN: Final = '6945576738:AAF0qdI6CL4MGYJmKEHgulKjndUiH2DkbWw'
BOT_USERNAME: Final = '@Kashimaahmed_bot'

async def start_command(update: Update, context) -> None:
    await update.message.reply_text('Hello, thank you!')

async def help_command(update: Update, context) -> None:
    await update.message.reply_text('Help command is not implemented yet.')

async def custom_command(update: Update, context) -> None:
    await update.message.reply_text('Custom command is not implemented yet.')

def send_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Кнопка 1", callback_data='button1'),
                 InlineKeyboardButton("Кнопка 2", callback_data='button2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

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

# Define a list of picture URLs
picture_urls = [
    'https://example.com/picture1.jpg',
    'https://example.com/picture2.jpg',
    'https://example.com/picture3.jpg',
    # Add more picture URLs as needed
]

async def send_random_picture(update: Update, context) -> None:
    # Get a random picture URL from the list
    random_picture_url = random.choice(picture_urls)

    # Send the picture to the chat
    update.message.reply_photo(photo=random_picture_url)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('randompicture', send_random_picture))  # Added the new command handler

    # Add message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Add error handler
    # app.add_handler(MessageHandler(filters.ERROR, error))
   # app.add_handler(MessageHandler(filters.ERROR, error))
    app.add_error_handler(error)

    print('Polling...')
    
    app.run_polling()

