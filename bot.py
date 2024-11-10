from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import start, handle_message
from config import TELEGRAM_TOKEN

# основная функция для запуска бота
def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
