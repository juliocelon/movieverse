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

async function obtenerDatosSeguros() {
    // Llama al endpoint generado por Netlify para tu función
    console.log('EMPEZANDO');
  const response = await fetch('..netlify/functions/get-api-key.js');
  console.log('AQUI');
  if (!response.ok) {
    throw new Error('Error al llamar a la función segura');
  }
console.log('VOY');
    const data = await response.json();
    console.log('YA FUE');
  console.log('Datos obtenidos de forma segura:', data);
}

obtenerDatosSeguros();