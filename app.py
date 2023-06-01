from flask import Flask, request
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import telegram
from handlers import start, text
TOKEN = "2116227480:AAFHmVr3wHV2EVLcpWKk5nQtFQ8pW3Xtq18"

bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route("/webhook", methods= ["POST", "GET"])
def webhok():
    if request.method == "POST":
        dp = Dispatcher(bot, None, workers=4)

        data = request.get_json(force=True)
        update = Update.de_json(data, bot)

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text, text))

        dp.process_update(update)

        return "ok"
    else:
        return "Not allowed get request"
    
if __name__ == "__main__":
    app.run(debug=True)