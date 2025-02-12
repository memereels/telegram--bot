from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import random
import threading
import time
import os

# ✅ Bot Token
BOT_TOKEN = '8064010533:AAHvbYSVOnOlJPznMQ13LaeT3zc6yFZrAos'
bot = Bot(token=BOT_TOKEN)

# ✅ Flask App Initialization
app = Flask(__name__)

# ✅ Channel Username
CHANNEL_USERNAME = '@kyahalhaibhai'

# ✅ Sample Video Links
videos = [
    'https://t.me/kyahalhaibhai/1',
    'https://t.me/kyahalhaibhai/2',
    'https://t.me/kyahalhaibhai/3'
]

# ✅ Start Command Handler
def start(update, context):
    update.message.reply_text("Welcome! Type /getvideo to receive a random video.")

# ✅ Get Video Command Handler
def get_video(update, context):
    video_link = random.choice(videos)
    message = update.message.reply_text(f"Here's your video: {video_link}")

    # ✅ Auto-delete after 15 minutes
    def delete_message():
        time.sleep(900)  # 900 seconds = 15 minutes
        try:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message.message_id)
        except:
            pass

    threading.Thread(target=delete_message).start()

# ✅ Dispatcher for Handling Commands
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("getvideo", get_video))

# ✅ Webhook for Telegram
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# ✅ Server Run on Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
