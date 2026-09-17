# CINEFILE // Neural Cinema Discovery Engine

An intentional, **anti-vibe coded** movie recommendation and discovery system powered by vector cosine similarity and TMDb metadata.

Designed with an editorial **Obsidian & Amber Gold** aesthetic, featuring high-fidelity typography, real-time vector affinity scores, dynamic hero spotlights, and micro-interactions.

---

## ✦ Key Features

- **Anti-Vibe Coded UI/UX**: Zero generic AI gradient templates or unstyled default widgets. Bespoke typography (`Space Grotesk`, `JetBrains Mono`), glassmorphic panels, dynamic ambient spotlights, and refined editorial layouts.
- **Dynamic Spotlight Hero**: High-res backdrop integration, TMDB score badges, director/cast credits, runtime, release year, and synopsis.
- **Neural Compatibility Badges**: Vector similarity calculations scaled to intuitive `% Match` confidence scores.
- **Instant Discovery & Mood Filters**: Quick exploration by genre (Sci-Fi Cyberpunk, Dark Noir & Crime, Space Opera, High-Octane Action).
- **Dual Runtime Support**:
  1. **Revamped Streamlit Engine** (`app.py`): Full-featured Streamlit app with custom dark theme tokens and responsive card grids.
  2. **Standalone Web App** (`web/index.html`): Ultra-fast client-side vector engine with keyboard hotkeys (`/` for instant search, `Esc` to close), trailer triggers, tactile sound synthesis, and local cinema vault (watchlist).

---

## ✦ Project Structure

```
├── .streamlit/
│   └── config.toml          # Custom dark theme configuration
├── web/
│   ├── index.html           # Standalone modern web app
│   ├── style.css            # Editorial obsidian & amber design system
│   └── app.js               # Client-side vector similarity engine & controller
├── app.py                   # Redesigned Streamlit web application
├── generate_model.py        # Model generator script for TMDb 5000 dataset
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ✦ Quick Start

### 1. Run the Streamlit Application

```bash
pip install -r requirements.txt
streamlit run app.py
```

### 2. Run the Standalone Web App

Open `web/index.html` directly in your browser or serve it via Python:

```bash
python -m http.server 8000 --directory web
```
Then visit `http://localhost:8000`.

---

## ✦ Generating the Full 5,000 Movie Model (Optional)

If you have downloaded `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`:

```bash
python generate_model.py --movies-data /path/to/tmdb_5000_movies.csv --credits-data /path/to/tmdb_5000_credits.csv
```

The system automatically detects `model/movie_list.pkl` and `model/similarity.pkl` and transitions from the curated demo archive to the full 5,000 movie vector space.
