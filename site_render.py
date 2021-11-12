from flask import Flask, render_template, request
from threading import Thread

from flask.helpers import url_for
from stats_getter import stats_getter

app = Flask('')


@app.route(url_for('index.html'))
def home():
    return render_template("index.html")


def run():
    app.run(host='0.0.0.0')


@app.route(url_for("result.html"), methods=['POST'])
def result():
    user_1_playlist = request.form['user_1']
    user_1_playlist.split()
    user_2_playlist = request.form['user_2']
    user_2_playlist.split()
    playlist_1 = user_1_playlist[34:]
    playlist_2 = user_2_playlist[34:]
    return render_template("result.html", user_1_stat=stats_getter(playlist_1), user_2_stat=stats_getter(playlist_2))


def show_site():
    t = Thread(target=run)
    t.start()
