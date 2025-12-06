// local-storage.mjs
import { FAVORITES_KEY } from '../config.mjs';
import { loadMovieReviews } from './tmdb-api.mjs';


export function getFavorites() {
    const favoritesString = sessionStorage.getItem(FAVORITES_KEY);
    return favoritesString ? JSON.parse(favoritesString) : [];
}

// isAdding - If true, adds. If false, removes.
export function toggleFavorite(movieId, isAdding) {
    let favorites = getFavorites();
    const movieIdStr = String(movieId);

    if (isAdding)
    {
        if (!favorites.includes(movieIdStr))
        {
            favorites.push(movieIdStr);
        }
    }
    else
    {
        favorites = favorites.filter(id => id !== movieIdStr);
    }

    sessionStorage.setItem(FAVORITES_KEY, JSON.stringify(favorites));
    updateFavoriteButtonState(movieIdStr);
}

export function updateFavoriteButtonState(movieId) {
    const favoriteButton = document.querySelector('.favorite-button');
    if (!favoriteButton) return;

    const favorites = getFavorites();
    const isFavorite = favorites.includes(String(movieId));

    if (isFavorite)
    {
        favoriteButton.textContent = '★ Added to Favorites';
        favoriteButton.classList.add('is-favorite');
    }
    else
    {
        favoriteButton.textContent = '❤️ Add to Favorites';
        favoriteButton.classList.remove('is-favorite');
    }
}

export function initializeFavoriteButton(movieId) {
    const favoriteButton = document.querySelector('.favorite-button');
    if (!favoriteButton) return;

    updateFavoriteButtonState(movieId);

    favoriteButton.addEventListener('click', () => {
        const isCurrentlyFavorite = favoriteButton.classList.contains('is-favorite');
        toggleFavorite(movieId, !isCurrentlyFavorite);
    });
}


function loadLocalComments(movieId) {
    const commentsContainer = document.querySelector('.reviews-container');
    const storageKey = `comments_${movieId}`;
    
    const localCommentsString = sessionStorage.getItem(storageKey);
    let localComments = localCommentsString ? JSON.parse(localCommentsString) : [];

    localComments.forEach(comment => {
        const commentHTML = `
            <div class="comment local-comment">
                <span class="username">You (Local):</span> "${comment.text}"
            </div>
        `;
        commentsContainer.insertAdjacentHTML('afterbegin', commentHTML);
    });
}

export async function refreshComments(movieId) {
    const commentsContainer = document.querySelector('.reviews-container');
    commentsContainer.innerHTML = ''; 
    loadLocalComments(movieId); 
    await loadMovieReviews(movieId); 

    if (commentsContainer.children.length === 0) {
        commentsContainer.innerHTML = '<p>No reviews available for this movie.</p>';
    }
}


export function saveLocalComment(movieId, commentText) {
    const storageKey = `comments_${movieId}`;
    const newComment = { text: commentText, timestamp: Date.now() };

    const localCommentsString = sessionStorage.getItem(storageKey);
    let localComments = localCommentsString ? JSON.parse(localCommentsString) : [];

    localComments.push(newComment);
    sessionStorage.setItem(storageKey, JSON.stringify(localComments));
    
    refreshComments(movieId); 
}