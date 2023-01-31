from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/"+date)
soup = BeautifulSoup(response.text, 'html.parser')
all_titles = soup.select(selector="li h3", class_="c-title")
titles = [title.getText().strip() for title in all_titles[:100]]

# Spotify Authentication
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
uri = [sp.search(title, type='track')["tracks"]["items"][0]["uri"] for title in titles]
playlist_ID = sp.user_playlist_create(user=user_id, name=f"Top 100s of {date}", public=False)["id"]
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_ID, tracks=uri)
