const TMDB_API_KEY = "63db0bb97ae40877eb2984aee64f3488";
const TMDB_BASE_URL = "https://api.themoviedb.org/3";
const IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500";

async function loadPopularMovies() {
    const movieCardsContainer = document.querySelector('.popular-movies .movie-cards');
    if (!movieCardsContainer) return;

    const url = `${TMDB_BASE_URL}/movie/popular?api_key=${TMDB_API_KEY}&language=es-ES&page=1`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
        
        const data = await response.json();
        const popularMovies = data.results.slice(0, 5);

        movieCardsContainer.innerHTML = ''; 

        popularMovies.forEach(movie => {
            const movieId = movie.id;
            const posterPath = movie.poster_path;
            const posterUrl = posterPath 
                ? `${IMAGE_BASE_URL}${posterPath}` 
                : 'https://placehold.co/250x375/333333/ffffff?text=No+Poster';

            const movieCardHTML = `
                <a href="movie-detail.html?id=${movieId}" 
                   class="movie-card" 
                   style="background-image: url('${posterUrl}'); 
                          background-size: cover; 
                          background-position: center;">
                </a>
            `;
            movieCardsContainer.insertAdjacentHTML('beforeend', movieCardHTML);
        });

    } catch (error) {
        console.error("Error loading popular movies:", error);
        movieCardsContainer.innerHTML = '<p style="color: red;">Error loading movies.</p>';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.popular-movies .movie-cards')) {
        loadPopularMovies();
    }
});
