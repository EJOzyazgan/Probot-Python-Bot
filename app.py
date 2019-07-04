from flask import Flask, request

# PLAYERS
from my_bot import get_bet

app = Flask(__name__)


@app.route("/bet", methods=['POST'])
def get_bot():
    print(request.json)
    return str(get_bet(request.json))
