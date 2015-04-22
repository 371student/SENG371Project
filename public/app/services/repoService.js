angular.module('repoService', [])

	.factory('Repo', function($http) {

		// create a new object
		var repoFactory = {};
		repoFactory.graphData = {};

		// store single repo dataset for dataCtrl graphing
		repoFactory.prepData = function(data) {
			repoFactory.graphData = data;
		};

		// get every repo's data
		repoFactory.all = function() {
			return $http.get('/api/repos');
		};

		// get one repo's data
		repoFactory.getOne = function(repoUrlForData) {
			return $http.post('/api/repo', {'url': repoUrlForData});
		};

		// add a new repo's data
		repoFactory.add = function(repoUrl) {
			return $http.post('/api/add', {'url': repoUrl});
		};

		// return our entire repoFactor object
		return repoFactory;

	});