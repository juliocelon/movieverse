const MOVIES_DATA = {
    '101': {
        title: "The Neon Samurai",
        year: 2024,
        rating: "8.5/10",
        genre: "Sci-Fi, Action",
        release: "2024-03-15",
        overview: "In a cyberpunk future, a retired samurai must once again wield his laser katana to protect the last free city from corruption.",
        posterUrl: "https://placehold.co/250x375/007bff/ffffff?text=Poster+101"
    },
    '102': {
        title: "Lost in the Woods",
        year: 2023,
        rating: "7.2/10",
        genre: "Drama, Thriller",
        release: "2023-11-01",
        overview: "A couple becomes lost in a dense forest during a vacation, revealing dark secrets as they struggle to survive.",
        posterUrl: "https://placehold.co/250x375/ff4500/ffffff?text=Poster+102"
    }
};

function loadMovieDetails() {
    const urlParams = new URLSearchParams(window.location.search);
    const movieId = urlParams.get('id');

    if (!movieId) {
        console.error("Movie ID not found in the URL.");
        document.querySelector('.movie-title').textContent = "Error: Movie not found.";
        return;
    }

    const movie = MOVIES_DATA[movieId];

    if (movie) {
        document.querySelector('.movie-title').textContent = `${movie.title} (${movie.year})`;

        const metaInfo = document.querySelector('.meta-info');
        metaInfo.innerHTML = `
            <span class="rating">${movie.rating}</span>
            <span class="genre">${movie.genre}</span>
            <span class="release-date">${movie.release}</span>
        `;

        document.querySelector('.overview-text').textContent = movie.overview;

        const poster = document.querySelector('.movie-poster-placeholder');
        poster.style.backgroundImage = `url(${movie.posterUrl})`;
        poster.style.backgroundSize = 'cover';
        poster.style.backgroundColor = 'transparent';
        poster.textContent = '';
    } else {
        document.querySelector('.movie-title').textContent = `Movie with ID ${movieId} not found.`;
    }
}

document.addEventListener('DOMContentLoaded', loadMovieDetails);
