(function () {
  'use strict';

  angular
    .module('proxyFrontend')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController($mdDialog, $mdToast, Restangular) {
    var vm = this;
    activate();

    vm.user = {};

    function activate() {
      getUserList()
    }

    vm.deleteUser = function (user) {
      user.doDELETE().then(function () {
        $mdToast.show(
          $mdToast.simple()
            .textContent('User deleted successfully')
            .position('bottom left')
            .hideDelay(3000)
        );
      });
      _.remove(vm.userList, user)
    };

    vm.showEditUserPrompt = function (event, user) {
      $mdDialog.show({
        locals: {user: user},
        controller: EditUserDialogController,
        controllerAs: 'ctrl',
        templateUrl: 'app/components/edit-user-dialog/edit-user-dialog.tmpl.html',
        parent: angular.element(document.body),
        targetEvent: event,
        clickOutsideToClose: true
      })
    };

    function EditUserDialogController($scope, $mdDialog, user) {
      $scope.user = user;
      $scope.createUser = function (user) {
        user.put().then(function () {
          $mdToast.show(
            $mdToast.simple()
              .textContent('User saved successfully')
              .position('bottom left')
              .hideDelay(3000)
          );
        });
        $mdDialog.hide();
      }
    }

    vm.createUser = function () {
      var user = Restangular.restangularizeElement(undefined, vm.user, 'users');
      user.post().then(function (response) {
        $mdToast.show(
          $mdToast.simple()
            .textContent('User created successfully')
            .position('bottom left')
            .hideDelay(3000)
        );
        vm.user = {};
        vm.userList.splice(0, 0, response)
      });
    };

    function getUserList() {
      Restangular.service('users').getList().then(function (response) {
        vm.userList = response;
      });
    }
  }
})();
