import argparse
import ast
import pickle
from pathlib import Path

import nltk
from nltk.stem.porter import PorterStemmer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def parse_entities(json_str: str) -> list:
    """Extract 'name' values from JSON-like list strings (genres, keywords)."""
    try:
        data = ast.literal_eval(json_str)
        return [item["name"] for item in data if "name" in item]
    except (ValueError, SyntaxError):
        return []


def parse_top_cast(json_str: str, top_n: int = 3) -> list:
    """Extract up to top_n leading actor names from the cast JSON string."""
    try:
        data = ast.literal_eval(json_str)
        return [item["name"] for item in data[:top_n] if "name" in item]
    except (ValueError, SyntaxError):
        return []


def parse_director(json_str: str) -> list:
    """Extract the Director's name from the crew JSON string."""
    try:
        data = ast.literal_eval(json_str)
        for member in data:
            if member.get("job") == "Director":
                return [member.get("name")]
        return []
    except (ValueError, SyntaxError):
        return []


def clean_and_prepare_dataset(movies_path: str, credits_path: str) -> pd.DataFrame:
    """Merge and preprocess the TMDB 5000 movies and credits datasets."""
    movies_df = pd.read_csv(movies_path)
    credits_df = pd.read_csv(credits_path)

    # 1. Merge datasets on 'title'
    merged_df = movies_df.merge(credits_df, on="title")

    # 2. Select essential metadata features
    features = ["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]
    df = merged_df[features].copy()

    # Handle missing values
    df.dropna(inplace=True)

    # 3. Parse JSON string columns
    df["genres"] = df["genres"].apply(parse_entities)
    df["keywords"] = df["keywords"].apply(parse_entities)
    df["cast"] = df["cast"].apply(parse_top_cast)
    df["crew"] = df["crew"].apply(parse_director)

    # 4. Tokenize overview into word list
    df["overview"] = df["overview"].apply(lambda x: x.split() if isinstance(x, str) else [])

    # 5. Remove spaces within entities to create single unified tokens
    # e.g., "Science Fiction" -> "ScienceFiction", "Sam Worthington" -> "SamWorthington"
    df["genres"] = df["genres"].apply(lambda items: [i.replace(" ", "") for i in items])
    df["keywords"] = df["keywords"].apply(lambda items: [i.replace(" ", "") for i in items])
    df["cast"] = df["cast"].apply(lambda items: [i.replace(" ", "") for i in items])
    df["crew"] = df["crew"].apply(lambda items: [i.replace(" ", "") for i in items])

    # 6. Combine all token lists into a unified 'tags' column
    df["tags"] = df["overview"] + df["genres"] + df["keywords"] + df["cast"] + df["crew"]
    df["tags"] = df["tags"].apply(lambda tokens: " ".join(tokens).lower())

    # Retain the clean dataframe
    new_df = df[["movie_id", "title", "tags"]].copy()

    # 7. Apply PorterStemmer for morphological normalization
    ps = PorterStemmer()

    def stem_text(text: str) -> str:
        return " ".join([ps.stem(word) for word in text.split()])

    new_df["tags"] = new_df["tags"].apply(stem_text)

    return new_df


def build_and_export_models(movies_path: str, credits_path: str, output_dir: str):
    """Preprocess data, compute cosine similarity, and serialize pickle artifacts."""
    print("✦ Processing raw TMDB datasets...")
    processed_df = clean_and_prepare_dataset(movies_path, credits_path)
    print(f"✦ Successfully preprocessed {len(processed_df)} movies.")

    # Vectorization using CountVectorizer
    print("✦ Vectorizing tags with CountVectorizer (max_features=5000, stop_words='english')...")
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(processed_df["tags"]).toarray()

    # Compute Cosine Similarity Matrix
    print("✦ Computing pairwise cosine similarity matrix...")
    similarity = cosine_similarity(vectors)

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Save processed dataframe (both as DataFrame and as dict)
    with (out_path / "movie_list.pkl").open("wb") as f:
        pickle.dump(processed_df, f)

    with (out_path / "movie_dict.pkl").open("wb") as f:
        pickle.dump(processed_df.to_dict(), f)

    with (out_path / "similarity.pkl").open("wb") as f:
        pickle.dump(similarity, f)

    print(f"✓ Successfully exported movie_list.pkl, movie_dict.pkl, and similarity.pkl to '{out_path}'")


def main():
    parser = argparse.ArgumentParser(description="Generate TMDB Content-Based Movie Recommender Model")
    parser.add_argument("--movies-data", required=True, help="Path to tmdb_5000_movies.csv")
    parser.add_argument("--credits-data", required=True, help="Path to tmdb_5000_credits.csv")
    parser.add_argument("--output-dir", default="model", help="Directory to save pickled models")
    args = parser.parse_args()

    build_and_export_models(args.movies_data, args.credits_data, args.output_dir)


if __name__ == "__main__":
    main()
