import ast
import os
import pickle
import requests
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==============================================================================
# 1. TMDB API & ASSET CONFIGURATION
# ==============================================================================
TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "8265bd1679663a7ea12ac168da84d2e8")
FALLBACK_POSTER = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=500&q=80"
MODEL_DIR = "model"
MOVIE_LIST_PATH = os.path.join(MODEL_DIR, "movie_list.pkl")
SIMILARITY_PATH = os.path.join(MODEL_DIR, "similarity.pkl")

# Built-in curated dataset fallback in case CSV files are not present locally
CURATED_DATA = [
    {"movie_id": 155, "title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"], "keywords": ["batman", "joker", "gotham", "vigilante"], "cast": ["ChristianBale", "HeathLedger", "AaronEckhart"], "crew": ["ChristopherNolan"], "overview": ["batman", "raises", "stakes", "in", "his", "war", "on", "crime", "gotham", "joker"]},
    {"movie_id": 27205, "title": "Inception", "genres": ["Action", "Sci-Fi", "Adventure"], "keywords": ["dreams", "subconscious", "heist", "mind"], "cast": ["LeonardoDiCaprio", "JosephGordon-Levitt", "ElliotPage"], "crew": ["ChristopherNolan"], "overview": ["cobb", "skilled", "thief", "steals", "corporate", "secrets", "dream", "sharing", "technology"]},
    {"movie_id": 157336, "title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"], "keywords": ["space", "blackhole", "wormhole", "relativity"], "cast": ["MatthewMcConaughey", "AnneHathaway", "JessicaChastain"], "crew": ["ChristopherNolan"], "overview": ["explorers", "wormhole", "surpass", "limitations", "human", "space", "travel"]},
    {"movie_id": 603, "title": "The Matrix", "genres": ["Action", "Sci-Fi"], "keywords": ["simulation", "cyberpunk", "artificialintelligence", "neo"], "cast": ["KeanuReeves", "LaurenceFishburne", "Carrie-AnneMoss"], "crew": ["LillyWachowski"], "overview": ["computer", "hacker", "underground", "insurgents", "fighting", "computers", "earth"]},
    {"movie_id": 335984, "title": "Blade Runner 2049", "genres": ["Sci-Fi", "Drama", "Mystery"], "keywords": ["cyberpunk", "replicant", "dystopia", "future"], "cast": ["RyanGosling", "HarrisonFord", "AnaDeArmas"], "crew": ["DenisVilleneuve"], "overview": ["blade", "runner", "lapd", "officer", "unearths", "long", "buried", "secret"]},
    {"movie_id": 438631, "title": "Dune", "genres": ["Sci-Fi", "Adventure"], "keywords": ["desert", "spice", "sandworm", "prophecy"], "cast": ["TimotheeChalamet", "RebeccaFerguson", "OscarIsaac"], "crew": ["DenisVilleneuve"], "overview": ["paul", "atreides", "brilliant", "gifted", "young", "man", "born", "destiny", "arrakis"]},
    {"movie_id": 19995, "title": "Avatar", "genres": ["Action", "Adventure", "Fantasy", "ScienceFiction"], "keywords": ["cultureclash", "future", "spacewar", "pandora"], "cast": ["SamWorthington", "ZoeSaldana", "SigourneyWeaver"], "crew": ["JamesCameron"], "overview": ["paraplegic", "marine", "dispatched", "moon", "pandora", "unique", "mission"]},
    {"movie_id": 285, "title": "Pirates of the Caribbean: At World's End", "genres": ["Adventure", "Fantasy", "Action"], "keywords": ["ocean", "pirate", "exoticisland", "eastindiatradingcompany"], "cast": ["JohnnyDepp", "OrlandoBloom", "KeiraKnightley"], "crew": ["GoreVerbinski"], "overview": ["captain", "barbossa", "will", "turner", "elizabeth", "swann", "sail", "world", "end"]},
    {"movie_id": 49026, "title": "The Dark Knight Rises", "genres": ["Action", "Crime", "Drama", "Thriller"], "keywords": ["dccomics", "crimefighter", "terrorist", "bane", "batman"], "cast": ["ChristianBale", "MichaelCaine", "GaryOldman"], "crew": ["ChristopherNolan"], "overview": ["eight", "years", "following", "joker", "reign", "anarchy", "batman", "encounters", "mysterious", "selina", "kyle"]},
    {"movie_id": 680, "title": "Pulp Fiction", "genres": ["Thriller", "Crime"], "keywords": ["hitman", "robbery", "gangster", "nonlinear"], "cast": ["JohnTravolta", "SamuelL.Jackson", "UmaThurman"], "crew": ["QuentinTarantino"], "overview": ["burger-loving", "hit", "man", "philosophical", "partner", "drug-addled", "gangster", "moll"]},
    {"movie_id": 13, "title": "Forrest Gump", "genres": ["Comedy", "Drama", "Romance"], "keywords": ["vietnamwar", "running", "historicalevents", "alabama"], "cast": ["TomHanks", "RobinWright", "GarySinise"], "crew": ["RobertZemeckis"], "overview": ["man", "low", "iq", "witnessed", "unwittingly", "influenced", "defining", "historical", "events"]},
    {"movie_id": 550, "title": "Fight Club", "genres": ["Drama"], "keywords": ["soap", "supportgroup", "insomnia", "alterego"], "cast": ["EdwardNorton", "BradPitt", "HelenaBonhamCarter"], "crew": ["DavidFincher"], "overview": ["ticking-time-bomb", "insomniac", "slippery", "soap", "salesman", "channel", "primal", "male", "aggression"]},
    {"movie_id": 78, "title": "Blade Runner", "genres": ["Sci-Fi", "Drama", "Thriller"], "keywords": ["android", "cyberpunk", "replicant", "dystopia"], "cast": ["HarrisonFord", "RutgerHauer", "SeanYoung"], "crew": ["RidleyScott"], "overview": ["twenty-first", "century", "detective", "specializes", "terminating", "replicants"]},
    {"movie_id": 120, "title": "The Lord of the Rings: The Fellowship of the Ring", "genres": ["Adventure", "Fantasy", "Action"], "keywords": ["middleearth", "ring", "hobbit", "wizard", "quest"], "cast": ["ElijahWood", "IanMcKellen", "ViggoMortensen"], "crew": ["PeterJackson"], "overview": ["young", "hobbit", "frodo", "thrust", "epic", "quest", "destroy", "one", "ring"]},
    {"movie_id": 87101, "title": "Terminator 2: Judgment Day", "genres": ["Action", "Sci-Fi", "Thriller"], "keywords": ["cyborg", "timetravel", "futurewar", "skynet", "terminator"], "cast": ["ArnoldSchwarzenegger", "LindaHamilton", "EdwardFurlong"], "crew": ["JamesCameron"], "overview": ["nearly", "10", "years", "passed", "sarah", "connor", "targeted", "termination"]}
]


# ==============================================================================
# 2. DATA PREPROCESSING & MODEL GENERATION PIPELINE
# ==============================================================================
def convert(text):
    """Extract names from JSON-string list of dicts."""
    try:
        data = ast.literal_eval(text)
        return [i["name"] for i in data if "name" in i]
    except Exception:
        return []


def convert3(text):
    """Extract top 3 cast names from JSON-string list of dicts."""
    try:
        data = ast.literal_eval(text)
        return [i["name"] for i in data[:3] if "name" in i]
    except Exception:
        return []


def fetch_director(text):
    """Extract director name(s) from crew JSON-string."""
    try:
        data = ast.literal_eval(text)
        for i in data:
            if i.get("job") == "Director":
                return [i.get("name")]
        return []
    except Exception:
        return []


def collapse(lst):
    """Remove spaces from strings in a list to create single unified tokens."""
    if not isinstance(lst, list):
        return []
    return [str(i).replace(" ", "") for i in lst]


def find_dataset_files():
    """Look for standard TMDb dataset files in known locations."""
    candidate_paths = [
        ("tmdb_5000_movies.csv", "tmdb_5000_credits.csv"),
        ("data/tmdb_5000_movies.csv", "data/tmdb_5000_credits.csv"),
        ("/kaggle/input/tmdb-movie-metadata/tmdb_5000_movies.csv", "/kaggle/input/tmdb-movie-metadata/tmdb_5000_credits.csv"),
    ]
    for m_path, c_path in candidate_paths:
        if os.path.exists(m_path) and os.path.exists(c_path):
            return m_path, c_path
    return None, None


def train_model_from_csv(movies_path: str, credits_path: str):
    """Train CountVectorizer + Cosine Similarity model from raw TMDb CSVs."""
    print(f"Loading data from {movies_path} and {credits_path}...")
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    # Merge on title
    movies = movies.merge(credits, on="title")
    movies = movies[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]
    movies.dropna(inplace=True)

    # Preprocess metadata
    movies["genres"] = movies["genres"].apply(convert)
    movies["keywords"] = movies["keywords"].apply(convert)
    movies["cast"] = movies["cast"].apply(convert3)
    movies["crew"] = movies["crew"].apply(fetch_director)

    # Collapse tokens (remove whitespace)
    movies["cast"] = movies["cast"].apply(collapse)
    movies["crew"] = movies["crew"].apply(collapse)
    movies["genres"] = movies["genres"].apply(collapse)
    movies["keywords"] = movies["keywords"].apply(collapse)

    # Tokenize overview
    movies["overview"] = movies["overview"].apply(lambda x: x.split() if isinstance(x, str) else [])

    # Combine all metadata into unified 'tags'
    movies["tags"] = movies["overview"] + movies["genres"] + movies["keywords"] + movies["cast"] + movies["crew"]

    # Final DataFrame
    new_df = movies[["movie_id", "title", "tags"]].copy()
    new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x).lower())

    # Compute CountVectorizer & Cosine Similarity
    print("Vectorizing tags...")
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vector = cv.fit_transform(new_df["tags"]).toarray()

    print("Computing cosine similarity matrix...")
    similarity = cosine_similarity(vector)

    # Export artifacts
    os.makedirs(MODEL_DIR, exist_ok=True)
    pickle.dump(new_df, open(MOVIE_LIST_PATH, "wb"))
    pickle.dump(similarity, open(SIMILARITY_PATH, "wb"))
    print("Exported models successfully.")
    return new_df, similarity


def build_curated_model():
    """Build similarity model from built-in curated catalog if CSVs are absent."""
    df = pd.DataFrame(CURATED_DATA)
    df["combined_tags"] = (
        df["overview"].apply(lambda x: " ".join(x))
        + " "
        + df["genres"].apply(lambda x: " ".join(x))
        + " "
        + df["keywords"].apply(lambda x: " ".join(x))
        + " "
        + df["cast"].apply(lambda x: " ".join(x))
        + " "
        + df["crew"].apply(lambda x: " ".join(x))
    ).str.lower()

    cv = CountVectorizer(stop_words="english")
    vector = cv.fit_transform(df["combined_tags"]).toarray()
    similarity = cosine_similarity(vector)

    new_df = df[["movie_id", "title"]].copy()
    new_df["tags"] = df["combined_tags"]

    os.makedirs(MODEL_DIR, exist_ok=True)
    pickle.dump(new_df, open(MOVIE_LIST_PATH, "wb"))
    pickle.dump(similarity, open(SIMILARITY_PATH, "wb"))
    return new_df, similarity


@st.cache_resource(show_spinner=False)
def load_data_and_model():
    """Load existing model or automatically train one."""
    if os.path.exists(MOVIE_LIST_PATH) and os.path.exists(SIMILARITY_PATH):
        try:
            movies = pickle.load(open(MOVIE_LIST_PATH, "rb"))
            similarity = pickle.load(open(SIMILARITY_PATH, "rb"))
            # Ensure movies is a DataFrame
            if isinstance(movies, dict):
                movies = pd.DataFrame(movies)
            return movies, similarity
        except Exception:
            pass

    # Check if raw CSVs exist to train from scratch
    movies_csv, credits_csv = find_dataset_files()
    if movies_csv and credits_csv:
        return train_model_from_csv(movies_csv, credits_csv)

    # Fallback to curated catalog
    return build_curated_model()


# ==============================================================================
# 3. TMDB POSTER FETCHING & RECOMMENDATION ENGINE
# ==============================================================================
@st.cache_data(show_spinner=False, ttl=3600)
def fetch_poster(movie_id):
    """Fetch movie poster URL from TMDb API with caching and error handling."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=4)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception:
        pass
    return FALLBACK_POSTER


def recommend(movie, movies_df, similarity_matrix, top_n=5):
    """Recommend top-N similar movies with corresponding posters."""
    if movie not in movies_df["title"].values:
        return [], []

    index = movies_df[movies_df["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity_matrix[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1 : top_n + 1]:
        movie_row = movies_df.iloc[i[0]]
        movie_id = int(movie_row["movie_id"])
        recommended_movie_names.append(movie_row["title"])
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


# ==============================================================================
# 4. STREAMLIT FRONTEND USER INTERFACE
# ==============================================================================
def main():
    st.set_page_config(
        page_title="Movie Recommender System",
        page_icon="🎬",
        layout="wide",
    )

    # Custom Clean Styling
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 2.2rem;
            font-weight: 700;
            color: #FF4B4B;
            margin-bottom: 0.2rem;
        }
        .sub-header {
            font-size: 1rem;
            color: #888888;
            margin-bottom: 2rem;
        }
        .movie-card {
            background-color: #1e1e24;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="main-header">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Content-Based Recommendation Engine using TMDb Metadata & Cosine Similarity</div>', unsafe_allow_html=True)

    # Load / Initialize Models
    movies, similarity = load_data_and_model()
    movie_list = sorted(movies["title"].unique())

    # Sidebar Options
    with st.sidebar:
        st.header("⚙️ Settings")
        st.info(f"📊 Dataset Size: **{len(movies)}** movies loaded")
        
        movies_csv, credits_csv = find_dataset_files()
        if movies_csv and credits_csv:
            if st.button("🔄 Retrain on TMDb CSVs"):
                with st.spinner("Processing TMDb dataset and vectorizing tags..."):
                    train_model_from_csv(movies_csv, credits_csv)
                    st.cache_resource.clear()
                    st.rerun()

    # Movie Selector
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown:",
        movie_list,
        index=0 if len(movie_list) > 0 else None,
    )

    # Recommendation Trigger
    if st.button("🚀 Show Recommendation", use_container_width=True, type="primary"):
        if selected_movie:
            with st.spinner("Computing cosine similarities & fetching movie posters..."):
                names, posters = recommend(selected_movie, movies, similarity, top_n=5)

            if names:
                st.subheader(f"✨ Movies Similar to '{selected_movie}':")
                cols = st.columns(5)
                for col, name, poster in zip(cols, names, posters):
                    with col:
                        st.markdown(f"**{name}**")
                        st.image(poster, use_container_width=True)
            else:
                st.warning("No recommendations found for the selected movie.")


if __name__ == "__main__":
    main()
