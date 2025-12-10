// La clave secreta SÍ es accesible aquí porque es código de servidor (serverless)
console.log('EMPEZANDO 2');
const API_KEY = process.env.YOUTUBE_API_KEY;
// const stripe = require('stripe')(API_KEY); // Ejemplo usando una librería
console.log('AQUI 2');
exports.handler = async (event, context) => {
  if (!API_KEY) {
    return { statusCode: 500, body: 'Clave de API no configurada en el entorno de Netlify' };
  }

  try {
    // 1. Lógica de negocio (ej. crear un pago, buscar un recurso)
    // 2. Aquí llamas a la API de terceros (Stripe, Twilio, etc.) usando la API_KEY
    const resultado = { data: "datos seguros de la api" }; 

    // Devuelve los resultados al frontend
    return {
      statusCode: 200,
      body: JSON.stringify(resultado),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};