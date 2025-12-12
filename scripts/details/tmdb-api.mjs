import { TMDB_API_KEY, TMDB_BASE_URL, LANGUAGE } from '../config.mjs';

export async function loadMovieDetail(movieId) {
    const movieDetailUrl = `${TMDB_BASE_URL}/movie/${movieId}?api_key=${TMDB_API_KEY}&language=${LANGUAGE}`;
    
    const detailResponse = await fetch(movieDetailUrl);
    if (!detailResponse.ok) {
        throw new Error(`Movie details HTTP error! status: ${detailResponse.status}`);
    }
    return detailResponse.json();
}

/**
 * Carga el video del trailer de YouTube para una película desde TMDB (Endpoint /videos).
 * @param {number} movieId - El ID de la película.
 * @returns {Promise<string|null>} El ID del video de YouTube o null si no se encuentra.
 */
export async function loadMovieTrailerVideo(movieId) {
    const videosUrl = `${TMDB_BASE_URL}/movie/${movieId}/videos?api_key=${TMDB_API_KEY}&language=${LANGUAGE}`;

    try {
        const response = await fetch(videosUrl);
        if (!response.ok) {
            throw new Error(`TMDB Videos HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Buscar el primer video que sea de tipo 'Trailer' o 'Teaser' y esté en YouTube.
        const trailer = data.results.find(video =>
            video.site === 'YouTube' &&
            (video.type === 'Trailer' || video.type === 'Teaser')
        );

        // Retorna la clave del video de YouTube (el ID)
        return trailer ? trailer.key : null;

    } catch (error) {
        console.error("Error loading movie trailer from TMDB:", error);
        return null;
    }
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