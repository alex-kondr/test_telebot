from flask import Flask
from teleflask import Teleflask
from config import settings

app = Flask(__name__)
bot = Teleflask(settings.token_telegram)
bot.init_app(app)

app.run("localhost", 8080, debug=True)