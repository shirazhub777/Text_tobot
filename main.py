
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import pytesseract
import tempfile

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("سلام! 👋 عکس بفرست تا متنت رو استخراج کنم.
برای VIP: /buy")

def buy(update, context):
    update.message.reply_text("برای خرید VIP یا اطلاعات بیشتر روی لینک زیر بزنید:
https://t.me/text_tomebot")

def handle_photo(update, context):
    user_id = update.message.from_user.id
    file = context.bot.getFile(update.message.photo[-1].file_id)
    with tempfile.NamedTemporaryFile(delete=True) as tf:
        file.download(custom_path=tf.name)
        text = pytesseract.image_to_string(Image.open(tf.name))
        update.message.reply_text(f"📄 متن استخراج‌شده:
{text[:4096]}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
