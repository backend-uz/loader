from telegram import Update, InputMediaVideo, InputMediaPhoto
from db import slider, reel, getBasicInfo


def start(update, context):
    bot = context.bot 
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, "Send me an instagram media link")


def text(update, context):
    bot = context.bot
    chat_id = update.message.chat.id
    text = update.message.text
    if text.startswith('https://www.instagram.com/'):
        if '/reel' in text:
            url = reel(text)
            bot.send_video(chat_id, url)

        elif '/p/' in text:
            url = slider(text)
            if len(url) > 1:
                media = []
                for i in url:

                    if '.mp4' in i:
                        media.append(InputMediaVideo(i))
                    else:
                        media.append(InputMediaPhoto(i))
                bot.send_media_group(chat_id, media)
            else:
                bot.send_photo(chat_id, url)
    else:
        account = getBasicInfo(text)
        bot.send_photo(chat_id=chat_id, photo=account[1], caption=account[0])

def profile(update, context):
    bot = context.bot
    chat_id = update.message.chat.id
    text = update.message.text
    if 'https://' not in text:
        account = getBasicInfo(text)
        bot.send_photo(chat_id=chat_id, image=account[1], caption=account[0])
