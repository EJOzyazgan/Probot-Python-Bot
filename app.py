from flask import Flask, request
import json

import my_bot

app = Flask(__name__)


@app.route("/bet", methods=['POST'])
def get_bet():
    return json.dumps(my_bot.bet(request.json))
