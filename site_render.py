from flask import Flask, render_template
from threading import Thread
from stats_getter import stats_getter

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html", stat1=stats_getter("x"), stat2=stats_getter("x"))


def run():
    app.run(host='0.0.0.0')


def show_site():
    t = Thread(target=run)
    t.start()
