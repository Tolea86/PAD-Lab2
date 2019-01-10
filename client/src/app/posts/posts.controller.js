(function () {
  'use strict';

  angular
    .module('proxyFrontend')
    .controller('PostListController', PostListController);

  /** @ngInject */
  function PostListController($scope, Restangular) {
    var vm = this;
    activate();
    vm.post = {};

    function activate() {
      getListOfPosts();
      getUserList();
    }

    vm.createPost = function () {
      vm.post.comments = [];
      var post = Restangular.restangularizeElement(undefined, vm.post, 'posts');
      post.post().then(function (response) {
        vm.postList.splice(0, 0, response);
      });
      vm.post = {};
    };

    vm.deletePost = function (post) {
      post.doDELETE();
      _.remove(vm.postList, post);
    };


    function getListOfPosts(){
      Restangular.service('posts').getList().then(function (response) {
        vm.postList = response;
      })
    }

    function getUserList() {
      Restangular.service('users').getList().then(function (response) {
        vm.userList = response;
      });
    }

  }
})();
