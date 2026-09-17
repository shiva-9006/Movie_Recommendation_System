// ==========================================================================
// CINEFILE ENGINE - REAL-TIME VECTOR RECOMMENDATION & DISCOVERY
// ==========================================================================

const MOVIES_DATABASE = [
  {
    id: 155,
    title: "The Dark Knight",
    year: 2008,
    rating: 9.0,
    runtime: "152 min",
    director: "Christopher Nolan",
    cast: ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
    genres: ["Action", "Crime", "Drama"],
    keywords: ["batman", "joker", "gotham", "chaos", "vigilante", "corruption"],
    overview: "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",
    poster: "https://image.tmdb.org/t/p/w780/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/hkBaDkMWbLaf8B1lsWsKX7Ew3Xq.jpg"
  },
  {
    id: 27205,
    title: "Inception",
    year: 2010,
    rating: 8.8,
    runtime: "148 min",
    director: "Christopher Nolan",
    cast: ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
    genres: ["Action", "Sci-Fi", "Adventure"],
    keywords: ["dreams", "subconscious", "heist", "mind", "totem", "reality", "architecture"],
    overview: "Cobb, a skilled thief who steals corporate secrets through the use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.",
    poster: "https://image.tmdb.org/t/p/w780/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg"
  },
  {
    id: 157336,
    title: "Interstellar",
    year: 2014,
    rating: 8.7,
    runtime: "169 min",
    director: "Christopher Nolan",
    cast: ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
    genres: ["Adventure", "Drama", "Sci-Fi"],
    keywords: ["space", "black hole", "wormhole", "relativity", "astronaut", "time travel", "gravity"],
    overview: "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.",
    poster: "https://image.tmdb.org/t/p/w780/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/xJHokMbljvjADYdit5fK5VQsXEG.jpg"
  },
  {
    id: 603,
    title: "The Matrix",
    year: 1999,
    rating: 8.7,
    runtime: "136 min",
    director: "The Wachowskis",
    cast: ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
    genres: ["Action", "Sci-Fi"],
    keywords: ["simulation", "cyberpunk", "artificial intelligence", "dystopia", "neo", "virtual reality", "red pill"],
    overview: "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
    poster: "https://image.tmdb.org/t/p/w780/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/7u3fvbg1vO9GMrSXm1zBhkGsq7.jpg"
  },
  {
    id: 335984,
    title: "Blade Runner 2049",
    year: 2017,
    rating: 8.0,
    runtime: "164 min",
    director: "Denis Villeneuve",
    cast: ["Ryan Gosling", "Harrison Ford", "Ana de Armas"],
    genres: ["Sci-Fi", "Drama", "Mystery"],
    keywords: ["cyberpunk", "replicant", "dystopia", "noir", "future", "artificial intelligence", "hologram"],
    overview: "Thirty years after the events of the first film, a new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what's left of society into chaos.",
    poster: "https://image.tmdb.org/t/p/w780/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/sAtoMqDVhNDQBc3QJL3RF6hlxGq.jpg"
  },
  {
    id: 438631,
    title: "Dune",
    year: 2021,
    rating: 8.0,
    runtime: "155 min",
    director: "Denis Villeneuve",
    cast: ["Timothée Chalamet", "Rebecca Ferguson", "Oscar Isaac"],
    genres: ["Sci-Fi", "Adventure"],
    keywords: ["spice", "sandworm", "desert planet", "prophecy", "empire", "space epic", "arrakis"],
    overview: "Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people.",
    poster: "https://image.tmdb.org/t/p/w780/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/eeijXm355xDqlZvNc3ENCH9io5f.jpg"
  },
  {
    id: 11,
    title: "Star Wars: A New Hope",
    year: 1977,
    rating: 8.6,
    runtime: "121 min",
    director: "George Lucas",
    cast: ["Mark Hamill", "Harrison Ford", "Carrie Fisher"],
    genres: ["Adventure", "Action", "Sci-Fi"],
    keywords: ["galactic empire", "jedi", "space opera", "rebellion", "death star", "lightsaber", "the force"],
    overview: "Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Luke Skywalker and captain Han Solo team up with R2-D2 and C-3PO to rescue the princess.",
    poster: "https://image.tmdb.org/t/p/w780/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/zqkmTXzjkAgPnBZoN2AZ5T8v9F.jpg"
  },
  {
    id: 299536,
    title: "Avengers: Infinity War",
    year: 2018,
    rating: 8.3,
    runtime: "149 min",
    director: "Anthony & Joe Russo",
    cast: ["Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo"],
    genres: ["Action", "Adventure", "Sci-Fi"],
    keywords: ["superhero", "infinity stones", "marvel", "thanos", "cosmic battle", "sacrifice"],
    overview: "As the Avengers and their allies have continued to protect the world, a new danger has emerged from the cosmic shadows: Thanos, a despot whose goal is to collect all six Infinity Stones.",
    poster: "https://image.tmdb.org/t/p/w780/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/mDfJG3LC3Dqb67AZ52x3Z0jOSUn.jpg"
  },
  {
    id: 1726,
    title: "Iron Man",
    year: 2008,
    rating: 7.9,
    runtime: "126 min",
    director: "Jon Favreau",
    cast: ["Robert Downey Jr.", "Gwyneth Paltrow", "Jeff Bridges"],
    genres: ["Action", "Sci-Fi", "Adventure"],
    keywords: ["superhero", "marvel", "billionaire", "high tech", "power suit", "weapons"],
    overview: "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil and reclaims his legacy.",
    poster: "https://image.tmdb.org/t/p/w780/78lPtwv72eTNqFW9COBYI0dWDJa.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/cyecB7godJ6kNHGON0DHcA99FGF.jpg"
  },
  {
    id: 278,
    title: "The Shawshank Redemption",
    year: 1994,
    rating: 9.3,
    runtime: "142 min",
    director: "Frank Darabont",
    cast: ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
    genres: ["Drama", "Crime"],
    keywords: ["prison", "hope", "friendship", "escape", "wrongful imprisonment", "justice"],
    overview: "Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison facility.",
    poster: "https://image.tmdb.org/t/p/w780/9cqNrmSplYFS59PlZrNmFeSkqpL.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg"
  },
  {
    id: 238,
    title: "The Godfather",
    year: 1972,
    rating: 9.2,
    runtime: "175 min",
    director: "Francis Ford Coppola",
    cast: ["Marlon Brando", "Al Pacino", "James Caan"],
    genres: ["Drama", "Crime"],
    keywords: ["mafia", "family", "organized crime", "godfather", "loyalty", "power", "corleone"],
    overview: "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family.",
    poster: "https://image.tmdb.org/t/p/w780/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/tmU7GeKVybMWF92GImsGqa5iO3G.jpg"
  },
  {
    id: 680,
    title: "Pulp Fiction",
    year: 1994,
    rating: 8.9,
    runtime: "154 min",
    director: "Quentin Tarantino",
    cast: ["John Travolta", "Samuel L. Jackson", "Uma Thurman"],
    genres: ["Crime", "Drama", "Thriller"],
    keywords: ["hitman", "nonlinear", "dialogue", "briefcase", "gangster", "cult classic"],
    overview: "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in four tales of violence and redemption.",
    poster: "https://image.tmdb.org/t/p/w780/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg"
  },
  {
    id: 550,
    title: "Fight Club",
    year: 1999,
    rating: 8.8,
    runtime: "139 min",
    director: "David Fincher",
    cast: ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"],
    genres: ["Drama", "Thriller"],
    keywords: ["insomnia", "alter ego", "anarchy", "consumerism", "underground fight", "soap"],
    overview: "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy.",
    poster: "https://image.tmdb.org/t/p/w780/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/hZkgoQYus5vegHoetLkCJzb17zJ.jpg"
  },
  {
    id: 157350,
    title: "Ex Machina",
    year: 2014,
    rating: 7.7,
    runtime: "108 min",
    director: "Alex Garland",
    cast: ["Domhnall Gleeson", "Alicia Vikander", "Oscar Isaac"],
    genres: ["Sci-Fi", "Drama", "Mystery"],
    keywords: ["artificial intelligence", "android", "turing test", "manipulation", "consciousness", "robot"],
    overview: "Celebrated programmer Caleb Smith wins a competition to spend a week at the private mountain estate of Nathan Bateman, the brilliant CEO of his company, to perform a Turing test on an AI android.",
    poster: "https://image.tmdb.org/t/p/w780/btbSMBHQ4k51h8f7X31GfEw0H4b.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/7f8hA3g6L5M0d7q1W2P8h2L0q4r.jpg"
  },
  {
    id: 87101,
    title: "Terminator 2: Judgment Day",
    year: 1991,
    rating: 8.6,
    runtime: "137 min",
    director: "James Cameron",
    cast: ["Arnold Schwarzenegger", "Linda Hamilton", "Edward Furlong"],
    genres: ["Action", "Sci-Fi", "Thriller"],
    keywords: ["cyborg", "time travel", "future war", "skynet", "liquid metal", "terminator"],
    overview: "Nearly 10 years have passed since Sarah Connor was targeted for termination. Now her son, John, is the target for a newer, deadlier Terminator.",
    poster: "https://image.tmdb.org/t/p/w780/5M0j0B18abtBI5flAQR8umneTR.jpg",
    backdrop: "https://image.tmdb.org/t/p/w1280/87p5n16fKjD3uW7L10oX2P7V0z7.jpg"
  }
];

// ==========================================================================
// VECTOR COSINE SIMILARITY ENGINE (JAVASCRIPT)
// ==========================================================================
class RecommenderEngine {
  constructor(movies) {
    this.movies = movies;
    this.vocabulary = new Set();
    this.movieVectors = [];
    this.buildIndex();
  }

  buildIndex() {
    // Generate document terms for each movie
    const docs = this.movies.map(m => {
      const tokens = [
        ...m.genres.map(g => g.toLowerCase()),
        ...m.keywords.map(k => k.toLowerCase()),
        ...m.cast.map(c => c.toLowerCase()),
        m.director.toLowerCase(),
        ...m.overview.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(/\s+/)
      ];
      tokens.forEach(t => {
        if (t.length > 2) this.vocabulary.add(t);
      });
      return tokens;
    });

    const vocabList = Array.from(this.vocabulary);
    const vocabIndex = new Map(vocabList.map((w, i) => [w, i]));

    // Build Term Frequency vectors
    this.movieVectors = docs.map(tokens => {
      const vec = new Float32Array(vocabList.length);
      tokens.forEach(t => {
        if (vocabIndex.has(t)) {
          vec[vocabIndex.get(t)] += 1.0;
        }
      });
      // Normalize vector
      let norm = 0;
      for (let i = 0; i < vec.length; i++) norm += vec[i] * vec[i];
      norm = Math.sqrt(norm);
      if (norm > 0) {
        for (let i = 0; i < vec.length; i++) vec[i] /= norm;
      }
      return vec;
    });
  }

  getRecommendations(targetMovieId, topK = 6) {
    const targetIdx = this.movies.findIndex(m => m.id === targetMovieId);
    if (targetIdx === -1) return [];

    const targetVec = this.movieVectors[targetIdx];
    const scores = [];

    for (let i = 0; i < this.movieVectors.length; i++) {
      if (i === targetIdx) continue;
      const compVec = this.movieVectors[i];
      let dot = 0;
      for (let j = 0; j < targetVec.length; j++) {
        dot += targetVec[j] * compVec[j];
      }
      scores.push({
        movie: this.movies[i],
        similarity: dot
      });
    }

    scores.sort((a, b) => b.similarity - a.similarity);

    return scores.slice(0, topK).map(s => {
      // Scale cosine score into intuitive matching percentage (65% to 99%)
      const matchScore = Math.min(99, Math.max(68, Math.round(s.similarity * 100 * 2.2 + 35)));
      return {
        ...s.movie,
        matchScore
      };
    });
  }
}

// ==========================================================================
// TACTILE SOUND SYNTHESIZER (WEB AUDIO API)
// ==========================================================================
class TactileAudio {
  constructor() {
    this.ctx = null;
    this.enabled = true;
  }

  init() {
    if (!this.ctx && typeof AudioContext !== 'undefined') {
      this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    }
  }

  playClick() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(800, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(300, this.ctx.currentTime + 0.04);
      gain.gain.setValueAtTime(0.06, this.ctx.currentTime);
      gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.04);
    } catch (e) {}
  }
}

// ==========================================================================
// APPLICATION CONTROLLER
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  const engine = new RecommenderEngine(MOVIES_DATABASE);
  const audio = new TactileAudio();

  let activeMovie = MOVIES_DATABASE[0]; // The Dark Knight
  let activeGenre = 'All';
  let watchlist = JSON.parse(localStorage.getItem('cinefile_vault') || '[]');

  // UI Element Selectors
  const searchInput = document.getElementById('movieSearchInput');
  const searchDropdown = document.getElementById('searchDropdown');
  const filterChips = document.getElementById('filterChips');
  const heroSection = document.getElementById('heroSection');
  const heroBackdrop = document.getElementById('heroBackdrop');
  const heroPoster = document.getElementById('heroPoster');
  const heroTitle = document.getElementById('heroTitle');
  const heroMetaRow = document.getElementById('heroMetaRow');
  const heroOverview = document.getElementById('heroOverview');
  const heroCredits = document.getElementById('heroCredits');
  const heroRecBtn = document.getElementById('heroRecBtn');
  const heroTrailerBtn = document.getElementById('heroTrailerBtn');
  const heroBookmarkBtn = document.getElementById('heroBookmarkBtn');
  const heroBookmarkIcon = document.getElementById('heroBookmarkIcon');
  const moviesGrid = document.getElementById('moviesGrid');
  const recSubheading = document.getElementById('recSubheading');
  
  // Modal Elements
  const movieModal = document.getElementById('movieModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalBackdrop = document.getElementById('modalBackdrop');
  const modalPoster = document.getElementById('modalPoster');
  const modalTitle = document.getElementById('modalTitle');
  const modalChips = document.getElementById('modalChips');
  const modalOverview = document.getElementById('modalOverview');
  const modalDirector = document.getElementById('modalDirector');
  const modalCast = document.getElementById('modalCast');
  const modalKeywords = document.getElementById('modalKeywords');
  const modalMatchTag = document.getElementById('modalMatchTag');
  const modalExploreBtn = document.getElementById('modalExploreBtn');
  const modalTrailerLink = document.getElementById('modalTrailerLink');

  // Watchlist Drawer
  const watchlistDrawer = document.getElementById('watchlistDrawer');
  const watchlistToggle = document.getElementById('watchlistToggle');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const watchlistList = document.getElementById('watchlistList');
  const watchlistCount = document.getElementById('watchlistCount');
  const soundToggle = document.getElementById('soundToggle');
  const soundIcon = document.getElementById('soundIcon');

  let currentModalMovie = null;

  // Initialize UI
  renderHero(activeMovie);
  renderRecommendations(activeMovie.id);
  updateWatchlistCount();

  // --------------------------------------------------------------------------
  // Render Hero Section
  // --------------------------------------------------------------------------
  function renderHero(movie) {
    activeMovie = movie;
    heroBackdrop.style.backgroundImage = `url('${movie.backdrop}')`;
    heroPoster.src = movie.poster;
    heroTitle.textContent = movie.title;
    heroOverview.textContent = movie.overview;

    // Badges
    heroMetaRow.innerHTML = `
      <span class="meta-pill highlight">★ ${movie.rating.toFixed(1)} TMDB</span>
      <span class="meta-pill">${movie.year}</span>
      <span class="meta-pill">${movie.runtime}</span>
      ${movie.genres.map(g => `<span class="meta-pill">${g}</span>`).join('')}
    `;

    // Credits
    heroCredits.innerHTML = `
      <div class="credit-item">
        <strong>DIRECTOR</strong>
        <span>${movie.director}</span>
      </div>
      <div class="credit-item">
        <strong>STARRING</strong>
        <span>${movie.cast.join(', ')}</span>
      </div>
    `;

    // Check Bookmark
    const isBookmarked = watchlist.some(m => m.id === movie.id);
    heroBookmarkIcon.textContent = isBookmarked ? '★' : '☆';
    heroBookmarkBtn.style.color = isBookmarked ? 'var(--accent-amber-light)' : '';
  }

  // --------------------------------------------------------------------------
  // Render Recommendations Grid
  // --------------------------------------------------------------------------
  function renderRecommendations(movieId) {
    const recommendations = engine.getRecommendations(movieId);
    recSubheading.textContent = `Calculated neural affinity vectors for ${activeMovie.title.toUpperCase()}`;
    moviesGrid.innerHTML = '';

    recommendations.forEach(rec => {
      const card = document.createElement('div');
      card.className = 'movie-card';
      card.innerHTML = `
        <div class="card-poster-wrapper">
          <img src="${rec.poster}" alt="${rec.title}" loading="lazy" />
          <div class="card-score-badge">${rec.matchScore}% MATCH</div>
        </div>
        <div class="card-body">
          <div class="card-title" title="${rec.title}">${rec.title}</div>
          <div class="card-meta">
            <span>★ ${rec.rating.toFixed(1)}</span>
            <span>${rec.year}</span>
          </div>
          <div class="card-genres">
            ${rec.genres.slice(0, 2).map(g => `<span class="genre-tag">${g}</span>`).join('')}
          </div>
          <div class="card-overview">${rec.overview}</div>
          <div class="card-actions">
            <button class="btn-card-action explore-btn" data-id="${rec.id}">EXPLORE</button>
            <a href="https://www.youtube.com/results?search_query=${encodeURIComponent(rec.title + ' ' + rec.year + ' trailer')}" target="_blank" class="btn-card-action" style="color:#FFF; border-color:rgba(255,255,255,0.15)">TRAILER</a>
          </div>
        </div>
      `;

      card.addEventListener('click', (e) => {
        if (e.target.tagName !== 'A' && !e.target.classList.contains('explore-btn')) {
          audio.playClick();
          openModal(rec);
        }
      });

      card.querySelector('.explore-btn').addEventListener('click', (e) => {
        e.stopPropagation();
        audio.playClick();
        renderHero(rec);
        renderRecommendations(rec.id);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      moviesGrid.appendChild(card);
    });
  }

  // --------------------------------------------------------------------------
  // Modal Handlers
  // --------------------------------------------------------------------------
  function openModal(movie) {
    currentModalMovie = movie;
    modalBackdrop.style.backgroundImage = `url('${movie.backdrop}')`;
    modalPoster.src = movie.poster;
    modalTitle.textContent = movie.title;
    modalOverview.textContent = movie.overview;
    modalDirector.textContent = movie.director;
    modalCast.textContent = movie.cast.join(', ');
    modalKeywords.textContent = movie.keywords.join(', ');
    modalMatchTag.textContent = movie.matchScore ? `${movie.matchScore}% NEURAL AFFINITY` : `★ ${movie.rating.toFixed(1)} TMDB`;

    modalChips.innerHTML = `
      <span class="meta-pill highlight">★ ${movie.rating.toFixed(1)}</span>
      <span class="meta-pill">${movie.year}</span>
      <span class="meta-pill">${movie.runtime}</span>
      ${movie.genres.map(g => `<span class="meta-pill">${g}</span>`).join('')}
    `;

    modalTrailerLink.href = `https://www.youtube.com/results?search_query=${encodeURIComponent(movie.title + ' trailer')}`;

    movieModal.classList.remove('hidden');
  }

  modalCloseBtn.addEventListener('click', () => {
    movieModal.classList.add('hidden');
  });

  movieModal.addEventListener('click', (e) => {
    if (e.target === movieModal) {
      movieModal.classList.add('hidden');
    }
  });

  modalExploreBtn.addEventListener('click', () => {
    if (currentModalMovie) {
      audio.playClick();
      movieModal.classList.add('hidden');
      renderHero(currentModalMovie);
      renderRecommendations(currentModalMovie.id);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  });

  // --------------------------------------------------------------------------
  // Hero CTA Actions
  // --------------------------------------------------------------------------
  heroRecBtn.addEventListener('click', () => {
    audio.playClick();
    renderRecommendations(activeMovie.id);
    document.querySelector('.recommendations-container').scrollIntoView({ behavior: 'smooth' });
  });

  heroTrailerBtn.addEventListener('click', () => {
    audio.playClick();
    window.open(`https://www.youtube.com/results?search_query=${encodeURIComponent(activeMovie.title + ' ' + activeMovie.year + ' trailer')}`, '_blank');
  });

  heroBookmarkBtn.addEventListener('click', () => {
    audio.playClick();
    toggleBookmark(activeMovie);
  });

  function toggleBookmark(movie) {
    const idx = watchlist.findIndex(m => m.id === movie.id);
    if (idx >= 0) {
      watchlist.splice(idx, 1);
    } else {
      watchlist.push(movie);
    }
    localStorage.setItem('cinefile_vault', JSON.stringify(watchlist));
    renderHero(activeMovie);
    updateWatchlistCount();
    renderWatchlistDrawer();
  }

  function updateWatchlistCount() {
    watchlistCount.textContent = watchlist.length;
  }

  // --------------------------------------------------------------------------
  // Watchlist Drawer
  // --------------------------------------------------------------------------
  function renderWatchlistDrawer() {
    watchlistList.innerHTML = '';
    if (watchlist.length === 0) {
      watchlistList.innerHTML = '<div style="color:var(--text-muted); font-size:0.85rem; font-family:var(--font-mono); text-align:center; padding:2rem 0;">Vault is empty. Bookmark movies to curate your list.</div>';
      return;
    }

    watchlist.forEach(m => {
      const item = document.createElement('div');
      item.className = 'watchlist-card';
      item.innerHTML = `
        <img src="${m.poster}" alt="${m.title}" />
        <div class="watchlist-card-info">
          <h4>${m.title}</h4>
          <span>${m.year} • ★ ${m.rating.toFixed(1)}</span>
        </div>
        <button class="btn-icon" style="width:30px; height:30px; font-size:0.8rem;" data-remove="${m.id}">✕</button>
      `;

      item.querySelector('[data-remove]').addEventListener('click', (e) => {
        e.stopPropagation();
        audio.playClick();
        toggleBookmark(m);
      });

      item.addEventListener('click', () => {
        audio.playClick();
        watchlistDrawer.classList.add('hidden');
        renderHero(m);
        renderRecommendations(m.id);
      });

      watchlistList.appendChild(item);
    });
  }

  watchlistToggle.addEventListener('click', () => {
    audio.playClick();
    renderWatchlistDrawer();
    watchlistDrawer.classList.remove('hidden');
  });

  drawerCloseBtn.addEventListener('click', () => {
    watchlistDrawer.classList.add('hidden');
  });

  watchlistDrawer.addEventListener('click', (e) => {
    if (e.target === watchlistDrawer) {
      watchlistDrawer.classList.add('hidden');
    }
  });

  // --------------------------------------------------------------------------
  // Search & Autocomplete with Keyboard Shortcut
  // --------------------------------------------------------------------------
  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase().trim();
    if (!q) {
      searchDropdown.classList.add('hidden');
      return;
    }

    const matches = MOVIES_DATABASE.filter(m => 
      m.title.toLowerCase().includes(q) ||
      m.director.toLowerCase().includes(q) ||
      m.cast.some(c => c.toLowerCase().includes(q))
    );

    if (matches.length === 0) {
      searchDropdown.innerHTML = '<div style="padding:1rem; color:var(--text-muted); font-size:0.8rem; font-family:var(--font-mono);">No cinematic matches found.</div>';
      searchDropdown.classList.remove('hidden');
      return;
    }

    searchDropdown.innerHTML = matches.map(m => `
      <div class="search-item" data-id="${m.id}">
        <img src="${m.poster}" class="search-item-thumb" />
        <div class="search-item-info">
          <h4>${m.title}</h4>
          <span>${m.year} • ${m.director}</span>
        </div>
      </div>
    `).join('');

    searchDropdown.classList.remove('hidden');

    searchDropdown.querySelectorAll('.search-item').forEach(item => {
      item.addEventListener('click', () => {
        const id = parseInt(item.getAttribute('data-id'), 10);
        const movie = MOVIES_DATABASE.find(m => m.id === id);
        if (movie) {
          audio.playClick();
          searchInput.value = '';
          searchDropdown.classList.add('hidden');
          renderHero(movie);
          renderRecommendations(movie.id);
        }
      });
    });
  });

  document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
      searchDropdown.classList.add('hidden');
    }
  });

  // Keyboard shortcut '/'
  window.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
    } else if (e.key === 'Escape') {
      movieModal.classList.add('hidden');
      watchlistDrawer.classList.add('hidden');
      searchDropdown.classList.add('hidden');
    }
  });

  // --------------------------------------------------------------------------
  // Genre Filter Buttons
  // --------------------------------------------------------------------------
  filterChips.querySelectorAll('.chip').forEach(chip => {
    chip.addEventListener('click', () => {
      audio.playClick();
      filterChips.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeGenre = chip.getAttribute('data-genre');

      const matching = activeGenre === 'All' 
        ? MOVIES_DATABASE 
        : MOVIES_DATABASE.filter(m => m.genres.includes(activeGenre));

      if (matching.length > 0) {
        renderHero(matching[0]);
        renderRecommendations(matching[0].id);
      }
    });
  });

  // --------------------------------------------------------------------------
  // Prediction Matrix Oracle Controller
  // --------------------------------------------------------------------------
  const predictionBtn = document.getElementById('predictionBtn');
  const heroPredictBtn = document.getElementById('heroPredictBtn');
  const predictionModal = document.getElementById('predictionModal');
  const predModalCloseBtn = document.getElementById('predModalCloseBtn');
  const predGenre = document.getElementById('predGenre');
  const predDirector = document.getElementById('predDirector');
  const predBudget = document.getElementById('predBudget');
  const predRatingVal = document.getElementById('predRatingVal');
  const predCriticsVal = document.getElementById('predCriticsVal');
  const predRoiVal = document.getElementById('predRoiVal');
  const barDirVal = document.getElementById('barDirVal');
  const barDirFill = document.getElementById('barDirFill');
  const barConceptVal = document.getElementById('barConceptVal');
  const barConceptFill = document.getElementById('barConceptFill');

  function calculatePredictions() {
    const genre = predGenre.value;
    const dir = predDirector.value;
    const budget = predBudget.value;

    let dirScore = 75;
    let baseRating = 7.2;
    let criticsScore = 78;
    let roi = 2.4;

    if (dir === 'auteur') { dirScore = 95; baseRating += 1.5; criticsScore += 16; roi += 1.2; }
    else if (dir === 'veteran') { dirScore = 85; baseRating += 0.9; criticsScore += 8; roi += 0.8; }
    else if (dir === 'indie') { dirScore = 78; baseRating += 0.6; criticsScore += 12; roi += 1.6; }
    else { dirScore = 60; baseRating += 0.1; criticsScore -= 5; roi += 0.4; }

    if (budget === 'mega') { roi *= 0.85; }
    else if (budget === 'indie') { roi *= 1.4; baseRating += 0.3; }

    const finalRating = Math.min(9.4, baseRating).toFixed(1);
    const finalCritics = Math.min(98, criticsScore);
    const finalRoi = roi.toFixed(1);

    predRatingVal.textContent = `★ ${finalRating} / 10`;
    predCriticsVal.textContent = `${finalCritics}%`;
    predRoiVal.textContent = `${finalRoi}x ROI`;

    barDirVal.textContent = `${dirScore}%`;
    barDirFill.style.width = `${dirScore}%`;

    const conceptScore = Math.min(96, Math.round(75 + (genre === 'Sci-Fi' ? 14 : 8)));
    barConceptVal.textContent = `${conceptScore}%`;
    barConceptFill.style.width = `${conceptScore}%`;
  }

  [predGenre, predDirector, predBudget].forEach(el => {
    if (el) el.addEventListener('change', calculatePredictions);
  });

  if (predictionBtn) {
    predictionBtn.addEventListener('click', () => {
      audio.playClick();
      calculatePredictions();
      predictionModal.classList.remove('hidden');
    });
  }

  if (heroPredictBtn) {
    heroPredictBtn.addEventListener('click', () => {
      audio.playClick();
      calculatePredictions();
      predictionModal.classList.remove('hidden');
    });
  }

  if (predModalCloseBtn) {
    predModalCloseBtn.addEventListener('click', () => {
      predictionModal.classList.add('hidden');
    });
  }

  if (predictionModal) {
    predictionModal.addEventListener('click', (e) => {
      if (e.target === predictionModal) {
        predictionModal.classList.add('hidden');
      }
    });
  }

  // Sound Toggle
  soundToggle.addEventListener('click', () => {
    audio.enabled = !audio.enabled;
    soundIcon.textContent = audio.enabled ? '🔊' : '🔇';
    audio.playClick();
  });
});
