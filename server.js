// get the things we need
var express 	= require('express');
var app 		= express();
var path 		= require('path');

// var apiRoutes = require('./app/routes/api')(app, express);
// app.use('/api', apiRoutes);

// set the public folder to serve public assets
app.use(express.static(__dirname + '/public'));

// MAIN CATCHALL ROUTE -------------
// SEND USERS TO FRONTEND ----------
app.get('*', function(req,res) {
	res.sendFile(path.join(__dirname + '/public/app/views/index.html'));
});

// start the server on port 8080 (http://localhost:8080)
app.listen(8080);
console.log('SENG 371!');