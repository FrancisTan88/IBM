const selectGroupMenuItem = (groupName) => {
  cy.contains('a[role=treeitem]', groupName).then(menu => {
    cy.wrap(menu).find('.p-panelmenu-icon').invoke('attr', 'class').then(attr => {
      if (attr.includes('right')) {
        cy.contains('a[role=treeitem]', groupName).should('be.visible').click();
      }
    })
  })
}

export class NavigationPage {
  applyPage() {
    selectGroupMenuItem('Commencement');
    selectGroupMenuItem('Commencement Management');
    cy.contains('a[role=treeitem]', 'Apply').click();
    cy.url().should('include', '/commencement-apply');
  }

  restorePage() {
    selectGroupMenuItem('Commencement');
    selectGroupMenuItem('Commencement Management');
    cy.contains('a[role=treeitem]', 'Restore').should('be.visible').click();
    cy.url().should('include', '/reverse-apply');
  }

  searchPage() {
    selectGroupMenuItem('Commencement');
    selectGroupMenuItem('Commencement Management');
    cy.contains('a[role=treeitem]', 'Search').should('be.visible').click();
    cy.url().should('include', '/commencement-enquiry');
  }

  amendPage() {
    selectGroupMenuItem('Commencement');
    selectGroupMenuItem('Contract Management');
    cy.contains('a[role=treeitem]', 'Amend').should('be.visible').click();
    cy.url().should('include', '/amend-apply');
  }

  repaymentScheduleRestructurePage() {
    selectGroupMenuItem('Commencement');
    selectGroupMenuItem('Contract Management');
    cy.contains('a[role=treeitem]', 'Repayment Schedule Restructure').should('be.visible').click();
    cy.url().should('include', '/repayment-schedule-restructure');
  }

  collateralSetPage() {
    selectGroupMenuItem('Collateral Management');
    selectGroupMenuItem('Collateral Information');
    cy.contains('a[href*="collateral-information-set"]', 'Set').should('be.visible').click();
    cy.url().should('include', '/collateral-information-set');
  }

  todoCard(cardStatus, workflowStage) {
    cy.get(`.card-header:contains(${cardStatus})`).closest('.card').contains(workflowStage).click();
  };
}

export const navigateTo = new NavigationPage()