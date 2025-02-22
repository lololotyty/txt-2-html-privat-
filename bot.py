import telebot
import os

API_ID = os.getenv("API_ID", "ac24e438ff9a0f600cf3283e6d60b1aa")
API_HASH = os.getenv("API_HASH", "25579552")
TOKEN = os.getenv("BOT_TOKEN", "7548242755:AAGiLXS6Qc2ZCPksD73t7yVlPKeFi4w86gM")


bot = telebot.TeleBot(TOKEN)

# Function to convert TXT to HTML
def txt_to_html(txt_path, html_path):
    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()
    
    html_content = f"""
    <!doctype html>
    <html>
    <head>
        <link rel='preconnect' href='https://fonts.googleapis.com'>
        <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>
        <link href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap' rel='stylesheet'>
        <meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5' name='viewport'>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>{title}</title>
        <style>
            body {margin: 0;font-family: 'Poppins', sans-serif;}
            table {word-break: break-word;border-collapse: collapse;width: 100%;}
            summary {font-weight: 600;text-align: center;padding: 14px;background-color: #0f0120;color: #ffffff;font-size: 18px;list-style: none;border-radius: 50px;margin: 3px;}
            td {font-size: 13px;padding: 13px;width: 50%;}
            a {text-decoration: none;}
            h1 {color: rgb(248, 123, 6);text-align: center;font-size: 25px;}
            tr:nth-child(even) {background-color: #f2f2f2;}
            .header {display: flex;align-items: center;padding: 10px;background-color: #f8f9fa;}
            .header img {width: 20px;margin-right: 10px;}
            .header a {text-decoration: none;color: #007bff;font-weight: 600;margin-right: 20px;}
            .footer {text-align: center;margin-top: 20px;}
            .footer-text {font-size: 15px;font-weight: bold;background: linear-gradient(to right, #f5f37a, #f1c480)}
        </style>
    </head>
    <body>
        <div class='header'>
            <a href='https://t.me/+2cOj_hKs64o0NDRl' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Channel'>
                Telegram Channel
            </a>
            <a href='https://telegram.me/I_AJPYTHON' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Username'>
                Telegram Username
            </a>
            <a href='https://whatsapp.com/channel/0029Vac9SnM6BIElqk2pMm2q' target='_blank'>
                <img src='https://graph.org/file/da84b2d7c1a5c958163b6.jpg' height='20'/>
                Whatsapp Channel
            </a>
        </div>
        <pre>
            <img src='https://graph.org/file/45f9bf5a52c6d7309253f.jpg' height='150'/>
        </pre>
        <h1>AIMERS ❤</h1>
        <details>
            <summary><p>OPEN</p></summary>
            <table>
                <tr>
                    <td>Updated Sankalp Batch Time - Table</td>
                    <td><a href='https://appxcontent-mcdn.akamai.net.in/paid_course4/2024-05-03-0.04502875872610956.pdf'>Click to View</a></td>
                </tr>
            </table>
            <h3>THANK YOU</h3>
            <h4>Contact with us in <a href='http://telegram.me/allaimers_bot'>
                <br/>
                AIMERS OFFICIAL BOT</a>
                <br/>
                in TELEGRAM.</h4>
        </details>
        <div class='footer'>
            <div class='footer-text'>
                Developed By: ＡＪ_ＰＹＴＨＯＮ
            </div>
        </div>
    </body>
    </html>
    """
    
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# Telegram bot handler
@bot.message_handler(content_types=['document'])
def handle_txt_file(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    txt_path = "input.txt"
    html_path = "output.html"
    
    with open(txt_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    txt_to_html(txt_path, html_path)
    
    with open(html_path, 'rb') as html_file:
        bot.send_document(message.chat.id, html_file)
    
    os.remove(txt_path)
    os.remove(html_path)

bot.polling()

