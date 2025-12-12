import { YOUTUBE_API_KEY, YOUTUBE_BASE_URL } from '../config.mjs';

/**
 * Busca el trailer oficial en YouTube usando la API de búsqueda.
 * @param {string} movieTitle - El título de la película a buscar.
 * @returns {Promise<string|null>} El ID del video de YouTube o null si falla o no se encuentra.
 */
export async function getTrailerFromYouTube(movieTitle) {
    const searchQuery = `${movieTitle} official trailer`;
    const youtubeSearchUrl = `${YOUTUBE_BASE_URL}?part=snippet&q=${encodeURIComponent(searchQuery)}&maxResults=1&type=video&key=${YOUTUBE_API_KEY}`;

    try {
        const response = await fetch(youtubeSearchUrl);
        
        if (!response.ok) {
            // Manejo de errores HTTP de la API de YouTube
            const errorData = await response.json().catch(() => ({})); 
        
            const detailedMessage = errorData.error 
                ? `${response.status} (${errorData.error.reason}): ${errorData.error.message}` 
                : `YouTube API HTTP error! status: ${response.status}`;
            
            console.error("YouTube API error details:", detailedMessage);
            return null; // Devuelve null si la API falla
        }

        const data = await response.json();
        
        if (data.items && data.items.length > 0) {
            // Retorna el ID del video si se encuentra
            return data.items[0].id.videoId;
        }

        return null; // Retorna null si no hay resultados
    } catch (error) {
        console.error("Error fetching trailer from YouTube API (network/parse error):", error);
        return null;
    }
}