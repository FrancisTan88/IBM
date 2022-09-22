<reference types="cypress"/>   /// refer to the cypress.config.js
import { navigateTo } from '../support/pageObjects/navigationPage';  /// import the object 'navigateTo' from navigationPage.js
import { onApplyPage } from '../support/pageObjects/applyPage';  /// import the object 'onApplyPage' from applyPage.js

describe('Commencement - Apply', () => {
  const caseNo = Cypress.env('case_no');    /// where is 'case_no' from ???? ///
  const plateNo = `J${new Date().getTime()}`;

  beforeEach(() => {    /// cy.intercept('method', 'url'): send requests to the url
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Applications/Save').as('postSaveCommencement');
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/collateral/Application/Submission').as('postSubmitCollateral');
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Applications/Submission').as('postSubmitCommencement');
    cy.intercept('POST', 'http://10.164.71.100/ingress/my/core/commencement/Applications/Approval').as('postApprovalCommencement');
  });

  it('CSR Apply Commencement', () => {
    cy.visit('http://ibm-dev-my-commencement.chailease.com.tw/');
    cy.$_Login(Cypress.env('cs').email);  /// refer to the environment variable set in the cypress.config.js

    navigateTo.applyPage();
    cy.$_WaitLoading();

    onApplyPage.searchCaseNo(caseNo);
    cy.$_WaitLoading();

    onApplyPage.selectContractFormat('ACT'); // ACT, Non-ACT, I-ACT, Money Lending

    onApplyPage.setupCollateral(plateNo);

    onApplyPage.setupCheckList(['Continuity Surety Agreement (for Corporation)', 'Continuity Surety Agreement (for Personal)'])

    onApplyPage.setupTermsAndConditions();

    onApplyPage.setupDisbursementInformation();

    cy.$_Action('Save')
    cy.wait('@postSaveCommencement', { timeout: 15000 });
    cy.$_CheckToaster('Success');
  });

  it.skip('CSR Set Collateral', () => {
    cy.visit('http://ibm-dev-my-collateral.chailease.com.tw/#/login?redirectPath=%2Fcollateral-information-set%3Flang%3Den-us%26companyId%3D92%26systemId%3D22%26systemFunctionId%3D176%26processDefKey%3DCollateralApplication%26functionCode%3DCollateralInformation%26privilegeCode%3DSet');
    cy.$_Login(Cypress.env('cs').email);

    // navigateTo.collateralSetPage();

    cy.$_SearchField('Case No.', caseNo);
    cy.$_ClickTable(caseNo);

    // Attachment Tab
    cy.$_ClickTab('Attachment');
    cy.get('input[type=file]').selectFile({
      contents: 'cypress/fixtures/test.pdf',
      fileName: 'test.pdf',
      mimeType: 'application/pdf',
      lastModified: Date.now(),
    }, { force: true });

    cy.wait(500); // avoid unknown Error

    cy.contains('button[pbutton]', 'OK').click();

    cy.get('label').contains('Exported').prev().click();

    cy.get('button').contains('Export to Web').click();
    cy.$_WaitLoading();
    cy.$_CheckToaster('Success');

    // Collateral Tab
    cy.$_ClickTab('Collateral');

    cy.get('[formcontrolname=settingComplete]').click();
    cy.get('[formcontrolname=settingCompleteDate]').find('input').type('01/09/2022');

    cy.contains('button[p-button]', 'Claim').click();
    cy.$_WaitLoading();
    cy.$_CheckToaster('Success');

    cy.$_Action('Submit');
    cy.wait('@postSubmitCollateral', { timeout: 15000 });
    cy.$_CheckToaster('Success');
  });    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


  it('CSR Set Collateral claim only', () => {
    cy.visit('http://ibm-dev-my-collateral.chailease.com.tw/#/login?redirectPath=%2Fcollateral-information-set%3Flang%3Den-us%26companyId%3D92%26systemId%3D22%26systemFunctionId%3D176%26processDefKey%3DCollateralApplication%26functionCode%3DCollateralInformation%26privilegeCode%3DSet');
    cy.$_Login(Cypress.env('cs').email);

    // navigateTo.collateralSetPage();

    cy.$_SearchField('Case No.', caseNo);
    cy.$_ClickTable(caseNo);

    // Collateral Tab
    cy.$_ClickTab('Collateral');

    cy.contains('button.p-button', 'Claim').click();
    cy.$_WaitLoading();
    cy.$_CheckToaster('Success');
  });

  it('CSR Continue Apply', () => {
    cy.visit('http://ibm-dev-my-commencement.chailease.com.tw/');
    cy.$_Login(Cypress.env('cs').substitute);
    cy.$_ClickTab('Substitute');

    navigateTo.todoCard('Commencement Application', 'Applying');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postSubmitCommencement', { timeout: 15000 });
    cy.$_CheckToaster('Success');
  });

  it('CSR Manager Approve', () => {
    cy.visit('http://ibm-dev-my-commencement.chailease.com.tw/');
    cy.$_Login(Cypress.env('csManager').email);

    navigateTo.todoCard('Commencement Application', 'Under Review');
    cy.$_ClickTable(caseNo);

    cy.$_Action('Submit');
    cy.wait('@postApprovalCommencement', { timeout: 15000 });
    cy.$_CheckToaster('Success');
  });

  it('CSR Check Search State', () => {
    cy.visit('http://ibm-dev-my-commencement.chailease.com.tw/');
    cy.$_Login(Cypress.env('cs').email);

    navigateTo.searchPage();

    cy.$_SearchField('Contract No.', caseNo);
    cy.$_CheckState(caseNo, 'Normal / -'); // Commencement Completed / -
  });
});
