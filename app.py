import os
import pickle
from pathlib import Path

import pandas as pd
import requests
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "8265bd1679663a7ea12ac168da84d2e8")
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_DIR = PROJECT_ROOT / "model"
MOVIE_MODEL_PATH = MODEL_DIR / "movie_list.pkl"
SIMILARITY_MODEL_PATH = MODEL_DIR / "similarity.pkl"
FALLBACK_POSTER = (
    "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba"
    "?auto=format&fit=crop&w=900&q=80"
)


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id: int) -> str:
    """Fetch the poster image from TMDB for a movie ID."""
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US",
            timeout=8,
        )
        response.raise_for_status()
        payload = response.json()
        poster_path = payload.get("poster_path")
        if not poster_path:
            return FALLBACK_POSTER
        return f"{TMDB_IMAGE_BASE}/{poster_path}"
    except requests.RequestException:
        return FALLBACK_POSTER


def build_demo_model():
    """Generate a lightweight in-memory demo model when the real CSV files are absent."""
    demo_data = [
        {
            "movie_id": 11,
            "title": "Star Wars",
            "overview": "A galaxy far away with epic space battles and a legacy of heroes.",
            "genres": ["Action", "Adventure", "Sci-Fi"],
            "keywords": ["space", "battle", "empire", "rebellion"],
            "cast": ["Mark Hamill", "Harrison Ford", "Carrie Fisher"],
            "crew": ["George Lucas"],
        },
        {
            "movie_id": 155,
            "title": "The Dark Knight",
            "overview": "A masked vigilante fights chaos as Gotham falls under criminal pressure.",
            "genres": ["Action", "Crime", "Drama"],
            "keywords": ["gotham", "crime", "mask", "hero"],
            "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
            "crew": ["Christopher Nolan"],
        },
        {
            "movie_id": 603,
            "title": "The Matrix",
            "overview": "A hacker discovers reality is a simulated world and must fight for freedom.",
            "genres": ["Action", "Sci-Fi"],
            "keywords": ["matrix", "simulation", "reality", "neo"],
            "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
            "crew": ["The Wachowskis"],
        },
        {
            "movie_id": 1726,
            "title": "Iron Man",
            "overview": "A billionaire weapons maker builds a suit and becomes a superhero.",
            "genres": ["Action", "Adventure", "Sci-Fi"],
            "keywords": ["superhero", "armor", "technology", "flight"],
            "cast": ["Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"],
            "crew": ["Jon Favreau"],
        },
        {
            "movie_id": 27205,
            "title": "Inception",
            "overview": "A thief enters dreams to plant ideas and change the future of a company.",
            "genres": ["Action", "Sci-Fi", "Thriller"],
            "keywords": ["dreams", "heist", "mind", "architecture"],
            "cast": ["Leonardo DiCaprio", "Tom Hardy", "Joseph Gordon-Levitt"],
            "crew": ["Christopher Nolan"],
        },
        {
            "movie_id": 299536,
            "title": "Avengers: Infinity War",
            "overview": "Superheroes unite to stop a cosmic tyrant and save the universe.",
            "genres": ["Action", "Adventure", "Sci-Fi"],
            "keywords": ["superhero", "universe", "battle", "thanos"],
            "cast": ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo"],
            "crew": ["Russo Brothers"],
        },
        {
            "movie_id": 27205,
            "title": "Interstellar",
            "overview": "A team travels through a wormhole in search of a new home for humanity.",
            "genres": ["Adventure", "Drama", "Sci-Fi"],
            "keywords": ["space", "humanity", "wormhole", "exploration"],
            "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
            "crew": ["Christopher Nolan"],
        },
        {
            "movie_id": 140607,
            "title": "Star Trek Beyond",
            "overview": "The Enterprise crew faces a powerful enemy in deep space.",
            "genres": ["Action", "Adventure", "Sci-Fi"],
            "keywords": ["space", "starship", "adventure", "exploration"],
            "cast": ["Chris Pine", "Zachary Quinto", "Simon Pegg"],
            "crew": ["Justin Lin"],
        },
    ]

    demo_df = pd.DataFrame(demo_data)
    demo_df["tags"] = (
        demo_df["overview"].fillna("")
        + " "
        + demo_df["genres"].apply(lambda x: " ".join(x)).fillna("")
        + " "
        + demo_df["keywords"].apply(lambda x: " ".join(x)).fillna("")
        + " "
        + demo_df["cast"].apply(lambda x: " ".join(x)).fillna("")
        + " "
        + demo_df["crew"].apply(lambda x: " ".join(x)).fillna("")
    )
    demo_df["tags"] = demo_df["tags"].str.lower()

    vectorizer = CountVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(demo_df["tags"])
    similarity = cosine_similarity(vectors)
    return demo_df, similarity


@st.cache_data(show_spinner=False)
def load_models():
    """Load recommendation model files if they exist, otherwise use a built-in demo model."""
    if MOVIE_MODEL_PATH.exists() and SIMILARITY_MODEL_PATH.exists():
        with MOVIE_MODEL_PATH.open("rb") as movie_file:
            movies = pickle.load(movie_file)

        with SIMILARITY_MODEL_PATH.open("rb") as similarity_file:
            similarity = pickle.load(similarity_file)

        return movies, similarity

    return build_demo_model()


@st.cache_data(show_spinner=False)
def recommend(selected_movie: str, movies, similarity):
    """Return the next five similar movies for the selected title."""
    if movies is None or similarity is None:
        return [], []

    if selected_movie not in movies["title"].values:
        return [], []

    index = movies[movies["title"] == selected_movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda item: item[1],
    )

    movie_names = []
    movie_posters = []

    for idx, score in distances[1:6]:
        movie_row = movies.iloc[idx]
        movie_names.append(movie_row["title"])
        movie_posters.append(fetch_poster(int(movie_row["movie_id"])))

    return movie_names, movie_posters


st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
    }
    .stApp {
        color: #e5e7eb;
    }
    div[data-testid="stSelectbox"] > div {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.5);
        border-radius: 12px;
    }
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.75rem;
    }
    .movie-card {
        background: rgba(17, 24, 39, 0.8);
        border-radius: 16px;
        padding: 0.75rem;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.25);
        text-align: center;
    }
    .movie-card img {
        border-radius: 12px;
        width: 100%;
        height: 320px;
        object-fit: cover;
    }
    .headline {
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin-bottom: 0.25rem;
    }
    .subheadline {
        color: #cbd5e1;
        font-size: 1.05rem;
        margin-bottom: 1rem;
    }
    .note-box {
        background: rgba(30, 41, 59, 0.8);
        padding: 1rem 1.25rem;
        border-radius: 12px;
        border: 1px solid rgba(99, 102, 241, 0.35);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="headline">🎬 Movie Recommender</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheadline">Discover movies that match your taste with a content-based recommendation engine.</div>',
    unsafe_allow_html=True,
)

movies, similarity = load_models()

with st.sidebar:
    st.markdown("### App status")
    if MOVIE_MODEL_PATH.exists() and SIMILARITY_MODEL_PATH.exists():
        st.success("Model files detected")
        st.caption(f"{len(movies)} movies available")
    else:
        st.warning("Demo data is active")
        st.caption("The real model files are not present, so the app is using an embedded sample catalog for a working demo experience.")

    st.markdown("---")
    st.markdown("### Generate the real model")
    st.code(
        "python generate_model.py --movies-data /path/to/tmdb_5000_movies.csv --credits-data /path/to/tmdb_5000_credits.csv",
        language="bash",
    )

if not (MOVIE_MODEL_PATH.exists() and SIMILARITY_MODEL_PATH.exists()):
    st.markdown(
        """
        <div class="note-box">
            The app is running in <strong>demo mode</strong> because the real model files were not found. When you add the TMDb dataset and generate
            <strong>movie_list.pkl</strong> and <strong>similarity.pkl</strong>, the recommender switches automatically to the full model-backed mode.
        </div>
        """,
        unsafe_allow_html=True,
    )

movie_list = movies["title"].tolist()
selected_movie = st.selectbox(
    "Type or select a movie",
    movie_list,
    index=movie_list.index("The Dark Knight") if "The Dark Knight" in movie_list else 0,
)

if st.button("Show recommendations", type="primary"):
    recommended_titles, recommended_posters = recommend(selected_movie, movies, similarity)

    if not recommended_titles:
        st.warning("No recommendations were found for this selection.")
    else:
        st.subheader(f"Movies similar to {selected_movie}")
        cols = st.columns(5)
        for column, title, poster in zip(cols, recommended_titles, recommended_posters):
            with column:
                st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                st.image(poster, width="stretch")
                st.markdown(f"**{title}**", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Select a movie from the list and click the button to see five recommendations.")

