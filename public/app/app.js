angular.module('GDAapp', ['app.routes'])

// create the controllers
// this will be the controller for the ENTIRE site
.controller('mainController', function() {
	// bind "this" to vm (view-model)
	var vm = this;

	// define a list of GitHub repositories
	// we will eventually just pull this list from the DB
	vm.repositories = [
		{ name: 'Django', url: 'https://github.com/django/django', status: 'Complete' },
		{ name: 'Pyramid', url: 'https://github.com/Pylons/pyramid', status: 'Complete' },
		{ name: 'Flask', url: 'https://github.com/mitsuhiko/flask', status: 'Complete' }
	];
})

// home page specific controller
.controller('homeController', function() {
	// bind "this" to vm (view-model)
	var vm = this;
})

// data page specific controller
.controller('dataController', function() {
	// bind "this" to vm (view-model)
	var vm = this;

	vm.message = 'Data page test message';

});