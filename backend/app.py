from flask import Flask, abort, render_template
from flask_socketio import SocketIO

from .pesenikManager import Pesenik

pesenik = Pesenik()
app = Flask(__name__)
sio = SocketIO(app)


@app.route("/")
def index():
    return render_template("guest.html", current_song=pesenik.currentSong)


@app.route("/admin/")
def admin_author_list():
    return render_template("admin/author_list.html", authors=pesenik.authors)


@app.route("/admin/<author_hash>/")
def admin_song_list(author_hash: str):
    author = pesenik.authors.get(author_hash)
    if author is None:
        abort(404)
    return render_template("admin/song_list.html", author=author)


@app.route("/admin/<author_hash>/<title_hash>/")
def admin_song(author_hash: str, title_hash: str):
    author = pesenik.authors.get(author_hash)
    if author is None:
        abort(404)

    song = author.songs.get(title_hash)
    if song is None:
        abort(404)

    pesenik.currentSong = song
    sio.emit(
        "change_song",
        {"author": song.author, "title": song.title, "text": song.text},
    )

    return render_template("admin/song.html", song=song)
