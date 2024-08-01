from telegram import Bot

# Replace with your bot's token and the chat ID
BOT_TOKEN = '7189362950:AAEVLyD0cHA-Mrzi5YbeJxf81GfDMiybm10'
CHAT_ID = 'manish'  # For example, a chat ID or a group ID

bot = Bot(token=BOT_TOKEN)

# Send a message
bot.send_message(chat_id=CHAT_ID, text="Hello!")
