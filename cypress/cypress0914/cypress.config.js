const { defineConfig } = require("cypress");

module.exports = defineConfig({
  viewportWidth: 1440,
  viewportHeight: 960,
  retries: 1,
  numTestsKeptInMemory: 5,
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    defaultCommandTimeout: 10000,
    specPattern: 'cypress/e2e/**/*.{js,jsx,tx,tsx}',
    env: {
      cs: {
        email: 'LilyYee@chailease.com.my',
        name: 'MY00242 Yee Choon Thye',
        substitute: 'CSLeong@chailease.com.my',
      },
      csManager: {
        email: 'KKChong@chailease.com.my',
        name: 'MY00190 K K Chong'
      },
      csBoss: {
        email: 'AlexYang@chailease.com.my',
        name: '00694 Yang Huei Yeu'
      },
      amendCredit: {
        email: 'ImanFirdaus@chailease.com.tw',
        name: 'MY00032 Muhammad Iman Firdaus'
      },
      amendCreditManager: {
        email: 'KKChong@chailease.com.my',
        name: 'MY00190 K K Chong'
      },
      credit: {
        email: 'SuhanizaSamsudin@chailease.com.my',
        name: 'MY00036 Suhaniza'
      },
      // credit:{
      //  email:  'nursyafiqah@chailease.com.my', 
      //  name:'MY00039 Nur Syafiqah'            
      // },
      creditManager: {
        email: 'KamKuan@chailease.com.my',
        name: 'MY00068 Ng Kam Kuan'
      },
      creditSeniorManager: {
        email: 'my99999@chailease.com.my',
        name: '04063 Chad Ueng'
      },
      legal: {
        email: 'Alexlee@chailease.com.my',
        name: 'MY00015 Alex Lee'
      },
      legalManager: {
        email: 'my99999@chailease.com.my',
        name: '04063 Chad Ueng'
      },
      financeAcc: {
        email: 'MarkChuang@chailease.com.my',
        name: '03186 Aqua Chuang'
      }
    }
  },
});
