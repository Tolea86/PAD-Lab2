(function () {
  'use strict';

  angular
    .module('proxyFrontend')
    .config(routerConfig);

  /** @ngInject */
  function routerConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('home', {
        url: '/users',
        templateUrl: 'app/main/main.html',
        controller: 'MainController as vm'
      })
      .state('posts', {
        url: '/posts',
        templateUrl: 'app/posts/post.list.html',
        controller: 'PostListController as vm'
      });

    $urlRouterProvider.otherwise('/users');
  }

})();
