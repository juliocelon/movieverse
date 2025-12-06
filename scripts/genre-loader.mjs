import { fetchPopularMovies, fetchMoviesByGenre, fetchMovieDetail } from './api.mjs';
import { displayMovieCards, initializeGenreResultsSection } from './dom-utils.mjs';
import { FAVORITES_KEY } from './config.mjs';

const POPULAR_MOVIES_CONTAINER = '.popular-movies .movie-cards';
const GENRE_RESULTS_CONTAINER = '.genre-results .movie-cards';
const GENRE_TITLE_SELECTOR = '.genre-results h2';

export async function loadPopularMovies() {
    const movieCardsContainer = document.querySelector(POPULAR_MOVIES_CONTAINER);
    if (!movieCardsContainer) return;

    try {
        const popularMovies = await fetchPopularMovies();
        displayMovieCards(POPULAR_MOVIES_CONTAINER, popularMovies);
    }
    catch (error)
    {
        movieCardsContainer.innerHTML = '<p style="color: red;">Error loading popular movies.</p>';
    }
}

export async function loadFavoriteMovies() {
    const movieCardsContainer = document.querySelector(GENRE_RESULTS_CONTAINER);
    const resultsTitle = document.querySelector(GENRE_TITLE_SELECTOR);
    if (!movieCardsContainer || !resultsTitle) return;

    // 1. Get favorite IDs from sessionStorage
    const favoritesString = sessionStorage.getItem(FAVORITES_KEY);
    const favoriteIds = favoritesString ? JSON.parse(favoritesString) : [];
    
    resultsTitle.textContent = "My Favorites";
    movieCardsContainer.innerHTML = '<p>Loading favorites...</p>'; 

    if (favoriteIds.length === 0) {
        movieCardsContainer.innerHTML = '<p>You haven\'t added any movies to your favorites yet.</p>';
        return;
    }

    try {
        // 2. Fetch details for each favorite movie ID
        const moviePromises = favoriteIds.map(fetchMovieDetail);

        const favoriteMovies = await Promise.all(moviePromises);
        
        // 3. Display movie cards
        displayMovieCards(GENRE_RESULTS_CONTAINER, favoriteMovies);

    } catch (error) {
        console.error("Error loading favorite movies:", error);
        movieCardsContainer.innerHTML = '<p style="color: red;">Error loading your favorite movies.</p>';
        resultsTitle.textContent = "My Favorites"; 
    }
}

export async function loadMoviesByGenre(genreId, genreName) {
    const movieCardsContainer = document.querySelector(GENRE_RESULTS_CONTAINER);
    const resultsTitle = document.querySelector(GENRE_TITLE_SELECTOR);
    if (!movieCardsContainer || !resultsTitle) return;

    try {
        movieCardsContainer.innerHTML = '<p>Loading movies...</p>'; 
        resultsTitle.textContent = `${genreName} Hits`; 

        const moviesToShow = await fetchMoviesByGenre(genreId);
        
        displayMovieCards(GENRE_RESULTS_CONTAINER, moviesToShow);

    }
    catch (error)
    {
        movieCardsContainer.innerHTML = '<p style="color: red;">Error loading genre movies.</p>';
        resultsTitle.textContent = "Genre Results"; 
    }
}


export function initializeGenreListeners() {
    const genreLinks = document.querySelectorAll('.genre-links a');

    genreLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); 
            
            const genreId = event.currentTarget.getAttribute('data-genre-id');
            const genreName = event.currentTarget.textContent;
            
            // Logic to toggle selection and reset the section
            const isActive = event.currentTarget.classList.contains('active');
            
            genreLinks.forEach(l => l.classList.remove('active'));
            
            if (isActive) {
                // If it was active, deselect it and reset the results section
                initializeGenreResultsSection(); 
            } else {
                // If not active, select it and load by genre or favorites
                event.currentTarget.classList.add('active');
                
                if (genreId === 'favorites') {
                    loadFavoriteMovies();
                } else {
                    loadMoviesByGenre(genreId, genreName);
                }
            }
        });
    });
}