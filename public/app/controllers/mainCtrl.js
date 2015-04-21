angular.module('mainCtrl', ['repoService'])

// create the controllers
// this will be the controller for the ENTIRE site
.controller('mainController', function($location, Repo) {
	// bind "this" to vm (view-model)
	var vm = this;

	// Get all the repositories
	Repo.all()
		// Make promise
		.success(function(data) {
			vm.repositories = data;
		});

	vm.submitRepoUrl = function() {
		vm.processing = true;
		
		Repo.add(vm.repoUrl)
			.success(function(data) {
				vm.processing = false;

				vm.repoUrl = null;
				// $location.path('/data');
			});
	};
});
