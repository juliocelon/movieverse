import { fetchMovieSearch } from './api.mjs';

const SEARCH_RESULTS_CONTAINER = '.search-results';
const SEARCH_BAR_SELECTOR = '.search-bar';

function displaySearchResults(movies) {
    const resultsContainer = document.querySelector(SEARCH_RESULTS_CONTAINER);
    if (!resultsContainer) return;

    if (movies.length === 0) {
        resultsContainer.innerHTML = '<div class="no-results">No movies found.</div>';
        resultsContainer.style.display = 'block';
        return;
    }

    let resultsHTML = movies.map(movie => {
        const year = movie.release_date ? new Date(movie.release_date).getFullYear() : 'N/A';
        return `
            <a href="movie-detail.html?id=${movie.id}" class="search-result-item">
                ${movie.title} (${year})
            </a>
        `;
    }).join('');

    resultsContainer.innerHTML = resultsHTML;
    resultsContainer.style.display = 'block';
}

async function searchMovies(query) {
    const resultsContainer = document.querySelector(SEARCH_RESULTS_CONTAINER);
    
    if (!query || query.length < 3) {
        resultsContainer.innerHTML = '';
        resultsContainer.style.display = 'none';
        return;
    }

    try {
        resultsContainer.innerHTML = '<div class="loading-results">Searching...</div>';
        resultsContainer.style.display = 'block';

        const searchResults = await fetchMovieSearch(query);
        
        displaySearchResults(searchResults);

    }
    catch (error)
    {
        resultsContainer.innerHTML = '<div class="error-results">Search error.</div>';
        resultsContainer.style.display = 'block';
    }
}

export function initializeSearchBarListener() {
    const searchBar = document.querySelector(SEARCH_BAR_SELECTOR);
    const resultsContainer = document.querySelector(SEARCH_RESULTS_CONTAINER);
    
    if (!searchBar || !resultsContainer) return;

    let searchTimer;
    searchBar.addEventListener('input', (event) => {
        clearTimeout(searchTimer);
        const query = event.target.value.trim();
        
        searchTimer = setTimeout(() => {
            searchMovies(query);
        }, 300); 
    });

    // Hide results when clicking outside
    document.addEventListener('click', (event) => {
        const searchContainer = document.querySelector('.search-container');
        if (searchContainer && !searchContainer.contains(event.target)) {
            resultsContainer.style.display = 'none';
        }
    });

    // Keep results visible if the bar is focused and has content
    searchBar.addEventListener('focus', () => {
        if (resultsContainer.innerHTML) {
            resultsContainer.style.display = 'block';
        }
    });
}