import os
import telebot
from telebot.types import InputFile
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_ID = os.getenv("API_ID", "ac24e438ff9a0f600cf3283e6d60b1aa")
API_HASH = os.getenv("API_HASH", "25579552")
TOKEN = os.getenv("BOT_TOKEN", "7548242755:AAGiLXS6Qc2ZCPksD73t7yVlPKeFi4w86gM")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.document.mime_type != "text/plain":
        bot.reply_to(message, "Please upload a valid .txt file.")
        return

    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    txt_filename = message.document.file_name
    html_filename = txt_filename.replace('.txt', '.html')

    # Save .txt file
    with open(txt_filename, "wb") as f:
        f.write(downloaded_file)

    # Convert to .html
    with open(txt_filename, "r", encoding="utf-8") as txt_file, open(html_filename, "w", encoding="utf-8") as html_file:
        html_file.write("<html><body><pre>\n")
        html_file.write(txt_file.read())
        html_file.write("\n</pre></body></html>")

    # Send back the .html file
    with open(html_filename, "rb") as html_file:
        bot.send_document(message.chat.id, InputFile(html_file))

    # Cleanup
    os.remove(txt_filename)
    os.remove(html_filename)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Send me a .txt file, and I'll convert it to .html for you.")

print("Bot is running...")
bot.polling()
