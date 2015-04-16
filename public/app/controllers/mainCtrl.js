angular.module('mainCtrl', ['repoService'])

// create the controllers
// this will be the controller for the ENTIRE site
.controller('mainController', function($location, Repo) {
	// bind "this" to vm (view-model)
	var vm = this;

	// define a list of GitHub repositories
	// we will eventually just pull this list from the DB
	vm.repositories = [
		{ name: 'Django', url: 'https://github.com/django/django', status: 'Complete' },
		{ name: 'Pyramid', url: 'https://github.com/Pylons/pyramid', status: 'Complete' },
		{ name: 'Flask', url: 'https://github.com/mitsuhiko/flask', status: 'Complete' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' },
		{ name: 'Test', url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', status: 'In Progress' }
	];

	vm.submitRepoUrl = function() {
		$location.path('/data');
	};


});
