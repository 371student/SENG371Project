angular.module('repoService', [])

	.factory('Repo', function($http) {

		// create a new object
		var repoFactory = {};

		// get a single repo's data
		repoFactory.get = function(repoUrl) {
			return $http.get('/api/repos/' + repoUrl);
		};

		// get a every repo's data
		repoFactory.all = function() {
			return $http.get('/api/repos/');
		};

		// add a new repo's data
		repoFactory.add = function(repoUrl) {
			return $http.post('/api/repos/', repoUrl);
		};

		// update a repo's data
		repoFactory.update = function(repoUrl) {
			return $http.put('/api/repos/', repoUrl);
		};

		// return our entire repoFactor object
		return repoFactory;

	});