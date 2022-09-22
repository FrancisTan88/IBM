/// <reference types="cypress"/>
import { navigateTo } from '../support/pageObjects/navigationPage';

describe('Commencement - Amend', () => {
  const caseNo = Cypress.env('case_no');

  beforeEach(() => {
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Amending/Submission').as('postCommencementAmendingSubmission');
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Amending/Approval').as('postCommencementAmendingApproval');
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Amending/UnderCreditReview/Submission').as('postCommencementAmendingUnderCreditReviewSubmission');

    cy.visit('http://ibm-dev-my-commencement.chailease.com.tw/');
  });

  it('CSR Apply Amend', () => {
    cy.$_Login(Cypress.env('cs').email);

    navigateTo.amendPage();

    // Search 'contract No'
    cy.$_SearchField('Contract No.', caseNo);
    cy.$_ClickTable(caseNo);

    cy.url().should('include', '/amend-apply/detail');
    cy.$_WaitLoading();

    cy.$_SelectDropDown('Reason of Amendment', 'Input Error')

    cy.$_TypeComment('Instruction', 'Restore - Invalid');

    //-----------------------------
    // Guarantor / Contact Person
    cy.$_ClickTab('Guarantor / Contact Person');

    if (['Jayson001', 'Jayson002', 'Jayson003'].includes(caseNo)) {

      cy.get('p-card.guarantor-card').eq(0).then($GuarantorCard => {

        cy.wrap($GuarantorCard).find('[formcontrolname=registeredAddressModel]').find('p-dropdown').eq(0).click();
        cy.$_SelectDropDownItem("Johor")

        cy.wrap($GuarantorCard).find('[formcontrolname=registeredAddressModel]').find('p-dropdown').eq(1).click();
        cy.$_SelectDropDownItem("Ayer Baloi")

        cy.wrap($GuarantorCard).find('[formcontrolname=contactAddressModel]').find('p-dropdown').eq(0).click();
        cy.$_SelectDropDownItem("Johor")

        cy.wrap($GuarantorCard).find('[formcontrolname=contactAddressModel]').find('p-dropdown').eq(1).click();
        cy.$_SelectDropDownItem("Ayer Baloi")

        cy.wrap($GuarantorCard).find('[formcontrolname=workAddressModel]').find('p-dropdown').eq(0).click();
        cy.$_SelectDropDownItem("Johor")

        cy.wrap($GuarantorCard).find('[formcontrolname=workAddressModel]').find('p-dropdown').eq(1).click();
        cy.$_SelectDropDownItem("Ayer Baloi")

        cy.wrap($GuarantorCard).find('[formcontrolname=workAddressModel]').find('input[pinputtext]').eq(0).type('my work address');
      });
    }

    if (['Jayson001', 'Jayson003'].includes(caseNo)) {
      //-----------------------------
      // Customer Information
      cy.$_ClickTab('Customer Information');

      cy.contains('Contact Information').parentsUntil('p-accordiontab').then($ContactTab => {

        cy.wrap($ContactTab).find('[formcontrolname=registeredAddressModel]').find('p-dropdown').eq(0).click();
        cy.$_SelectDropDownItem("Johor")

        cy.wrap($ContactTab).find('[formcontrolname=registeredAddressModel]').find('p-dropdown').eq(1).click();
        cy.$_SelectDropDownItem("Ayer Baloi")

        cy.wrap($ContactTab).find('[formcontrolname=contactAddressModel]').find('p-dropdown').eq(0).click();
        cy.$_SelectDropDownItem("Johor")

        cy.wrap($ContactTab).find('[formcontrolname=contactAddressModel]').find('p-dropdown').eq(1).click();
        cy.$_SelectDropDownItem("Ayer Baloi")
      })

      cy.contains('Work Information').parent().find('[formcontrolname=civilServant]').click();
      cy.wait(500);
      cy.$_SelectDropDownItem("Civilian");

      cy.contains('Work Information').parent().find('[formcontrolname=position]').type('CEO');
    }

    cy.$_Action('Submit');

    // Vehicle Alert
    cy.get('[role=dialog]').find('button').contains('OK').click({ force: true });
    cy.wait('@postCommencementAmendingSubmission', { timeout: 30000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('csManager').name);
  });

  it('CSR Manager Approve Amend', () => {
    cy.$_Login(Cypress.env('csManager').email);
    navigateTo.todoCard('Commencement Amending Application', 'Under Review');
    cy.$_ClickTable(caseNo);
    cy.url().should('include', '/amend-apply/review');

    cy.$_Action('Submit');
    cy.wait('@postCommencementAmendingApproval', { timeout: 30000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster('MY00032 Muhammad Iman Firdaus');
    // cy.$_CheckToaster('MY00242 Yee Choon Thye');
    cy.url().should('include', '/amend-apply/review');
  });

  it('Credit Approve Amend', () => {
    cy.$_Login(Cypress.env('amendCredit').email);

    navigateTo.todoCard('Commencement Amending Application', 'Under Credit Review');
    cy.$_ClickTable(caseNo);
    cy.url().should('include', '/amend-apply/review');

    cy.$_Action('Submit');

    // Vehicle Alert
    cy.get('[role=dialog]').find('button').contains('OK').click({ force: true });
    cy.wait('@postCommencementAmendingUnderCreditReviewSubmission', { timeout: 30000 });

    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('amendCreditManager').name);
    cy.url().should('include', '/amend-apply/review');
  });

  it('Credit Manager Approve Amend', () => {
    cy.$_Login(Cypress.env('amendCreditManager').email);
    navigateTo.todoCard('Commencement Amending Application', 'Under Credit Manager Review');
    cy.$_ClickTable(caseNo);
    cy.url().should('include', '/amend-apply/review');

    cy.$_Action('Submit');
    cy.wait('@postCommencementAmendingApproval', { timeout: 30000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster('04063 Chad Ueng');
    cy.url().should('include', '/amend-apply/review');
  });

  it('Senior Credit Manager Approve Amend', () => {
    cy.$_Login(Cypress.env('creditSeniorManager').email);
    navigateTo.todoCard('Commencement Amending Application', 'Under Credit Manager Review');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postCommencementAmendingApproval', { timeout: 30000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('cs').name);
    cy.url().should('include', '/amend-apply/review');
  });

  it('CSR Confirm Amend', () => {
    cy.$_Login(Cypress.env('cs').substitute);
    cy.$_ClickTab('Substitute');
    navigateTo.todoCard('Commencement Amending Application', 'Amend Confirm');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postCommencementAmendingApproval', { timeout: 30000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster('Process End');
    cy.url().should('include', '/amend-apply/review');
  });
});