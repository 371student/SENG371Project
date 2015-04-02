// inject ngRoute for all our routing needs
angular.module('routerRoutes', ['ngRoute'])

// configure our routerRoutes
.config(function($routeProvider, $locationProvider) {
	$routeProvider

	// route for the home page
	.when('/', {
		templateUrl	: 'views/pages/home.html',
		controller	: 'mainController',
		controllerAs: 'home' 
	})

	// route for the data page
	.when('/data', {
		templateUrl	: 'views/pages/data.html',
		controller	: 'dataController',
		controllerAs: 'data' 
	});

	// set our app up to have prety URLs
	$locationProvider.html5Mode(true);

});