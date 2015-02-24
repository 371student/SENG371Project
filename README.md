# SENG371Project
#### Project Question
* How is the growth of a software project affected by coupling? 

#### Methodology
* Write a script that would iteratively move through the history of the master branch of a software project, and then use Snakefood to capture the complexity of the dependency graph at that point in time. 

#### Data Sources
* We will test our research question by analyzing three codebases with our tool.
<br /> 1) [Django](https://github.com/django/django)
<br /> 2) [Pyramid](https://github.com/Pylons/pyramid)
<br /> 3) [Flask](https://github.com/mitsuhiko/flask)

#### Project Milestones
*Below are the milestones for our project. Milestone 3 is ideal; however, may not be possible.*

1. Feasibility analysis (Feb. 3) - Experiment with Snakefood and GitStats to verify that the data we need (in terms of coupling/dependencies and growth) is available. Record the run-time for these events and extrapolate over an entire cycle of our potential tool.
2. Tool Creation (Feb. 22)
  1. Write a Python program to iterate through the commit history of a GitHub project and run Snakefood at evenly spaced points throughout a project’s history to obtain dependency/coupling information (Coupling Factor). Output this information to a machine-readable format.
  2. Edit the source code for GitStats to output monthly growth information (Growth Factor) in the same a machine-readable format as the dependency/coupling information.
3. Data Analysis (Feb. 23)
  1. Use the machine-readable information obtained to plot coupling/dependency data against growth data.
  2. Analyze the data acquired and find other meaningful relationships between coupling and growth, and use this feedback to drive future development.


