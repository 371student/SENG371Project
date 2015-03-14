# SENG371Project
#### Current Usage Instructions
1. git clone \<this repo\>
2. sudo apt-get install snakefood
3. git clone \<repo to analyze\>
4. Navigate to the root directory of the git project you wish to analyze
5. git log --date-order > temp.txt
6. cat temp.txt | python /path/to/gda.py > output.csv
7. python /path/to/gitstats.py . /output/directory

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
2015-02 |		92 |	    4172 |	            489
2015-01 |		43 |	    0 |	             0
2014-12 |	  52 |	    11008 |            424
2014-11 |		97 |	     354 |	             133
2014-10 |		16 |	     60 |                  28
2014-09 |		12 |	     14 |	              10
2014-08 |		20 |	      0 |	               0
2014-07 |		51 |	      713 |	               231
2014-06 |		10 |	      38 |	               3
2014-05 |		39 |	      389 |	               742
2014-04 |		93 |	      837 |	              1075
2014-03 |		30 |	      0 |	               0
        		 …

*Resulting graph from comparing Coupling Factor to Growth Factor*
![alt tag](http://i.imgur.com/Vd4BVcv.png)
![alt tag](http://i.imgur.com/6JPyAdx.png)
![alt tag](http://i.imgur.com/GdRLz9O.png)

As is evidenced, there is a strong correlation between the growth and coupling/dependencies in Django. Further work is needed to more completely understand the relationship between coupling and growth. It is still unclear if there is a one or two-way causal relationship between the two factors. The analysis of multiple repositories would reduce threats to the validity of our claims.

#### Project Milestones

1. Feasibility Analysis (Feb. 3) - Experiment with Snakefood and GitStats to verify that the data we need (in terms of coupling/dependencies and growth) is available. Record the run-time for these events and extrapolate over an entire cycle of our potential tool.
2. Tool Creation (Feb. 22)
  1. Write a Python program to iterate through the commit history of a GitHub project and run Snakefood at evenly spaced points throughout a project’s history to obtain dependency/coupling information (Coupling Factor). Output this information to a machine-readable format.
  2. Edit the source code for GitStats to output monthly growth information (Growth Factor) in the same a machine-readable format as the dependency/coupling information.
3. Data Analysis (Feb. 23)
  1. Use the machine-readable information obtained to plot coupling/dependency data against growth data.
  2. Analyze the data acquired and find other meaningful relationships between coupling and growth, and use this feedback to drive future development.

#### Future Work

1. Automate/simplify program flow - Our next step is to remove intermediate steps for users by streamlining the entire application process. Ideally a user could simply run our tool with tFurther analysis of data | X | X | Xhe location of a cloned Git repository as a parameter (possibly with a time-increment parameter as well), and our tool would output the information.
2. Graph output - As an extension to automation, we would like our tool to produce graphical representations of the outputted data, to make it immediately meaningful for users.
3. Parallelize computation / improve performance at scale - Currently, our tool will run for hours on sufficiently large repositories. By refactoring our code to take advantage of threading or distributed computing, we could achieve much faster computation. 

#### Team Member’s Roles

* Chris - Data Scientist
* Richard - Developer
* Sarah - Developer
* 

# Estimation and Timeline

#### Task Breakdown and Estimations 
Task | Importance | Effort | Risk
---- | ---- | ---- | ----
Streamline the process | 8 | 7 | 2
There should be 1 file created at runtime (the output.csv)| 6 | 7 | 3
Run gitstats in quiet mode | 9 | 8 | 1
Prompt user for git info, repo link etc .. instead of following the readme | 5 | 5 | 1
Inform user of current script status during runtime | 3 | 4 | 1
Incorporate matplotlib into script | 10 | 5 | 4
Increase performance | 7 | 10 | 9
Look into non-python repositories | 6 | 9 | 0
Further analysis of data | 10 | 8 | 3




#### Sprint 1 Plan  (March 10th - March 24th)
* Look into non-python repositories
* Incorporate matplotlib into script 
* There should be 1 file created at runtime
* Look into gitstats alternatives 

#### Sprint 2 Plan (March 24th - April 7th)
* Further analysis of data (new relationships, finding correlations/causations)
* Streamline the process
* Prompt user for git info, repo link etc .. instead of following the readme 

#### Sprint 3 Plan  (April 7th - April 21st)
* Increase performance
* Inform user of current script status during runtime 
* Run gitstats in quiet mode



####  Scrum Meeting Times
* During lab times
* Bi-weekly hangouts meetings

#### Team Member Roles

Task | Chris | Richard  | Sarah
---- | ---- | ---- | ---- 
Sprint 1 |  |  | 
Non-python repositories | X | X | X
Incorporate matplotlib | X | | 
1 file created | | X | X
gitstats alternatives | X | X | X
Sprint 2 |  |  | 
Streamline the process | X | X | X
Prompt user for info | | | X
Further analysis of data | X | X | X
Sprint 3 |  |  | 
Increase performance | X |  X |
Inform user script status | | | X
Run gitstats in quiet mode | | X |



