// dom-utils.mjs - CORRECTED VERSION

import { IMAGE_BASE_URL } from './config.mjs';

export function createMovieCardHTML(movie) {
    const movieId = movie.id;
    const posterPath = movie.poster_path;
    const movieTitle = movie.title;
    
    const posterUrl = posterPath 
        ? `${IMAGE_BASE_URL}${posterPath}` 
        : 'https://placehold.co/250x375/333333/ffffff?text=No+Poster';

    // CHANGE: Removed inline background styles and added an <img> tag.
    return `
        <a href="movie-detail.html?id=${movieId}" 
           class="movie-card" 
           aria-label="View details for ${movieTitle}">
            
            <img src="${posterUrl}" 
                 alt="Poster for ${movieTitle}" 
                 class="movie-poster"> 
                 
        </a>
    `;
}

export function initializeGenreResultsSection() {
    const resultsContainer = document.querySelector('.genre-results .movie-cards');
    const resultsTitle = document.querySelector('.genre-results h2');
    
    if (!resultsContainer || !resultsTitle) return;
    
    resultsTitle.textContent = "Genre Results";
    resultsContainer.innerHTML = '<p>Select a genre above to see movies here.</p>';
}

export function displayMovieCards(selector, movies) {
    const movieCardsContainer = document.querySelector(selector);
    if (!movieCardsContainer) return;
    
    movieCardsContainer.innerHTML = ''; 

    if (movies.length === 0)
    {
        movieCardsContainer.innerHTML = '<p>No movies found.</p>';
        return;
    }

    movies.forEach(movie => {
        const movieCardHTML = createMovieCardHTML(movie);
        movieCardsContainer.insertAdjacentHTML('beforeend', movieCardHTML);
    });
}