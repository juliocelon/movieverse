const TMDB_API_KEY = "63db0bb97ae40877eb2984aee64f3488";
const TMDB_BASE_URL = "https://api.themoviedb.org/3";
const IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500";
const DEFAULT_MOVIE_COUNT = 7; 

function createMovieCardHTML(movie) {
    const movieId = movie.id;
    const posterPath = movie.poster_path;
    const posterUrl = posterPath 
        ? `${IMAGE_BASE_URL}${posterPath}` 
        : 'https://placehold.co/250x375/333333/ffffff?text=No+Poster';

    return `
        <a href="movie-detail.html?id=${movieId}" 
           class="movie-card" 
           style="background-image: url('${posterUrl}'); 
                  background-size: cover; 
                  background-position: center;">
        </a>
    `;
}

async function loadPopularMovies() {
    const movieCardsContainer = document.querySelector('.popular-movies .movie-cards');
    if (!movieCardsContainer) return;

    const url = `${TMDB_BASE_URL}/movie/popular?api_key=${TMDB_API_KEY}&language=es-ES&page=1`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
        
        const data = await response.json();
        const popularMovies = data.results.slice(0, DEFAULT_MOVIE_COUNT);

        movieCardsContainer.innerHTML = ''; 

        popularMovies.forEach(movie => {
            const movieCardHTML = createMovieCardHTML(movie);
            movieCardsContainer.insertAdjacentHTML('beforeend', movieCardHTML);
        });

    } catch (error) {
        console.error("Error loading popular movies:", error);
        movieCardsContainer.innerHTML = '<p style="color: red;">Error loading popular movies.</p>';
    }
}

async function loadMoviesByGenre(genreId, genreName) {
    const movieCardsContainer = document.querySelector('.favorites .movie-cards');
    const favoritesTitle = document.querySelector('.favorites h2');
    
    const url = `${TMDB_BASE_URL}/discover/movie?api_key=${TMDB_API_KEY}&with_genres=${genreId}&language=es-ES&sort_by=popularity.desc&page=1`;

    if (!movieCardsContainer || !favoritesTitle) return;

    try {
        movieCardsContainer.innerHTML = '<p>Loading movies...</p>'; 
        favoritesTitle.textContent = `${genreName} Hits`; 

        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
        
        const data = await response.json();
        const moviesToShow = data.results.slice(0, DEFAULT_MOVIE_COUNT); 

        movieCardsContainer.innerHTML = ''; 

        if (moviesToShow.length === 0) {
            movieCardsContainer.innerHTML = `<p>No ${genreName} movies found.</p>`;
            return;
        }

        moviesToShow.forEach(movie => {
            const movieCardHTML = createMovieCardHTML(movie);
            movieCardsContainer.insertAdjacentHTML('beforeend', movieCardHTML);
        });

    } catch (error) {
        console.error(`Error loading ${genreName} movies:`, error);
        movieCardsContainer.innerHTML = '<p style="color: red;">Error loading genre movies.</p>';
        favoritesTitle.textContent = "Favorites"; 
    }
}

function initializeGenreListeners() {
    const genreLinks = document.querySelectorAll('.genre-links a');
    
    genreLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); 
            
            const genreId = event.currentTarget.getAttribute('data-genre-id');
            const genreName = event.currentTarget.textContent;
            
            if (genreId) {
                genreLinks.forEach(l => l.classList.remove('active'));
                event.currentTarget.classList.add('active');
                
                loadMoviesByGenre(genreId, genreName);
            }
        });
    });
}


document.addEventListener('DOMContentLoaded', () => {
    loadPopularMovies(); 
    
    initializeGenreListeners();
    
    loadMoviesByGenre(28, "Action"); 
});