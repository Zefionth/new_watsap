from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from handlers import start, handle_message, button
from config import TELEGRAM_TOKEN

# основная функция для запуска бота
def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button, pattern="next"))

    # запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
