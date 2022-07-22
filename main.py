from telegram import *
from telegram.ext import *
import requests
from bs4 import BeautifulSoup as bs

import logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

updater = Updater(token="5441032198:AAF6vVRrvbUTLRvLfr76-fMuZfTaV8ftbUo")



allowedUsernames = ['vonikreus']


def start(update: Update, context: CallbackContext):
    user = update.effective_user['first_name']
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Assalom alleykum, xush kelibsiz {user}!, @bajarildibot yordamida chiqaring!")

def get(update: Update, context: CallbackContext):
    URL = f"https://asaxiy.uz/product?key={update.message.text}"
    bot = requests.get(URL)
    soup = bs(bot.content, "html.parser")

    searches = soup.find_all("div", class_="col-6 col-xl-3 col-md-4")
    # print(searches)
    for search in searches:
        print(searches)
        title = search.find("div", class_="product__item d-flex flex-column justify-content-between").find("div", class_ = "product__item-info").find("a").text
        image = search.find("div", class_="product__item d-flex flex-column justify-content-between").find("div", class_ = "product__item-img").find("img")["data-src"]
        # image = search.find("div", class_="product__item-img").find("img")
        # size = len(image["data-src"])
        # if image['data-src'][size - 5:] == ".webp":
        #     url = image['data-src'][:size - 5]
        # else:
        #     url = image['data-src']
        content = search.find("div", class_="product__item d-flex flex-column justify-content-between").find("div",class_="product__item-info").find("div", class_="product__item-info--prices").text
        # print(title)
        update.message.reply_text(f"{title}{image}{content}")





dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get))


updater.start_polling()
updater.idle()
