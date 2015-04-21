// inject ngRoute for all our routing needs
angular.module('app.routes', ['ngRoute'])

// configure our routerRoutes
.config(function($routeProvider, $locationProvider) {
	
	$routeProvider

	// route for the home page
	.when('/', {
		templateUrl	: 'app/views/pages/home.html',
		controller	: 'mainController',
		controllerAs: 'home' 
	})

	// route for the success page
	.when('/repoadded', {
		templateUrl	: 'app/views/pages/repoadded.html',
		controller	: 'mainController',
		controllerAs: 'repoadded' 
	})

	// route for the data page
	.when('/data', {
		templateUrl	: 'app/views/pages/data.html',
		controller	: 'dataController',
		controllerAs: 'data' 
	})

	.otherwise({
        redirectTo: '/'
    });

	// set our app up to have pretty URLs
	$locationProvider.html5Mode(true);

});