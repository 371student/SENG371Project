angular.module('mainCtrl', ['repoService'])

	.controller('mainController', function($location, Repo) {
		// bind "this" to vm (view-model)
		var vm = this;

		/* MAIN
		---------------------------------------*/
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
					$location.path('/repoadded');
				});
		};

		/* REPOADDED
		---------------------------------------*/
		vm.successMessage = "You have added a repository to the queue. Check back in a little while to view the results! (You may need to refresh the page)";

		vm.backHome = function() {
			$location.path('/home');
			Repo.all()
				// Make promise
				.success(function(data) {
					vm.repositories = data;
				});
		}
		
	});
