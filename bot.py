from telegram import Bot
from telegram.ext import Updater, CommandHandler
import random
import time
import threading

# Telegram Bot Token
BOT_TOKEN = '8064010533:AAHvbYSVOnOlJPznMQ13LaeT3zc6yFZrAos'

# Channel username jahan videos hain
CHANNEL_USERNAME = '@kyahalhaibhai'

# Video list (apne actual video links yahan add karo)
videos = [
    'https://t.me/kyahalhaibhai/1',
    'https://t.me/kyahalhaibhai/2',
    'https://t.me/kyahalhaibhai/3'
]

# Bot ke functions
def start(update, context):
    update.message.reply_text("Welcome! Type 'get video' to receive a random video.")

def get_video(update, context):
    video_link = random.choice(videos)
    message = update.message.reply_text(f"Here's your video: {video_link}")
    
    # 15 minute baad message delete karne ka function
    def delete_message():
        time.sleep(900)  # 900 seconds = 15 minutes
        try:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message.message_id)
        except:
            pass
    
    threading.Thread(target=delete_message).start()

# Main function
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("getvideo", get_video))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
