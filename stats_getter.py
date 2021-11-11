import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


auth_manager = SpotifyClientCredentials(
    client_id='3ef2038cebf54a798590da6ac6ae6321',
    client_secret='d7f09d28bb3d4902a7764be55cad3763'
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
    avg_duration = "{:.2f}".format(avg_duration)
    total_popularity = 0
    for id in track_ids:
        track_info_for_popularity = sp.track(id)
        track_popularity = track_info_for_popularity['popularity']
        total_popularity += track_popularity
    avg_popularity = total_popularity/len(track_ids)
    avg_popularity = "{:.2f}".format(avg_popularity)
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


'''
THIS FEATURE IS STILL UNDER DEVELOPMENT
def common_getter(p_1, p_2):
    p_1_songs = []
    p_1_artists = []
    p_2_songs = []
    p_2_artists = []
    count = 1
    playlists = [p_1[34:], p_2[34:]]
    for playlist in playlists:
        playlist = sp.user_playlist("spotify", playlist)
        track_ids = []
        for item in playlist['tracks']['items']:
            track = item['track']
            track_ids.append(track['id'])
        for id in track_ids:
            track_info = sp.track(id)
            name = track_info['name']
            artist = track_info['album']['artists'][0]['name']
            if count == 1:
                p_1_songs.append(name)
                p_1_artists.append(artist)
            elif count == 2:
                p_2_songs.append(name)
                p_2_artists.append(artist)
    p_1_artists_set = set(p_1_artists)
    p_1_songs_set = set(p_1_songs)
    common_artists = p_1_artists_set.intersection(p_2_artists)
    common_songs = p_1_songs_set.intersection(p_2_songs)
    common_artists_as_list = list(common_artists)
    common_songs_as_list = list(common_songs)
    common = []
    if len(common_artists) == 0:
        common.append("No common artists found")
    elif len(common_artists) != 0:
        com_artists = ', '.join(map(str, common_artists_as_list))
        common.append(com_artists)
    if len(common_songs) == 0:
        common.append("No common songs found")
    elif len(common_songs) != 0:
        com_songs = ', '.join(map(str, common_songs_as_list))
        common.append(com_songs)
    return common

'''
