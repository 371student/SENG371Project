# SENG371Project
#### Project Question
* How is the growth of a software project affected by coupling? Is it possible to analyze/visualize coupling in a software project?

#### Methodology
* Write a script that would iteratively move through the history of the master branch of a software project, and then use Snakefood to capture a frame of the dependency graph at that point in time. Compile all the frames into a video and run it concurrently beside a gource visualization.

*By seeing the growth of a project next to the evolving dependency graph, relationships between between periods of high or low coupling, as well as periods of fast or slow growth could be discovered and analysed.*

#### Codebase / Systems
* We would analyze 3 codebases with our tool.
<br /> 1) [Django](https://github.com/django/django)
<br /> 2) [Pyramid](https://github.com/Pylons/pyramid)
<br /> 3) [Flask](https://github.com/mitsuhiko/flask)

#### Project Milestones
*Below are the milestones for our project. Milestone 3 is ideal; however, may not be possible.*

1. Feasibility analysis - run Snakefood on individual commits first to see how a video of these pictures would look. If dependency graphs are significantly different, then development will pivot to include editing the Snakefood code to suit our needs.
2. Create a script that iteratively moves through the history of the master branch of a software project on Github, runs Snakefood on each commit, and captures/names/stores an image. 
3. 
  1. Further edit the script to encode all the images into a video where the frames are synchronized with a Gource visualization. Or,
  2. Edit the source code of Snakefood to display its visualizations in a way that is more condusive to our goals. Then attempt Milestone 3a.
  3. 
  
#### Proof of Concept Experiment
*Although our experiment was not completed within the lab time, this experiment sheds some light on how we will define periods of high and low growth within the software projects we are analyzing. In addition, we get a better understanding of how we are testing our hypothesis.*
###### Assertion - Growth of a software project is inversely proportionate to increasing coupling/dependencies.
1. Use [GitStats](https://github.com/hoxu/gitstats) on a software project (Django, for example) and consult the graphs for "File Count by Date" and "Lines of Code" to determine periods of high and low growth in the project's history.
2. Take multiple samples from each of the high and low growth periods and run snakefood to get snapshots (as well as numerical values for dependency connections) of the project's dependencies at those time.
3. Compare GitStats growth graphs with the dependency snapshots to determine if there is a correlation between changes in dependency/coupling growth rate and changes in a project's file count and/or lines of code produced.
  
#### Things to Watch Out For
 * Excessive "include"s could possibly skew results.  


