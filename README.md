# About
__Spotweet__ is a Python application based on another project of the same name, [Spotweet](https://github.com/Lokarin/Spotweet). In a few words, it reads from the Spotify API and tweets what the user is currently listening to -- that is, song and artist.

## Requirements
In order for you to get __Spotweet__ to work properly, you must do these things:

- Have a Twitter developer account;
- Have access to Spotify's developer dashboard;
- Have Python installed in your computer;
- Have both `tweepy` and `spotipy` installed in your computer via `pip`.

## Setting up the application
The only thing to be done in order to run __Spotweet__ is to have access to the your API keys from both Twitter and Spotify and paste them over their current placeholder: <br/>

```
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
```
<br/>

Then, run the code by opening the terminal and typing: `python spotweet.py`.

## Example
For demonstratation purposes the application ran every five seconds. By default it checks the player every 30 seconds.
![Screen Shot 2023-08-01 at 16 39 28](https://github.com/vszanetti/spotweet/assets/67712911/6f7b23d8-c4b7-4621-be83-7bb128999c21)

