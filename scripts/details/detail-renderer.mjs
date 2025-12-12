import { loadMovieDetail, loadMovieTrailerVideo } from './tmdb-api.mjs'; // <-- Importa loadMovieTrailerVideo
import { getTrailerFromYouTube } from './youtube-api.mjs';
import { formatRuntime } from './utils.mjs';
import { refreshComments, saveLocalComment, initializeFavoriteButton } from './local-storage.mjs';
import { IMAGE_BASE_URL } from '../config.mjs';


function displayMovieDetails(movie, youtubeVideoId) {
    const year = movie.release_date ? new Date(movie.release_date).getFullYear() : 'N/A';
    document.querySelector('.movie-title').textContent = `${movie.title} (${year})`;
    document.title = `MovieVerse - ${movie.title}`;

    const rating = movie.vote_average ? `${movie.vote_average.toFixed(1)}/10` : 'N/A';
    const genres = movie.genres ? movie.genres.map(g => g.name).join(', ') : 'N/A';
    const runtime = formatRuntime(movie.runtime);
    const releaseDate = movie.release_date || 'N/A';

    const metaInfo = document.querySelector('.meta-info');
    metaInfo.innerHTML = `
        <span class="rating">⭐️ ${rating}</span>
        <span class="runtime">${runtime}</span>
        <span class="genre">${genres}</span>
        <span class="release-date">🗓 ${releaseDate}</span>
    `;
    
    // Overview
    document.querySelector('.overview-text').textContent = movie.overview || 'Synopsis not available.';

    // Poster
    const posterUrl = movie.poster_path 
        ? `${IMAGE_BASE_URL}${movie.poster_path}` 
        : 'https://placehold.co/250x375/333333/ffffff?text=No+Poster';
    
    const poster = document.querySelector('.movie-poster-placeholder');
    poster.style.backgroundImage = `url('${posterUrl}')`;
    poster.style.backgroundSize = 'cover';
    poster.style.backgroundColor = 'transparent';
    poster.textContent = '';
    
    // Trailer
    const trailerPlaceholder = document.querySelector('.trailer-placeholder');
    if (youtubeVideoId) { 
        // Usamos una URL de embed de YouTube estándar
        const youtubeEmbedUrl = `https://www.youtube.com/embed/${youtubeVideoId}?autoplay=0&controls=1`;
        trailerPlaceholder.innerHTML = `
            <iframe width="100%" height="400" 
                    src="${youtubeEmbedUrl}" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen
                    title="Movie Trailer">
            </iframe>
        `;
    } else
    {
        trailerPlaceholder.innerHTML = '<p>Trailer not available (Not found on YouTube).</p>';
    }
}


function initializeCommentForm(movieId) {
    const commentForm = document.getElementById('comment-form');
    if (commentForm) {
        commentForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Stop form submission
            const commentInput = document.getElementById('comment-text');
            const commentText = commentInput.value.trim();
            
            if (commentText) {
                saveLocalComment(movieId, commentText);
                commentInput.value = ''; 
            }
        });
    }
}

export async function loadMovieDetails() {
    const urlParams = new URLSearchParams(window.location.search);
    const movieId = urlParams.get('id');

    if (!movieId) {
        document.querySelector('.movie-title').textContent = "Error: Movie ID not found in URL.";
        return;
    }

    try {
        const movie = await loadMovieDetail(movieId);
        let youtubeVideoId = null;

        // 1. Intenta obtener el trailer con la API de YouTube (búsqueda)
        youtubeVideoId = await getTrailerFromYouTube(movie.title);

        if (!youtubeVideoId) {
            // 2. Si falla la búsqueda de YouTube, intenta obtener el trailer con TMDB API (videos)
            console.warn("YouTube API failed or found no results. Falling back to TMDB videos endpoint.");
            youtubeVideoId = await loadMovieTrailerVideo(movieId);
        }
        
        displayMovieDetails(movie, youtubeVideoId);
        
        await refreshComments(movieId); 

        initializeCommentForm(movieId);
        
        initializeFavoriteButton(movieId);


    } catch (error)
    {
        console.error("Error loading movie details:", error);
        document.querySelector('.movie-title').textContent = "Error: Could not load movie details from TMDB.";
    }
}