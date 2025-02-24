import telebot
import os
import re

API_ID = os.getenv("API_ID", "25579552")
API_HASH = os.getenv("API_HASH", "ac24e438ff9a0f600cf3283e6d60b1aa")
TOKEN = os.getenv("BOT_TOKEN", "746000087")

bot = telebot.TeleBot(TOKEN)


# Function to extract URLs from text
def extract_links(content):
    pattern = re.compile(r'(.+?):(https?://\S+)')
    return pattern.findall(content)

# Function to convert TXT to HTML with extracted links
def txt_to_html(txt_path, html_path):
    file_name = os.path.basename(txt_path).replace('.txt', '')
    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()
    
    # Extract links from text
    links = extract_links(content)

    # Format links as HTML rows
    link_rows = "".join([
        f"<tr><td>{name}</td><td><a href='{url}' target='_blank'>Click to View</a></td></tr>" 
        for name, url in links
    ])
    
    html_content = f"""
    <!doctype html>
    <html>
    <head>
        <link rel='preconnect' href='https://fonts.googleapis.com'>
        <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>
        <link href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap' rel='stylesheet'>
        <meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5' name='viewport'>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>{file_name}</title>
        <style>
            body {{margin: 0;font-family: 'Poppins', sans-serif;}}
            table {{word-break: break-word;border-collapse: collapse;width: 100%;}}
            summary {{font-weight: 600;text-align: center;padding: 14px;background-color: #0f0120;color: #ffffff;font-size: 18px;list-style: none;border-radius: 50px;margin: 3px;}}
            td {{font-size: 13px;padding: 13px;width: 50%;}}
            a {{text-decoration: none;}}
            h1 {{color: rgb(248, 123, 6);text-align: center;font-size: 25px;}}
            tr:nth-child(even) {{background-color: #f2f2f2;}}
            .header {{display: flex;align-items: center;padding: 10px;background-color: #f8f9fa;}}
            .header img {{width: 20px;margin-right: 10px;}}
            .header a {{text-decoration: none;color: #007bff;font-weight: 600;margin-right: 20px;}}
            .footer {{text-align: center;margin-top: 20px;}}
            .footer-text {{font-size: 15px;font-weight: bold;background: linear-gradient(to right, #f5f37a, #f1c480)}}
        </style>
    </head>
    <body>
        <div class='header'>
            <a href='https://t.me/save_restricted_botss' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Channel'>
                Telegram Channel
            </a>
            <a href='https://t.me/defencecornor' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Main Channel'>
                Telegram Main
            </a>
            <a href='https://telegram.dog/TalkwithSupport_bot' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Username'>
                Telegram Username
            </a>
        </div>
        <pre>
            <img src='https://i.ibb.co/23h0XKRF/max.jpg' height='150'/>
        </pre>
        <h1>krēˈādər</h1>
        <details>
            <summary><p>{file_name}</p></summary>
            <table>
                {link_rows}
            </table>
            <h3>THANK YOU</h3>
            <h4>Contact with us in <a href='https://telegram.dog/TalkwithSupport_bot'>
                <br/>
                krēˈādər</a>
                <br/>
                in TELEGRAM.</h4>
        </details>
        <div class='footer'>
            <div class='footer-text'>
                Developed By: krēˈādər
            </div>
        </div>
    </body>
    </html>
    """
    
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# Telegram bot handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg',
                   caption='Welcome to the TXT to HTML Converter Bot!\nSend a .txt file, and I will convert it into an HTML file with clickable links.')

# Telegram bot handler
@bot.message_handler(content_types=['document'])
def handle_txt_file(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)

    # Extract the original file name
    original_file_name = message.document.file_name
    file_name_without_ext = os.path.splitext(original_file_name)[0]  # Remove .txt extension

    txt_path = f"{file_name_without_ext}.txt"
    html_path = f"{file_name_without_ext}.html"  # Ensure it's a valid string

    downloaded_file = bot.download_file(file_info.file_path)

    with open(txt_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Call the conversion function with correct string paths
    txt_to_html(txt_path, html_path)

    with open(html_path, 'rb') as html_file:
        bot.send_document(message.chat.id, html_file)

    os.remove(txt_path)
    os.remove(html_path)

bot.polling()



