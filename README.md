# Song-Recommendation-System

A Content-Based Filtering song recommendation system that suggests similar songs using TF-IDF and Cosine Similarity. Extended with Spotipy for fetching real-time metadata from Spotify, and a Streamlit frontend for easy interaction.


![Project Screenshot](https://github.com/DEEPAK-RAMGIRI/Song-Recommendation-System/blob/main/SONG%20RECCOMENDATION.png)

### Approach & Techniques Used
- Dataset: [Spotify Dataset](https://drive.google.com/uc?id=1YA5XPVjTS-MEYKa71vu7qI9f6gYpD0rv)
- Text Preprocessing – tokenization & stemming using NLTK
- TF-IDF Vector Conversion – feature extraction
- Cosine Similarity – recommendation generation
- Spotipy Integration – fetch song metadata & cover images from Spotify
- Pickle - used for storing processed data and similarity matrices to save computation time.
- Streamlit - provides a simple web-based frontend for interaction.

👉 get spotify client id & secrets [here](https://developer.spotify.com/)
```plaintext
song/
├── main.py
├── project.ipynb # For Teststing the code
│── files.md # contains similar.pkl and data.pkl files 
│── requirements.txt
└── README.md                # Project documentation
```
