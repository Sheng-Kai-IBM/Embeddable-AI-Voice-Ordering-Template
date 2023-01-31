from helperFunctions import *
from flask import Flask, render_template, request, flash, redirect, Response, url_for

app = Flask(__name__)
language, raw_address, customer_address, raw_order, pizza_size, pizza_topping, play_audio = None, None, None, None, None, None, None


def root():
    # TODO


def get_info():
    # TODO


def get_topping():
    # TODO


def get_info_redirect():
    # TODO


def get_topping_redirect():
    # TODO


def get_order():
    # TODO


def get_info_record_wav():
    # TODO


def get_topping_record_wav():
    # TODO


@app.route("/play_local_wav")
def play_local_wav():
    return Response(play_local_wav_file(play_audio), mimetype="audio/x-wav")


if __name__ == "__main__":
    
    app.run(debug=False, use_reloader=True, port=8080, host="0.0.0.0")
