from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from handlers import start, handle_message, button
from config import TELEGRAM_TOKEN

# Основная функция для запуска бота
def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Обработчики
    application.add_handler(CommandHandler("start", start))  # Команда /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Текстовые сообщения
    application.add_handler(CallbackQueryHandler(button))  # Все нажатия на кнопки, включая "Next"

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
