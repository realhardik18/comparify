from flask import Flask, render_template, request
from threading import Thread
from flask.helpers import send_file, url_for
from stats_getter import stats_getter
from song_downloader import return_mp3

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


def run():
    app.run(host='0.0.0.0')


@app.route('/result', methods=['POST'])
def result():
    user_1_playlist = request.form['user_1']
    user_1_playlist.split()
    user_2_playlist = request.form['user_2']
    user_2_playlist.split()
    playlist_1 = user_1_playlist[34:]
    playlist_2 = user_2_playlist[34:]
    return render_template("result.html", user_1_stat=stats_getter(playlist_1), user_2_stat=stats_getter(playlist_2))


@app.route("/download")
def download():
    return render_template("download.html")


@app.route("/music", methods=['POST'])
def music():
    song_link = request.form['song']
    song_link.split()
    song_id = song_link[31:]
    song_path = return_mp3(song_id)
    return send_file(song_path, as_attachment=True)


def show_site():
    t = Thread(target=run)
    t.start()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
