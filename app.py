from flask import Flask, request

# PLAYERS
from my_bot import get_bet

app = Flask(__name__)


@app.route("/bet", methods=['POST'])
def get_bot():

    return '0'  # str(get_bet(request.json))
