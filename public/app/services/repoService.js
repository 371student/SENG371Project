angular.module('repoService', [])

	.factory('Repo', function($http) {

		// create a new object
		var repoFactory = {};

		// get every repo's data
		repoFactory.all = function() {
			return $http.get('/api/repos');
		};

		// add a new repo's data
		repoFactory.add = function(repoUrl) {
			return $http.post('/api/add', repoUrl);
		};

		// return our entire repoFactor object
		return repoFactory;

	});