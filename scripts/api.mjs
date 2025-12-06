import { 
    TMDB_API_KEY, 
    TMDB_BASE_URL, 
    LANGUAGE, 
    DEFAULT_MOVIE_COUNT 
} from './config.mjs';


async function tmdbFetch(path, params = {}) {
    // Construct query string
    const queryString = new URLSearchParams({
        api_key: TMDB_API_KEY,
        language: LANGUAGE,
        ...params
    }).toString();
    
    const url = `${TMDB_BASE_URL}${path}?${queryString}`;

    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status} from ${path}`);
    }
    
    return response.json();
}

export async function fetchPopularMovies() {
    try {
        const data = await tmdbFetch('/movie/popular', { page: 1 });
        return data.results.slice(0, DEFAULT_MOVIE_COUNT);
    } catch (error) {
        console.error("Error fetching popular movies:", error);
        throw error;
    }
}

export async function fetchMoviesByGenre(genreId) {
    try {
        const data = await tmdbFetch('/discover/movie', {
            with_genres: genreId,
            sort_by: 'popularity.desc',
            page: 1
        });
        return data.results.slice(0, DEFAULT_MOVIE_COUNT);
    } catch (error) {
        console.error(`Error fetching movies by genre ${genreId}:`, error);
        throw error;
    }
}

export async function fetchMovieDetail(movieId) {
    try {
        return await tmdbFetch(`/movie/${movieId}`);
    } catch (error) {
        console.error(`Error fetching movie detail for ID ${movieId}:`, error);
        throw error;
    }
}

export async function fetchMovieSearch(query) {
    if (!query || query.length < 3) return [];
    
    try {
        const data = await tmdbFetch('/search/movie', {
            query: encodeURIComponent(query),
            page: 1
        });

        return data.results.slice(0, DEFAULT_MOVIE_COUNT); 
    } catch (error) {
        console.error("Error fetching movie search:", error);
        throw error;
    }
}