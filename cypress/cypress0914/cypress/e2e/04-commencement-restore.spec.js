/// <reference types="cypress"/>
import { navigateTo } from '../support/pageObjects/navigationPage';

describe('Commencement - Restore', () => {
  const caseNo = Cypress.env('case_no');

  beforeEach(() => {
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Reverse/Submission').as('postCommencementReverseSubmission');
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Document/Submission').as('postCommencementDocumentSubmission');
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Reverse/Approval').as('postCommencementReverseApproval');

    cy.visit('http://ibm-dev-my-commencement.chailease.com.tw/');
  });

  it('Document Application', () => {
    cy.$_Login(Cypress.env('cs').email);
    navigateTo.todoCard('Document Application', 'Commenced');
    cy.$_SearchField('Case No.', caseNo);
    cy.$_WaitLoading();

    cy.$_ClickTable(caseNo);
    cy.url().should('include', '/commencement-document/review');

    cy.$_Action('Submit');
    cy.wait('@postCommencementDocumentSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
  });

  it('CSR Apply Restore', () => {
    cy.$_Login(Cypress.env('cs').email);

    // Go Apply Search Page
    navigateTo.restorePage();

    // Search 'contract No'
    cy.$_SearchField('Contract No.', caseNo);
    cy.$_ClickTable(caseNo);
    cy.url().should('include', '/reverse-apply/detail');

    cy.contains('loading').should('be.not.visible');
    cy.$_WaitLoading();

    cy.$_SelectDropDown('Restore Type', 'Invalid');

    cy.$_TypeComment('Remark', 'Restore - Invalid');

    cy.$_Action('Submit');
    cy.wait('@postCommencementReverseSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
  });

  it('CSR Manager Approve Restore', () => {
    cy.$_Login(Cypress.env('csManager').email);

    cy.url().should('equal', 'http://ibm-dev-my-commencement.chailease.com.tw/#/');
    navigateTo.todoCard('Commencement Restore Application', 'Under Review');
    cy.$_ClickTable(caseNo);
    cy.url().should('include', '/reverse-apply/review');
    cy.$_WaitLoading();

    cy.$_Action('Submit');
    cy.wait('@postCommencementReverseApproval', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.url().should('include', '/reverse-apply/review');
  });

  it('CSR Check Search State', () => {
    cy.$_Login(Cypress.env('cs').email);

    // Go Apply Search Page
    navigateTo.searchPage();

    cy.$_SearchField('Contract No.', caseNo);
    cy.$_CheckState(caseNo, 'Uncommencement / Credit Completed'); // Credit Approve
  });

});
