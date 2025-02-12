from flask import Flask, request
import telegram
import os
import random

TOKEN = "8064010533:AAHvbYSVOnOlJPznMQ13LaeT3zc6yFZrAos"
CHANNEL_USERNAME = "@kyahalhaibhai"  # Aapka channel name

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# Function to send random video from the channel
def send_random_video(chat_id):
    try:
        # Fetch the latest 100 messages from the channel
        updates = bot.get_chat(CHANNEL_USERNAME).get_history(limit=100)

        # Filter only video messages
        videos = [msg for msg in updates if msg.video]

        if videos:
            random_video = random.choice(videos)
            bot.send_video(chat_id=chat_id, video=random_video.video.file_id)
        else:
            bot.send_message(chat_id=chat_id, text="No videos found in the channel.")
    except Exception as e:
        bot.send_message(chat_id=chat_id, text=f"Error: {e}")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    if message == '/start':
        bot.send_message(chat_id=chat_id, text="Welcome to the bot!")
    elif message == '/getvideo':
        send_random_video(chat_id)
    else:
        bot.send_message(chat_id=chat_id, text="Invalid command. Use /getvideo to get a video.")

    return 'ok'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
