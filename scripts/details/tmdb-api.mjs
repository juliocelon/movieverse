
import { TMDB_API_KEY, TMDB_BASE_URL, LANGUAGE } from '../config.mjs';

export async function loadMovieDetail(movieId) {
    const movieDetailUrl = `${TMDB_BASE_URL}/movie/${movieId}?api_key=${TMDB_API_KEY}&language=${LANGUAGE}`;
    
    const detailResponse = await fetch(movieDetailUrl);
    if (!detailResponse.ok) {
        throw new Error(`Movie details HTTP error! status: ${detailResponse.status}`);
    }
    return detailResponse.json();
}

export async function loadMovieReviews(movieId) {
    const reviewsUrl = `${TMDB_BASE_URL}/movie/${movieId}/reviews?api_key=${TMDB_API_KEY}&language=${LANGUAGE}`;
    const commentsContainer = document.querySelector('.reviews-container');

    try {
        const response = await fetch(reviewsUrl);
        if (!response.ok) throw new Error(`Reviews HTTP error! status: ${response.status}`);
        
        const data = await response.json();
        const latestReviews = data.results.slice(0, 3); 

        latestReviews.forEach(review => {
            const author = review.author_details.username || review.author;
            const content = review.content.length > 300 
                ? review.content.substring(0, 300) + '...'
                : review.content;
            
            const rating = review.author_details.rating ? `(⭐️ ${review.author_details.rating}/10)` : '';

            const commentHTML = `
                <div class="comment tmdb-review">
                    <span class="username">${author} ${rating}:</span> "${content}"
                </div>
            `;
            
            // Insert at the end (beforeend) so they appear after the local comments.
            commentsContainer.insertAdjacentHTML('beforeend', commentHTML);
        });

    } catch (error)
    {
        console.error("Error loading movie reviews:", error);
    }
}