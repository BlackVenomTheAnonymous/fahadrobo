def start(update, context):
    message = "Hello! Welcome to the bot. How can I assist you today?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
