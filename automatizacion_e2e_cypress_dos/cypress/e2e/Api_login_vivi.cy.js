describe('Login en Demoblaze API', () => {
  it('Ingreso de un usuario existente en el API de Demoblaze (Login)', () => {
  cy.request({
    method: 'POST',
    url: 'https://api.demoblaze.com/login',
    headers: { 'Content-Type': 'application/json' },
    body: {
      username: 'vivi_nuevo1',
      password: 'Contraseña123!'
    }
  }).then((response) => {
    expect(response.status).to.eq(200);

    // Validar que contenga Auth_token
    expect(response.body).to.include('Auth_token');

    // La respuesta es un string, no JSON
    cy.log('Respuesta completa: ' + response.body);
    
  });
});

it('Ingreso fallido en el API de Demoblaze (Login)', () => {
  cy.request({
    method: 'POST',
    url: 'https://api.demoblaze.com/login',
    headers: { 'Content-Type': 'application/json' },
    body: {
      username: 'vivi_nuevo1',
      password: 'Contraseña1234!'
    }
  }).then((response) => {
    expect(response.status).to.eq(200);

    // Validar que el body tenga la propiedad errorMessage
    expect(response.body).to.have.property('errorMessage');

    // Validar que el mensaje sea de usuario existente
    expect(response.body.errorMessage).to.eq('Wrong password.');

    // Log del mensaje
    cy.log('Mensaje de respuesta: ' + response.body.errorMessage);
    
  });
});

})