from telegram import Update
from telegram.ext import CallbackContext
from recommendations import get_recommendations

# функция для старта бота
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Напиши краткое описание того, что ты хочешь посмотреть, и я подберу фильм.')

# функция обработки сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Ваш запрос обрабатывается")
    
    query = update.message.text
    recommendations = get_recommendations(query)
    
    if recommendations:
        await update.message.reply_text(f"Вот несколько фильмов, которые могут вам понравиться:\n{recommendations}")
    else:
        await update.message.reply_text("Извините, я не смог найти подходящих фильмов. Попробуйте описать запрос по-другому.")
