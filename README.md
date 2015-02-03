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


