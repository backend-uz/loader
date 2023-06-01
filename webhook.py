import telegram

TOKEN="2116227480:AAFHmVr3wHV2EVLcpWKk5nQtFQ8pW3Xtq18"
url = "https://cajiv.pythonanywhere.com/webhook"
bot = telegram.Bot(TOKEN)

# print(bot.delete_webhook())

print(bot.set_webhook(url))
print(bot.get_webhook_info())