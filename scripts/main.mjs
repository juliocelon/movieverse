import { loadPopularMovies, initializeGenreListeners, loadMoviesByGenre } from './genre-loader.mjs';
import { initializeSearchBarListener } from './search.mjs';
import { initializeGenreResultsSection } from './dom-utils.mjs';

document.addEventListener('DOMContentLoaded', () => {

    loadPopularMovies(); 
    initializeGenreListeners();
    initializeSearchBarListener(); 
    
    initializeGenreResultsSection(); 
    
    const defaultGenreId = "28";
    const defaultGenreName = "Action";
    
    loadMoviesByGenre(defaultGenreId, defaultGenreName);
    
    // Mark the Action link as active
    const actionLink = document.querySelector(`.genre-links a[data-genre-id="${defaultGenreId}"]`);
    if (actionLink) {
        actionLink.classList.add('active');
    }
});