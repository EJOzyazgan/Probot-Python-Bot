from flask import Flask, request
import json

from .my_bot import bet

app = Flask(__name__)


@app.route("/bet", methods=['POST'])
def get_bet():
    return json.dumps(get_bet(request.json))
