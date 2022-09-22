/// <reference types="cypress"/>
import { navigateTo } from '../support/pageObjects/navigationPage';

describe('Commencement - Repayment Schedule Restructure', () => {
  const caseNo = Cypress.env('case_no');

  beforeEach(() => {
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/RepaymentSchedule/Restructure/Submission').as('postCommencementRepaymentScheduleRestructureSubmission');
    cy.intercept('POST', 'http://10.164.67.100/ingress/financial-calculate/service/FinancialCalculate/CalculatePmt').as('postCalculatePmt');
    cy.intercept('POST', ' http://10.164.67.100/ingress/financial-calculate/service/FinancialCalculate/CalculateNPVAndIRR').as('postCalculateNPVAndIRR');

    cy.visit('http://ibm-dev-my-commencement.chailease.com.tw/');
  });

  it('CSR Apply', () => {
    cy.$_Login(Cypress.env('cs').email);

    // Go Apply Search Page
    navigateTo.repaymentScheduleRestructurePage();

    // Search 'contract No'
    cy.$_SearchField('Contract No.', caseNo);
    cy.$_ClickTable(caseNo);

    // GO Replayment Schedule Restructure Detail
    cy.url().should('include', '/repayment-schedule-restructure/detail');

    cy.$_SelectDropDown('Reason of Amendment', 'Project-based restructure');
    cy.$_TypeComment('Instruction', 'Apply Restructure');

    cy.$_SelectDropDown('credit', 'Credit');
    cy.$_SelectDropDown('legal', 'Collection');
    cy.$_SelectDropDown('others', 'Finance&Acc');

    cy.get('[formcontrolname="terms"]').clear().type('66');
    cy.get('p-checkbox[name="extension"]').click();
    cy.$_SelectDropDown('Pay By End of Month', 'Y');
    cy.$_SelectDropDown('Term of Restructure Start', '5');

    cy.contains('button', 'Generate Repayment Info').click();
    cy.wait('@postCalculatePmt');

    cy.get('[formcontrolname="monthlyPaymentAmount"]').eq(4).find('input').clear().type(800);

    cy.contains('button', 'Calculate').click();
    cy.wait('@postCalculateNPVAndIRR');

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('csManager').name);
  });

  it('CSR Manager Under Review', () => {
    cy.$_Login(Cypress.env('csManager').email);
    navigateTo.todoCard('Repayment Schedule Restructure', 'Under Review');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('csBoss').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('CSR Boss Under Review', () => {
    cy.$_Login(Cypress.env('csBoss').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Under Review');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', {
      timeout: 10000
    });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('creditManager').name);
    cy.$_CheckToaster(Cypress.env('legal').name);
    cy.$_CheckToaster(Cypress.env('financeAcc').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Credit Assigning', () => {
    cy.$_Login(Cypress.env('creditManager').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Officer Assigning (Credit)');
    cy.$_ClickTable(caseNo);

    cy.$_SelectDropDown('Comment', 'Assign To Processor');

    cy.get('.p-field-label').contains('Officer Assign').parent().next().find('p-autocomplete').click();
    cy.contains('li', 'MY00036 Suhaniza').click();

    cy.$_TypeComment('Instruction', 'Credit Review');
    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('credit').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Credit Officer Countersign', () => {
    cy.$_Login(Cypress.env('credit').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Officer Countersign (Credit)');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('creditManager').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Credit Manager Countersign', () => {
    cy.$_Login(Cypress.env('creditManager').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Manager Countersign (Credit)');
    cy.$_ClickTable(caseNo);

    cy.$_SelectDropDown('Comment', 'Recommended For Approval');

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Legal Officer Assigning', () => {
    cy.$_Login(Cypress.env('legal').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Officer Assigning (Legal)');
    cy.$_ClickTable(caseNo);

    cy.$_SelectDropDown('Comment', 'Recommended For Approval');

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('legalManager').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Legal Manager Countersign', () => {
    cy.$_Login(Cypress.env('legalManager').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Manager Countersign (Legal)');
    cy.$_ClickTable(caseNo);

    cy.$_SelectDropDown('Comment', 'Recommended For Approval');

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('financeAcc').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Other Officer Assigning', () => {
    cy.$_Login(Cypress.env('financeAcc').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Officer Assigning (Other)');
    cy.$_ClickTable(caseNo);

    cy.$_SelectDropDown('Comment', 'Recommended For Approval');

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('csBoss').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Managing Director Under Review', () => {
    cy.$_Login(Cypress.env('csBoss').email)
    navigateTo.todoCard('Repayment Schedule Restructure', 'Managing Director Under Review');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('cs').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('Sales Final Review', () => {
    cy.$_Login(Cypress.env('cs').substitute);
    cy.$_ClickTab('Substitute');
    navigateTo.todoCard('Repayment Schedule Restructure', 'Sales Final Review');
    cy.$_ClickTable(caseNo);

    // Attachment Tab
    cy.$_ClickTab('Attachment');

    cy.get('input[type=file]').selectFile({
      contents: 'cypress/fixtures/test.pdf',
      fileName: 'test.pdf',
      mimeType: 'application/pdf',
      lastModified: Date.now(),
    }, { force: true });
    cy.wait(600); // avoid unknown Error
    cy.contains('button[pbutton]', 'OK').click();

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster(Cypress.env('cs').name);
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });

  it('CSR Restructure Confirm', () => {
    cy.$_Login(Cypress.env('cs').substitute)
    cy.$_ClickTab('Substitute');
    navigateTo.todoCard('Repayment Schedule Restructure', 'Restructure Confirm');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postCommencementRepaymentScheduleRestructureSubmission', { timeout: 10000 });
    cy.$_CheckToaster('Success');
    cy.$_CheckToaster('Process End');
    cy.url().should('include', '/repayment-schedule-restructure/review');
  });
});