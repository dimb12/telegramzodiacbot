import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я расскажу какой прогноз ждет твой знак зодиака. Введите свой знак зодиака.")

def echo(update, context):
    sign = update.message.text.lower()
    folder_path = os.path.join('predictions', sign.capitalize())
    
    if os.path.exists(folder_path):
        file_path = os.path.join(folder_path, 'текст.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                text = file.read()
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Нет информации для данного знака зодиака.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Неправильный знак зодиака.")

def main():
    updater = Updater(token='5853736823:AAHbtSu5hdJlVzhefshEZAvPJTOxXF73Gm8', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
