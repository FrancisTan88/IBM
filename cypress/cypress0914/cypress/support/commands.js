// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add('$_WaitLoading', () => {
  cy.get('p-progressspinner', { timeout: 60000 }).should('be.not.visible');
  cy.wait(1000);

  cy.get('p-blockui').then(($loading) => {
    if($loading.children().length === 0) {
      cy.log('----- wait -----')
      cy.$_WaitLoading();
    }

    // cy.wrap($loading).invoke('attr', 'ng-reflect-blocked').then(attr => {
    //   if (attr.includes('true')) {
    //     cy.$_WaitLoading();
    //   }
    // })
  });
  
});

Cypress.Commands.add('$_Login', (email) => {
  cy.intercept('GET', 'http://10.164.71.100/ingress/my/system-management/Rbac/Permission/User/**').as('Login');

  cy.get('.p-inputtext').type(email);
  cy.contains('button', 'Login').click();
  cy.wait('@Login', { timeout: 30000 });
  cy.$_WaitLoading();
});

Cypress.Commands.add('$_ClickTodoCard', (cardStatus, workflowStage) => {
  cy.get(`.card-header:contains(${cardStatus})`).closest('.card').contains(workflowStage).click();
});

Cypress.Commands.add('$_ClickTab', (tabname) => {  // This is a func about top tab
  cy.get('[role=presentation]').contains(tabname).click();
});

Cypress.Commands.add('$_GetTableRow', (key, parent = 'sigv-data-table') => {
  cy.get(parent).contains('tr', key); // sigv-check-list
});

Cypress.Commands.add('$_ClickTable', (caseNo) => {
  cy.$_GetTableRow(caseNo).find('a').click();
  cy.$_WaitLoading();
});

Cypress.Commands.add('$_Action', (action) => {
  cy.$_WaitLoading();
  cy.contains('button[pbutton]', action, { timeout: 30000 }).should('be.visible').click();
});

Cypress.Commands.add('$_SearchField', (fieldname, caseNo) => {
  cy.get('.p-field-label').contains(fieldname).next().type(caseNo);
  cy.$_Action('Search');
});

Cypress.Commands.add('$_CheckState', (caseNo, state) => {
  cy.$_GetTableRow(caseNo).contains(state);
});

Cypress.Commands.add('$_TypeText', (label, text) => {
  cy.contains('.p-field', label).find('.p-inputtext').type(text);
});

Cypress.Commands.add('$_TypeComment', (label, comment) => {
  cy.contains('.p-field', label).find('.p-inputtextarea').type(comment);
});

Cypress.Commands.add('$_ClickDropDownList', (label) => {
  cy.contains('.p-field', label).find('.p-dropdown').click();
  cy.wait(300);
});

Cypress.Commands.add('$_ClickCheckbox', (label) => {
  cy.contains('.p-field', label).find('.p-checkbox').click();
});

Cypress.Commands.add('$_SelectDropDownItem', (value) => {
  cy.contains('p-dropdownitem', value).first().click();
  cy.wait(300);
});

Cypress.Commands.add('$_SelectDropDown', (label, value) => {
  cy.$_ClickDropDownList(label);
  cy.$_SelectDropDownItem(value);
});

Cypress.Commands.add('$_CheckToaster', (message) => {
  cy.get('p-toast').contains(message).should('be.visible');
});
