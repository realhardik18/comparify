import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(
    client_id="x",
    client_secret="x"
)

sp = spotipy.Spotify(auth_manager=auth_manager)


def stats_getter(playlist):
    track_ids = []
    playlist = sp.user_playlist("spotify", playlist)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])

    total_lenght = 0
    for id in track_ids:
        track_info_for_duration = sp.track(id)
        track_lenght = track_info_for_duration['duration_ms']
        total_lenght += track_lenght
    dur_in_mins = total_lenght/60000
    avg_duration = dur_in_mins/len(track_ids)
    total_popularity = 0
    for id in track_ids:
        track_info_for_popularity = sp.track(id)
        track_popularity = track_info_for_popularity['popularity']
        total_popularity += track_popularity
    avg_popularity = total_popularity/len(track_ids)
    playlist_artists = []
    for id in track_ids:
        track_info_for_most_occuring_artist = sp.track(id)
        track_artist = track_info_for_most_occuring_artist['album']['artists'][0]['name']
        playlist_artists.append(track_artist)
    most_common_artist = max(set(playlist_artists), key=playlist_artists.count)
    stats = {
        'avg_len': avg_duration,
        'avg_pop': avg_popularity,
        'most_com_artist': most_common_artist
    }

    return stats
