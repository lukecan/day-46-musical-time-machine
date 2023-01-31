# Musical Time Machine
This code scrapes the top 100 songs of a specified year from Billboard Hot 100 charts and adds them to a private playlist on the user's Spotify account.
## Requirements
- `BeautifulSoup`
- `requests`
- `dotenv`
- `Spotipy`
## Spotify Authentication
To authenticate with Spotify, you need to sign up for a Spotify Developer Account and create an app. This will provide you with the client ID and client secret needed to run the code. The `dotenv` package is used to store these credentials in an environment variable, so they are not exposed in the code.
## Usage
The user is prompted to input the desired year in the format YYYY-MM-DD. The code then scrapes the top 100 songs of that year from the Billboard Hot 100 charts and adds them to a private playlist on the user's Spotify account.
## Conclusion
This code is a fun way to create a playlist of popular songs from a specific year. It utilizes web scraping, authentication with the Spotify API, and playlist creation with the Spotify API to create a personalized playlist.
