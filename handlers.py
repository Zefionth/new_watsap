from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from recommendations import get_recommendations

# Функция для старта бота
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Привет! Напиши краткое описание того, что ты хочешь посмотреть, и я подберу фильм.'
    )

# Функция обработки сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Ваш запрос обрабатывается")
    
    query = update.message.text
    recommendations = get_recommendations(query)
    
    if recommendations:
        context.user_data['recommendations'] = recommendations
        context.user_data['current_index'] = 0  # Начальный индекс
        await send_recommendation(update.message, context)
    else:
        await update.message.reply_text("Извините, я не смог найти подходящих фильмов. Попробуйте описать запрос по-другому.")

# Функция для отправки текущей рекомендации
async def send_recommendation(message, context: CallbackContext) -> None:
    current_index = context.user_data['current_index']
    recommendations = context.user_data['recommendations']
    
    # Проверка, есть ли еще рекомендации
    if current_index < len(recommendations):
        item = recommendations[current_index]
        keyboard = [[InlineKeyboardButton("Далее", callback_data="next")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await message.reply_text(f"{item}", reply_markup=reply_markup)
    else:
        await message.reply_text("Больше рекомендаций нет. Можете попробовать написать запрос по-другому.")

# Обработчик для кнопки "Далее"
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    # Увеличиваем индекс и отправляем следующую рекомендацию
    context.user_data['current_index'] += 1
    await send_recommendation(query.message, context)
