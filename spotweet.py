import tweepy
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import time

# Twitter API keys
client = tweepy.Client(consumer_key='YOUR_TWITTER_API_KEY',
                       consumer_secret='YOUR_TWITTER_API_SECRET_KEY',
                       access_token='YOUR_TWITTER_ACCESS_TOKEN',
                       access_token_secret='YOUR_TWITTER_ACCESS_TOKEN_SECRET')

# Spotify credentials
spotify_username = "YOUR_SPOTIFY_USERNAME"
spotify_client_id = "YOUR_SPOTIFY_CLIENT_ID"
spotify_client_secret = "YOUR_SPOTIFY_CLIENT_SECRET"
spotify_redirect_uri = "http://localhost:8080/callback"

# Authenticate with Spotify API
scope = "user-modify-playback-state user-read-currently-playing user-read-playback-position user-read-playback-state"
token = util.prompt_for_user_token(spotify_username,
                                   scope,
                                   client_id=spotify_client_id,
                                   client_secret=spotify_client_secret,
                                   redirect_uri=spotify_redirect_uri)
spotify = spotipy.Spotify(auth=token)

def get_current_track():
    try:
        playback_info = spotify.current_playback()
        track_name = playback_info["item"]["name"]
        artist_name = playback_info["item"]["artists"][0]["name"]  # Assuming there's at least one artist
        return track_name, artist_name
    except:
        return None, None

def tweet_current_track(track_name, artist_name):
    tweet = f"listening to {track_name} - {artist_name}"
    response = client.create_tweet(text=tweet)
    print(f"Tweeted: {tweet}")

if __name__ == "__main__":
    current_track = None
    current_artist = None

    while True:
        new_track, new_artist = get_current_track()

        if new_track is not None and new_track != current_track:
            tweet_current_track(new_track, new_artist)
            current_track = new_track
            current_artist = new_artist
  
  # Check for a new track every 30 seconds
        time.sleep(30) 
