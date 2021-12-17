import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from googlesearch import search
import os
from pytube import YouTube


def return_mp3(song_id):
    auth_manager = SpotifyClientCredentials(
        client_id='3ef2038cebf54a798590da6ac6ae6321',
        client_secret='d7f09d28bb3d4902a7764be55cad3763'
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)

    track_info = sp.track(song_id)
    song_name = track_info['name']+" youtube"
    results = []
    for j in search(song_name, tld="co.in", num=1, stop=1, pause=2):
        results.append(j)
    vid_link = results[0]
    yt = YouTube(vid_link)
    video = yt.streams.filter(only_audio=True).first()
    destination = r"your file destination"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = f"{track_info['name']}.mp3"
    file_name = track_info['name']+'.mp3'
    os.rename(out_file, new_file)
    return file_name
