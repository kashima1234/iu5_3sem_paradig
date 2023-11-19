
from typing import Final
from telegram import Update,  InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

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


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error handler
    app.add_error_handler(error)

    # Start polling
    print('Polling...')
    app.run_polling(poll_interval=3)








# import pytesseract
# import cv2
# from telegram.ext import Updater, MessageHandler, filters, CommandHandler, CallbackContext
# from telegram import Update

# # Set the path to the Tesseract OCR executable
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Привет! Отправьте мне изображение для распознавания текста.")

# def convert_image_to_text(update: Update, context: CallbackContext) -> None:
#     photo = context.bot.getFile(update.message.photo[-1].file_id)
#     photo.download('image.jpg')

#     image = cv2.imread('image.jpg')
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     text = pytesseract.image_to_string(gray_image)

#     update.message.reply_text(f"Распознанный текст: \n{text}")

# def main() -> None:
#     updater = Updater('6945576738:AAF0qdI6CL4MGYJmKEHgulKjndUiH2DkbWw')
#     dispatcher = updater.dispatcher

#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(MessageHandler(filters.photo & ~filters.command, convert_image_to_text))

#     updater.start_polling()
#     updater.idle()def main() -> None:
#     updater = Updater("YOUR_BOT_TOKEN")

#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher

#     # Register command and message handlers
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, convert_image_to_text))

#     # Start the Bot
#     updater.start_polling()

#     # Run the bot until you press Ctrl-C
#     updater.idle()

# if __name__ == '__main__':
#     main()

# if __name__ == '__main__':
#     main()







# from typing import Final
# from telegram import Update
# from telegram.ext import Application, ContextTypes, MessageHandler, filters, ContextTypes




# TOKEN: Final = '6945576738:AAF0qdI6CL4MGYJmKEHgulKjndUiH2DkbWw'

# BOT_USERNAME: Final = '@Kashimaahmed_bot'


# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello, Thank you ma nigga')


# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
#     await update.message.reply_text('Hello, Thank you ma nigga')


# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello, Thank you ma nigga')





# def handle_response(text: str) ->str:
#     processed: str = text.lower()

#     if 'hello' in text:
#         return 'yooo wassup nigga'
    
#     if 'how are you ' in text:
#         return 'im fine '
#     if 'I love you ':
#         return 'i love you tooooo'
    



# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type


#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
          

#     if message_type == 'group':
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME, '').strip()
#             response: str = handle_response(new_text)
#         else:
#             return
#     else:
#         response: str = handle_response(text)

#         print('Bot:', response)
#         await update.messapge.reply_text(response)

# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):

#     print(f'Update {update} caused error{context.error}')



# if __name__ == '__main__':
#     app = Application.builder().token(TOKEN).build()


#     #commands

#     app.add_handler(CommandHandler('star', start_command))
#     app.add_handler(CommandHandler('help', help_command))
#     app.add_handler(CommandHandler('custom', custom_command))

#     #messages
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     #error
#     app.add_error_handler(error)

#     #polls the bot 
#     print('Poling...')
#     app.run_polling(poll_interval=3)





# from typing import Final
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# TOKEN: Final = '6945576738:AAF0qdI6CL4MGYJmKEHgulKjndUiH2DkbWw'
# BOT_USERNAME: Final = '@Kashimaahmed_bot'

# # Your other functions (start_command, help_command, custom_command, handle_response, handle_message, error) here...

# def send_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [[InlineKeyboardButton("Кнопка 1", callback_data='button1'),
#                  InlineKeyboardButton("Кнопка 2", callback_data='button2')]]

#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)


#     async def start_command(update: Update, context) -> None:
#        await update.message.reply_text('Hello, thank you!')


#     async def help_command(update: Update, context) -> None:
#         await update.message.reply_text('Help command is not implemented yet.')


#     async def custom_command(update: Update, context) -> None:
#         await update.message.reply_text('Custom command is not implemented yet.')


# if __name__ == '__main__':
#     app = Application.builder().token(TOKEN).build()

#     # Commands
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(CommandHandler('help', help_command))
#     app.add_handler(CommandHandler('custom', custom_command))
#     app.add_handler(CommandHandler('buttons', send_buttons))

#     # Messages
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     # Error handler
#     app.add_error_handler(error)

#     # Start polling
#     print('Polling...')
#     app.run_polling(poll_interval=3)
