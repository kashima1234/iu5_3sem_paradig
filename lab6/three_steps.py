import asyncio

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes

FIRST_NAME, LAST_NAME, AGE = range(3)

# Dictionary to store user information
user_info = {}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in user_info:
        user_info[user_id] = {}

    await update.message.reply_text('Welcome! Please provide your first name.')

    # Set the state to FIRST_NAME
    return FIRST_NAME

async def set_first_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_info[user_id]['first_name'] = update.message.text

    await update.message.reply_text(f"Great, {user_info[user_id]['first_name']}! Now, please provide your last name.")

    # Set the state to LAST_NAME
    return LAST_NAME

async def set_last_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_info[user_id]['last_name'] = update.message.text

    await update.message.reply_text(f"Excellent, {user_info[user_id]['first_name']} {user_info[user_id]['last_name']}! "
                                    "Finally, please provide your age.")

    # Set the state to AGE
    return AGE

async def set_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    try:
        user_info[user_id]['age'] = int(update.message.text)
        await update.message.reply_text('Thank you! Here is the information you provided:\n'
                                        f"First Name: {user_info[user_id]['first_name']}\n"
                                        f"Last Name: {user_info[user_id]['last_name']}\n"
                                        f"Age: {user_info[user_id]['age']}")
    except ValueError:
        await update.message.reply_text('Please provide a valid age. Please start the process again with /start.')

    # End the conversation
    return ConversationHandler.END
