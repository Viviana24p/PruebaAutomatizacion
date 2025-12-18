describe('Registro en Demoblaze API', () => {
  
  it('Registro de un usuario nuevo en el API de Demoblaze (SignUp)', () => {
  cy.request({
    method: 'POST',
    url: 'https://api.demoblaze.com/signup',
    headers: { 'Content-Type': 'application/json' },
    body: {
      username: 'vivi_' + Date.now(), // Para evitar duplicidad se pone la fecha actual
      password: 'Contraseña123!'
    }
  }).then((response) => {
    expect(response.status).to.eq(200);

    // Log completo para depuración
    cy.log('Respuesta completa: ' + JSON.stringify(response.body));

  });
});

it('Registro de un usuario existente en el API de Demoblaze (SignUp)', () => {
  cy.request({
    method: 'POST',
    url: 'https://api.demoblaze.com/signup',
    headers: { 'Content-Type': 'application/json' },
    body: {
      username: 'vivi_nuevo', // El mismo username del caso anterior
      password: 'Contraseña123!'
    }
  }).then((response) => {

    // Validar status
    expect(response.status).to.eq(200);

    // Validar que el body tenga la propiedad errorMessage
    expect(response.body).to.have.property('errorMessage');

    // Validar que el mensaje sea de usuario existente
    expect(response.body.errorMessage).to.eq('This user already exist.');

    // Log del mensaje
    cy.log('Mensaje de respuesta: ' + response.body.errorMessage);
  });
});

});

