from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from handlers import start, handle_message, button
from config import TELEGRAM_TOKEN

def main() -> None:
    """Запускает Telegram-бота."""
    # Создаем экземпляр приложения с токеном бота
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрация обработчиков команд и сообщений
    application.add_handler(CommandHandler("start", start))  # Обработка команды /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Обработка текстовых сообщений
    application.add_handler(CallbackQueryHandler(button))  # Обработка нажатий на кнопки

    # Запуск бота в режиме опроса (polling)
    application.run_polling()

if __name__ == '__main__':
    main()
