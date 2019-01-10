(function() {
  'use strict';

  angular
    .module('proxyFrontend')
    .config(config);

  /** @ngInject */
  function config($logProvider, $locationProvider, RestangularProvider) {
    // Enable log
    $logProvider.debugEnabled(true);

    // Set options third-party lib
    // Set restangular options
    // RestangularProvider.setBaseUrl('http://localhost:8000/api/v1/');
    RestangularProvider.setBaseUrl('http://localhost:8000/api/v1/');
    RestangularProvider.setRequestSuffix('/');
    RestangularProvider.setDefaultHttpFields({spinner: true});

    $locationProvider.html5Mode(true);
  }

})();
