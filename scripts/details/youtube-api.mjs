import { YOUTUBE_API_KEY, YOUTUBE_BASE_URL } from '../config.mjs';

export async function getTrailerFromYouTube(movieTitle) {
    const searchQuery = `${movieTitle} official trailer`;
    const youtubeSearchUrl = `${YOUTUBE_BASE_URL}?part=snippet&q=${encodeURIComponent(searchQuery)}&maxResults=1&type=video&key=${YOUTUBE_API_KEY}`;

try {
        const response = await fetch(youtubeSearchUrl);
        
        if (!response.ok) {
            const errorData = await response.json(); 
        
            const detailedMessage = errorData.error 
                ? `${response.status} (${errorData.error.reason}): ${errorData.error.message}` 
                : `YouTube API HTTP error! status: ${response.status}`;
            
            throw new Error(detailedMessage);
        }

    } catch (error) {
        console.error("Error fetching trailer from YouTube API:", error);
        return null;
    }
}