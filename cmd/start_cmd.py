def start_cmd(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! This is the start command.")
