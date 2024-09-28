import telebot # библиотека telebot
from confik import token # импорт токена

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом.")

@bot.message_handler(func=lambda message: True)  
def ban_and_kick_user(message):
    if message.text.startswith('https://') == True:
        chat_id = message.chat.id # сохранение id чата
            # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
            # проверка пользователя
        if user_status != 'administrator' or user_status != 'creator':
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
             
    if message.text.startswith('Я не хочу здесь находиться') == True:
        chat_id = message.chat.id # сохранение id чата
            # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
            # проверка пользователя
        if user_status != 'administrator' or user_status != 'creator':
            bot.kick_chat_member(chat_id, user_id) # пользователь с user_id будет выгнан в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был выгнан.")
            
@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)  

bot.infinity_polling(none_stop=True)
