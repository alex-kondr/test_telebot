import time

from telebot import TeleBot, types

from config import settings


bot = TeleBot(settings.token_telegram)
# bot.set_webhook()


# The `users` variable is needed to contain chat ids that are either in the search or in the active dialog, like {chat_id, chat_id}
# users = {}
# The `freeid` variable is needed to contain chat id, that want to start conversation
# Or, in other words: chat id of user in the search
# freeid = None

# `/start` command handler
#
# That command only sends you 'Just use /find command!'
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    print(message.chat.id)
    print(message.chat.first_name)
    print(message.chat.last_name)
    print(message.sticker)
    print(message.text)
    
    bot.send_message(message.chat.id, "Перевіряю чи ти не заблокований ☠ ....")
    time.sleep(5)    
    
    if message.chat.id == 1906752116:    
        bot.send_message(message.chat.id, "Кохана, тебе заблокувати не можливо. Надішли будь який анімований стікер 💋")
    else:
        bot.send_message(message.chat.id, "Сестро, це ти?")
        # bot.send_message(message.chat.id, "Ти заблокований ☠")
        # bot.send_message(message.chat.id, "☠")
    

# message handler for conversation
#
# That handler needed to send message from one opponent to another
# If you are not in `users`, you will recieve a message 'No one can hear you...'
# Otherwise all your messages are sent to your opponent
#
# Questions:
# 1. Is there any way to improve readability like `content_types=['all']`?
# 2. Is there any way to register this message handler only when i found the opponent?



@bot.message_handler(content_types=['sticker'])
def chatting(message: types.Message):
    print(message.chat.id)
    print(message.chat.first_name)
    print(message.chat.last_name)
    print(message.sticker)
    
    # bot.send_message(1110407897, message.text)
    bot.send_sticker(1110407897, message.sticker.file_id)
    
    
#         # bot.send_message(message.chat.id, "Ну привіт")
#     # bot.copy_message(1110407897, message.chat.id, 109)
#     # bot.send_sticker(1110407897, emoji='👍', sticker="CAACAgIAAxkBAAIBIGRQ99Wl5vvem4gwL6-9lGuwKHpYAAIEEQAC-rKoS3YUy5_7sD-iLwQ")
    
#     # message
    
    if message.chat.id == 1906752116:    
        bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAIBIGRQ99Wl5vvem4gwL6-9lGuwKHpYAAIEEQAC-rKoS3YUy5_7sD-iLwQ")
    else:
        bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAIBZmRRBxRnNBGLYMNzKK9Ra6ag8ZW0AAJwDAACDzUgS0IGOplsVK2mLwQ")
    # print(json.dumps(message.text))
    # with open("test.txt", "w", encoding="utf-8") as fd:
    #     json.
    # bot.copy_message
    # bot.send_message(1906752116, "🥰")
    

# @bot.message_handler(commands=['hi'])
# def send_mes(message: types.Message):
#     print(message.chat.id)
#     print(message.text)
    
    
#     bot.send_message(1110407897, message.text)

@bot.message_handler(content_types=['animation', 'audio', 'contact', 'dice', 'document', 'location', 'photo', 'poll', 'sticker', 'text', 'venue', 'video', 'video_note', 'voice'])
def chatting(message: types.Message):
    print(message.chat.id)
    print(message.chat.first_name)
    print(message.chat.last_name)
    print(message.text)
    print(message.animation)
    
    if message.content_type == "text":    
        bot.send_message(1110407897, message.text)
    elif message.content_type == "animation": 
        bot.send_animation(1110407897, message.animation.file_id)
    
    # CgACAgQAAxkBAAIBXWRRBaxjKV1l1H9Xi7-ASEygQpcPAALDAgACWZkMU1eJcxRQ5_sGLwQ
    
    if message.text.lower() == "так":
        bot.send_message(message.chat.id, "Тобі тут не місце")
        bot.send_message(message.chat.id, "Це тобі в прикуску ->")
        bot.send_animation(message.chat.id, "CgACAgQAAxkBAAIBXWRRBaxjKV1l1H9Xi7-ASEygQpcPAALDAgACWZkMU1eJcxRQ5_sGLwQ")
        bot.send_message(message.chat.id, "Надішли анімований стікер")
    elif message.text.lower() == "ні":
        bot.send_message(message.chat.id, "Не обманюй")
        bot.send_message(message.chat.id, "Це тобі в прикуску ->")
        bot.send_animation(message.chat.id, "CgACAgQAAxkBAAIBXWRRBaxjKV1l1H9Xi7-ASEygQpcPAALDAgACWZkMU1eJcxRQ5_sGLwQ")
        bot.send_message(message.chat.id, "Надішли анімований стікер")
    else:
        bot.send_message(message.chat.id, "Введи щось путнє")
        bot.send_message(5146491788, "Ото цяця...🤡")
        
    
    
    


if __name__ == "__main__":
    bot.infinity_polling()