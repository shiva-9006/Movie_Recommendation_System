import argparse
import ast
import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_data(movies_df, credits_df):
    movies_df = movies_df.merge(credits_df, on="title")
    relevant_columns = [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew",
    ]
    movies_df = movies_df[relevant_columns]
    movies_df = movies_df.dropna()

    def convert(obj):
        L = []
        for i in ast.literal_eval(obj):
            L.append(i["name"])
        return L

    movies_df["genres"] = movies_df["genres"].apply(convert)
    movies_df["keywords"] = movies_df["keywords"].apply(convert)

    def convert_cast(obj):
        L = []
        counter = 0
        for i in ast.literal_eval(obj):
            if counter != 3:
                L.append(i["name"])
                counter += 1
            else:
                break
        return L

    movies_df["cast"] = movies_df["cast"].apply(convert_cast)

    def fetch_director(obj):
        L = []
        for i in ast.literal_eval(obj):
            if i["job"] == "Director":
                L.append(i["name"])
                break
        return L

    movies_df["crew"] = movies_df["crew"].apply(fetch_director)

    movies_df["genres"] = movies_df["genres"].apply(lambda x: [i.replace(" ", "") for i in x])
    movies_df["keywords"] = movies_df["keywords"].apply(lambda x: [i.replace(" ", "") for i in x])
    movies_df["cast"] = movies_df["cast"].apply(lambda x: [i.replace(" ", "") for i in x])
    movies_df["crew"] = movies_df["crew"].apply(lambda x: [i.replace(" ", "") for i in x])

    movies_df["tags"] = (
        movies_df["overview"]
        + " "
        + movies_df["genres"].apply(lambda x: " ".join(x))
        + " "
        + movies_df["keywords"].apply(lambda x: " ".join(x))
        + " "
        + movies_df["cast"].apply(lambda x: " ".join(x))
        + " "
        + movies_df["crew"].apply(lambda x: " ".join(x))
    )

    return movies_df[["movie_id", "title", "tags"]]


def build_model(movies_path: str, credits_path: str, output_dir: str):
    movies_df = pd.read_csv(movies_path)
    credits_df = pd.read_csv(credits_path)

    processed = clean_data(movies_df, credits_df)
    processed["tags"] = processed["tags"].apply(lambda x: x.lower())

    vectorizer = CountVectorizer(max_features=5000, stop_words="english")
    vectors = vectorizer.fit_transform(processed["tags"]).toarray()
    similarity = cosine_similarity(vectors)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    with (output_path / "movie_list.pkl").open("wb") as movie_file:
        pickle.dump(processed, movie_file)

    with (output_path / "similarity.pkl").open("wb") as sim_file:
        pickle.dump(similarity, sim_file)

    print(f"Saved model artifacts to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate movie recommender model files.")
    parser.add_argument("--movies-data", required=True, help="Path to tmdb_5000_movies.csv")
    parser.add_argument("--credits-data", required=True, help="Path to tmdb_5000_credits.csv")
    parser.add_argument("--output-dir", default="model", help="Directory to save the model files")
    args = parser.parse_args()

    build_model(args.movies_data, args.credits_data, args.output_dir)


if __name__ == "__main__":
    main()
