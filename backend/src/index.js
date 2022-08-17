const app = require('./app');

require('./firebae')

// Inicializamos el servidor 
app.listen(3000);
console.log('Serve is running on port 3000');