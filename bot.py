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

# HTML Template for better readability
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 20px;
            background-color: #f4f4f4;
        }}
        .container {{
            max-width: 800px;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            white-space: pre-wrap;
        }}
        h2 {{
            text-align: center;
            color: #333;
        }}
        .download {{
            text-align: center;
            margin-top: 20px;
        }}
        .download a {{
            text-decoration: none;
            background: #28a745;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>{title}</h2>
        <pre>{content}</pre>
    </div>
</body>
</html>
"""

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "📜 Send me a .txt file, and I'll return it as a readable HTML page.")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.document.mime_type != "text/plain":
        bot.reply_to(message, "❌ Please upload a valid .txt file.")
        return

    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    txt_filename = message.document.file_name
    html_filename = txt_filename.replace('.txt', '.html')

    # Save .txt file
    with open(txt_filename, "wb") as f:
        f.write(downloaded_file)

    # Read .txt file and format as HTML
    with open(txt_filename, "r", encoding="utf-8") as txt_file:
        text_content = txt_file.read()

    # Preserve text formatting with <pre> tags
    html_content = HTML_TEMPLATE.format(title=txt_filename, content=text_content)

    # Save as HTML file
    with open(html_filename, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    # Send back the .html file
    with open(html_filename, "rb") as html_file:
        bot.send_document(message.chat.id, InputFile(html_file))

    # Cleanup
    os.remove(txt_filename)
    os.remove(html_filename)

print("Bot is running...")
bot.polling()

