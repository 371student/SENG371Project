# SENG371Project
#### Current Usage Instructions
1. Navigate to http://www.growthcoupling.com/
2. Enter a repo url
3. See results

OR <br>
 1. Navigate to http://www.growthcoupling.com/ <br>
 2. Select an existing repo <br>
 3. See results <br>

#### Project Question
* How is the growth of a software project affected by coupling? 
* Insights on the development process itself can be made by knowing how adding dependencies (or increasing coupling) affects the growth of the project.
* Results from our tool could be used to make insights about software projects that use Git as a versioning tool. Our tool could potentially draw attention to things like technical debt / legacy code.

#### Methodology
* Write a script that would iteratively move through the history of the master branch of a software project, and then use [Snakefood](http://furius.ca/snakefood/) to capture the complexity of the dependency graph at that point in time. This complexity metric - or “Coupling Factor” - will be calculated as the ratio of dependency-graph edges to nodes (at that point in time). (Note: as Snakefood only provides coupling information for Python projects, our tool is also restricted to Python projects at this time)
* Edit the source code of [GitStats](https://github.com/hoxu/gitstats) to serve monthly-growth information about the same project. This growth metric - or “Growth Factor” - will be calculated as follows:
  1. Divide the average of Commits/Month by the average of the Coupling Factor.
  2. Multiply this number by 4.
  3. Growth factor is equal to to Commits/Month divided by the number obtained in 2.
* Compare the information obtained in the ways mentioned above by plotting the two factors over time, and against one-another. The graph comparing the Coupling Factor and Growth Factor for a particular project can then be analyzed to determine if the project’s complexity is increasing over time relative to its growth. The graph can also be compared to the comparison graphs of other projects, and conclusions about project health can be drawn.

#### Data Sources
* We will test our research question by analyzing three codebases with our tool.
<br /> 1) [Django](https://github.com/django/django)
<br /> 2) [Pyramid](https://github.com/Pylons/pyramid)
<br /> 3) [Flask](https://github.com/mitsuhiko/flask)

#### Results
*No Magic was performed to gather our data. 
*Here is part of the output CSV file for Pyramid:*

Dependency Graph

 Date |  		Coupling Factor 
 ---- | ---- 
 2008-07 |		2.44444444444   
 2008-08 |		2.75            
 2008-09 |		3.0             
 2008-10 |		2.98591549296   
 2008-11 |		3.10526315789   
 2008-12 |		3.11842105263   
 2009-01 |		3.29347826087   
 2009-02 |		3.28260869565   
 2009-03 |		3.28260869565   
 2009-04 |		3.29032258065   
		…

Date |  		Commits | Lines Added | Lines Removed
---- | ---- | ---- | ---- 
2015-02 |		92 |	    4172  |	   489
2015-01 |		43 |	    0 	  |	   0
2014-12 |		52 |	    11008 |        424
2014-11 |		97 |	    354   |	   133
2014-10 |		16 |	    60    |        28
2014-09 |		12 |	    14    |	   10
2014-08 |		20 |	    0     |	   0
2014-07 |		51 |	    713   |	   231
2014-06 |		10 |	    38    |	   3
2014-05 |		39 |	    389   |	   742
2014-04 |		93 |	    837   |	   1075
2014-03 |		30 |	    0     |	   0
        		 …

*Resulting graph from comparing Coupling Factor to Growth Factor*
![alt tag](http://i.imgur.com/Vd4BVcv.png)
![alt tag](http://i.imgur.com/6JPyAdx.png)
![alt tag](http://i.imgur.com/GdRLz9O.png)

As is evidenced, there is a strong correlation between the growth and coupling/dependencies in Django. Further work is needed to more completely understand the relationship between coupling and growth. It is still unclear if there is a one or two-way causal relationship between the two factors. The analysis of multiple repositories would reduce threats to the validity of our claims.

#### Project Milestones For Project 1

1. Feasibility Analysis (Feb. 3) - Experiment with Snakefood and GitStats to verify that the data we need (in terms of coupling/dependencies and growth) is available. Record the run-time for these events and extrapolate over an entire cycle of our potential tool.
2. Tool Creation (Feb. 22)
  1. Write a Python program to iterate through the commit history of a GitHub project and run Snakefood at evenly spaced points throughout a project’s history to obtain dependency/coupling information (Coupling Factor). Output this information to a machine-readable format.
  2. Edit the source code for GitStats to output monthly growth information (Growth Factor) in the same a machine-readable format as the dependency/coupling information.
3. Data Analysis (Feb. 23)
  1. Use the machine-readable information obtained to plot coupling/dependency data against growth data.
  2. Analyze the data acquired and find other meaningful relationships between coupling and growth, and use this feedback to drive future development.

#### Future Work From Project 1

1. Automate/simplify program flow - Our next step is to remove intermediate steps for users by streamlining the entire application process. Ideally a user could simply run our tool with tFurther analysis of data | X | X | Xhe location of a cloned Git repository as a parameter (possibly with a time-increment parameter as well), and our tool would output the information.
2. Graph output - As an extension to automation, we would like our tool to produce graphical representations of the outputted data, to make it immediately meaningful for users.
3. Parallelize computation / improve user performance at scale - Currently, our tool will run for hours on sufficiently large repositories. By refactoring our code to take advantage of threading or distributed computing, we could achieve much faster computation. 

#### Team Member’s Roles In Project 1

* Chris - Data Scientist
* Richard - Developer
* Sarah - Developer

<hr>

# Estimation and Timeline For Project 2

#### Task Breakdown and Estimations 
Task | Importance | Effort | Risk
---- | ---- | ---- | ----
Research: Using non-python repositories | 2 | 2 | 0
Research: Server, client, database technologies | 5 | 4 | 0
Research: Gitstats alternatives | 3 | 3 | 0
Research: Further analysis of data | 8 | 10 | 1
Development: Incorporate [d3](http://d3js.org/) into the application | 8 | 6 | 4
Development: Create an interface on the client side | 10 | 7 | 4
Development: Create basic server code | 10 | 5 | 4
Development: Create server and client code that exchange data | 8 | 7 | 4
Development: Create a worker script  | 8 | 7 | 4
Development: Estabolish sending data between client, server and databse | 10 | 8 | 5
Development: Inform user of current script status during runtime | 3 | 4 | 1
Development: Allow users to select a repo from a list of ones previously run | 8 | 6 | 3


#### Sprint 1	(March 10th - March 24th)
Plan | Accomplished 
 ---- | ----
Research: Using non-python repositories 	| Decided it was best to continue using Snakefood and python-based repositories
Research: Server, client, database technologies | We decided on the following: <br> server: python <br> client: HTML, CSS, JS, and Angular.js framework <br> database: MongoDB
Research: Gitstats alternatives  		| We decided to no longer use gitstats in our application
Research: Further analysis of data		| Find mathematical cooralation between growth factor and coupling factor

#### Sprint 2	(March 24th - April 7th)
Plan | Accomplished 
 ---- | ----
Development: Incorporate d3 into the application		| d3 was successfully incorporated into the client code
Development: Create an interface on the client side		| User interface was successfully developed using HTML, CSS, JS, and Angular.js
Development: Create basic server code				| This was successfully completed. At this point we had a functional website with minimal features.
Development: Create server and client code that exchange data	| This was successfully completed using ajax and json objects

#### Sprint 3	(April 7th - April 30th)
Plan | Accomplished 
 ---- | ----
Development: Create a worker script					     | In progress
Development: Estabolish sending data between client, server and databse      | In progress
Development: Inform user of current script status during runtime	     | In progress
Development: Allow users to select a repo from a list of ones previously run | In progress


####  Scrum Meeting Times
* During lab times
* Bi-weekly hangouts meetings

#### Team Member Roles
* Chris - Data scientist and lead front-end developer
* Richard - Back-end developer
* Sarah - Apprentice front-end developer and readme updater

Task | Chris | Richard  | Sarah
---- | ---- | ---- | ---- 
Sprint 1 | | |
Research: Using non-python repositories | X | X | X
Research: Server, client, database technologies | X | X | 
Research: Gitstats alternatives | X | X | X
Research: Further analysis of data | X |  | 
Sprint 2 | | |
Development: Incorporate [d3](http://d3js.org/) into the application |  |  | X
Development: Create an interface on the client side | X |  | X
Development: Create basic server code |  | X  | 
Development: Create server and client code that exchange data | X | X | X
Sprint 3 | | |
Development: Create a worker script  |  | X | 
Development: Estabolish sending data between client, server and databse |  | X | 
Development: Inform user of current script status during runtime | X | X | X
Development: Allow users to select a repo from a list of ones previously run | X |  | X


### Improvements From Project 1
1. No downloadable content - Project 1 required the user to clone our repository and install all the dependencies. For project 2, we use a server to run our script where the user simply supplies the reporsitory  url. 
2. Graph output - In project 1, the user gathered the .csv files and choose a program of their choice to view th data and manually graph it. In order to increate automation, our tool now uses d3 to produce graphical representations of the outputted data, to make it immediately meaningful for users.
3. Increased user preformance - In poject 1, our tool would run for hours on sufficiently large repositories. By storing repositories in our database, we can simply pull the data from the database rather than running the script again. 
4. Created a user interface - Project 1 required the user to run linux commands in the terminal and follow a tedious process in order to get the desired output. By creating a web application we created a clean UI for our users. 
5. We improved upon our project 1 trendlines. In project 2 they account for a higher degree polynomual allowing for more accurate results.

