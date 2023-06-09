from telegram.ext import Updater, CommandHandler
import os

def main():
    # Create the bot and start the updater
    updater = Updater(token="6298316109:AAFAXuonPlRaY-jmJZInN5orW4iiB5nHyAM", use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers dynamically from the `/cmd` folder
    cmd_folder = "./cmd"
    for filename in os.listdir(cmd_folder):
        if filename.endswith("_cmd.py"):
            module_name = os.path.splitext(filename)[0]
            module = __import__(f"cmd.{module_name}", fromlist=[module_name])
            command_handler = getattr(module, module_name)
            dispatcher.add_handler(CommandHandler(module_name, command_handler))

    # Start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()
