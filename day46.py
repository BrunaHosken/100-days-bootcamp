#Spotify Playlist

from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


SPOTIFY_ID= os.getenv('SPOTIFY_ID')
SPOTIFY_SECRET= os.getenv('SPOTIFY_SECRET')

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="projeto tcc", 
    )
)

user_id = sp.current_user()["id"]


year_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = year_input.split('-')[0]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year_input}")
page = response.text

soup = BeautifulSoup(page, "html.parser")

musics = soup.select(selector="li h3",  id="title-of-a-story")[0:100]

music_list = [ music.getText().strip() for music in musics ]
print(music_list)

scope = "user-library-read"

uri = []
for search in music_list:
    results = sp.search(q=f'track:{search} year:{year}', type='track')
    try:
        uri.append(results['tracks']['items'][0]['uri'])
        print(f"{search} -  found")
    except IndexError:
        print(f"{search} -  don't found")


playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100",  public=False)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks= uri)
