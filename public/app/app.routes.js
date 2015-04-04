// inject ngRoute for all our routing needs
angular.module('app.routes', ['ngRoute'])

// configure our routerRoutes
.config(function($routeProvider, $locationProvider) {
	
	$routeProvider

	// route for the home page
	.when('/', {
		templateUrl	: 'app/views/pages/home.html',
		controller	: 'mainController',
		controllerAs: 'main' 
	});

	// route for the data page
	// .when('/data', {
	// 	templateUrl	: 'app/views/pages/data.html',
	// 	controller	: 'dataController',
	// 	controllerAs: 'data' 
	// });

	// set our app up to have pretty URLs
	$locationProvider.html5Mode(true);

});