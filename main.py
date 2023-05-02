# -*- coding: utf-8 -*-
from flask import Flask
from teleflask import Teleflask
from teleflask.messages import PlainMessage, HTMLMessage

from config import settings


# @djsahbok
# print(settings.token_telegram)

# Just set API_KEY = "your-api-key".
app = Flask(__name__)
bot = Teleflask(settings.token_telegram)
bot.init_app(app)

print("me")
print(bot.bot.get_me())


@app.route("/")
def index():
    return "This is a normal Flask page."
# end def


# Register the /start command
@bot.command("start")
def start(update, text):
    # update is the update object. It is of type pytgbot.api_types.receivable.updates.Update
    # text is the text after the command. Can be empty. Type is str.
    return HTMLMessage("<b>Hello!</b> Thanks for using @" + app.username + "!")
    # return TextMessage("<b>Hello!</b> Thanks for using @" + app.username + "!", parse_mode="html")
# end def


# register a function to be called for updates.
@bot.on_update
def foo(update):
    from pytgbot.api_types.receivable.updates import Update
    assert isinstance(update, Update)
    # do stuff with the update
    # you can use app.bot to access the bot's messages functions
    if not update.message:
        return
        # you could use @app.on_message instead of this if.
    # end if
    if update.message.new_chat_member:
        return PlainMessage("Welcome!")
        # return TextMessage("Welcome!", parse_mode="text")


if __name__ == "__main__":  # no nginx
    # "__main__" means, this python file is called directly.
    # not to be confused with "main" (because main.py) when called from from nginx
    app.run(host='0.0.0.0', debug=True, port=5000) 