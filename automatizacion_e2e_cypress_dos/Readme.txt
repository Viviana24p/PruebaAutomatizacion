Requisitos previos
- Tener Node.js instalado.
- Tener Cypress instalado en el proyecto:
- Conexión a internet (la API es pública).

Casos de prueba

1. Registro de usuario nuevo

- Se envía un POST a /signup con un username único (se usa Date.now() para evitar duplicados).
- Se loguea la respuesta completa para depuración.

2. Registro de usuario existente

- Se envía un POST a /signup con un username ya registrado.
- La respuesta esperada es:
{ "errorMessage": "This user already exist." }
- Se valida que el body tenga la propiedad errorMessage.
- Se comprueba que el mensaje sea "This user already exist.".
- Se loguea la respuesta para depuración.

3. Login exitoso

- Se envía un POST a /login con credenciales válidas (usuario y contraseña correctos).
- Se valida que el status sea 200.
- Se comprueba que el body incluya la palabra "Auth_token".
- Se loguea la respuesta completa para depuración.

4. Login fallido

- Se envía un POST a /login con credenciales inválidas o un usuario inexistente.
- Se valida que el status sea 200.
- Se comprueba que el body tenga la propiedad errorMessage.
- Se valida que el mensaje corresponda al error esperado ("Wrong password.").
- Se loguea la respuesta completa para depuración.

Ejecución
- Abrir Cypress con: npx cypress open
- Seleccionar el archivo de prueba y ejecutar.
