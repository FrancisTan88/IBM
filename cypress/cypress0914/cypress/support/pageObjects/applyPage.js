class ApplyPage {
  searchCaseNo(caseNo) {
    cy.$_TypeText( 'Case No.', caseNo);
    cy.$_Action('Search');
  }

  selectContractFormat(contractName) {
    cy.$_SelectDropDown('Contract Format', contractName); // ACT, Non-ACT, I-ACT
  }

  setupCollateral(plateNo) {
    cy.$_ClickTab('Collateral');
    cy.get('[formcontrolname=plateNo]').clear().type(plateNo);
  }

  setupCheckList(checklist) {
    cy.$_ClickTab('Check List');
    checklist.forEach(item => {
      cy.$_GetTableRow(item, 'sigv-check-list').find('p-checkbox').click();
    });
  }

  setupTermsAndConditions() {
    cy.$_ClickTab('Terms & Conditions');
    cy.get('[role=tab]').contains('Fees & Charges').click();
    cy.$_GetTableRow('Commission', 'p-accordiontab').find('p-checkbox').click();
  }

  setupDisbursementInformation() {
    cy.$_ClickTab('Disbursement Information');
    cy.contains('label[for=deduction]', 'Remit').click();

    cy.get('sigv-disb-remit').then($Remit => {
      // Salaes Incentive
      cy.wrap($Remit).find('[formcontrolname="paymentType"]').eq(0).click();
      cy.$_SelectDropDownItem('Sales Incentive');

      // Dealer Incentive
      cy.wrap($Remit).find('button').contains('Add').click();
      cy.wrap($Remit).find('[formcontrolname="paymentType"]').eq(1).click();
      cy.wait(500);
      cy.$_SelectDropDownItem('Dealer Incentive');

      // Finance
      cy.wrap($Remit).find('button').contains('Add').click();
      cy.wrap($Remit).find('[formcontrolname="paymentType"]').eq(2).click();
      cy.wait(500);
      cy.$_SelectDropDownItem('Finance');

      cy.wrap($Remit).find('[formcontrolname="disbReceiver"]').eq(2).click();
      cy.wait(500);
      cy.$_SelectDropDownItem('Dealer');
    })
  }
}

export const onApplyPage = new ApplyPage();