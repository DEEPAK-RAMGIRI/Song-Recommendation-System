import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials
import pickle
import spotipy
import os
from dotenv import load_dotenv


load_dotenv()

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to top, #30cfd0 0%, #330867 100%) !important;
        background-attachment: fixed;
        color: white; /* optional: make text readable */
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

SPOTIPY_CLIENT_ID=os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET=os.getenv('CLIENT_SECRET')

print("CLIENT_ID:", SPOTIPY_CLIENT_ID)
print("CLIENT_SECRET:", SPOTIPY_CLIENT_SECRET)


auth_manager = SpotifyClientCredentials(
   client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_cover_photo(song,artist ):
  search = f"track:{song} artist:{artist}"
  results = sp.search(q=search,type="track")

  if results and results["tracks"]["items"]:
    track = results["tracks"]["items"][0]
    cover_url = track['album']['images'][0]['url'] 
    return cover_url
  else:
    return "https://upload.wikimedia.org/wikipedia/commons/2/26/512pxIcon-sunset_photo_not_found.png"
  

def reccommend_song(song):
  song_index = data[data['song'] == song].index[0]
  recom_distance = sorted(list(enumerate(similar[song_index])),reverse=True,key=lambda x:x[1])

  songs = []
  posters = []
  
  
  for i in recom_distance[1:5]:
    artist = data.iloc[i[0]].artist
    songs.append(data.iloc[i[0]].song)
    posters.append(get_cover_photo(data.iloc[i[0]].song,artist))
  return songs,posters

st.header("Song Reccomendations")

data = pickle.load(open('data','rb'))
similar = pickle.load(open('similar','rb'))
songlist = data['song'].values
selected_song = st.selectbox("Type or select the eng song only",songlist)

if st.button("Show Reccomendations "):
    songs, posters = reccommend_song(selected_song)
    cols = st.columns(4) 
    for i, col in enumerate(cols):
        with col:
            st.text(songs[i])
            st.image(posters[i])
    st.info("this is based on content based filtering")