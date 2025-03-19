# Soccer Data Analysis

This is the repository for my project on data analysis of various statistics to predict final standings for soccer leagues. 

## Report   

When thinking about what to do for this project, I wanted to do something related to sports data analysis. This decision was partially because of my love for sports and partially because of how accessible the data is. Information about goals scored, expected goals, and more complex stats are available for free in their raw forms. This was very important for the type of data analysis I wanted to do for this project.

I chose data from my favorite soccer league: the Women’s Super League (WSL) in England. This is the top flight of women’s football in England and has some of the best women’s teams in the world. 

The champion of the WSL is determined by the first-place finisher. The second and third-place finishers qualify for the Champions League, and the last-place finisher is relegated to the league below the WSL. Because standings are important in the WSL, I wanted to find out if any of the statistics that are recorded about the WSL could be used to predict where a team would finish at the top of the table. If there are no completely accurate stats, is there another way to predict where teams will end up? 

### XML File 
[Python used linked here.](XMLCreation.py)   

To answer this question, I downloaded the data from FBref.com into a CSV file. Then, I transformed this data into a format that can be easily manipulated. I picked XML formatting because it is a format that I am comfortable working with and a format that works great with Python. Every team is an element in the “standings” element, with each team having the same elements contained in it. These elements included the team names and their statistics from the season. I then validated this XML document to make sure that it was formatted correctly. 

### Data Analysis
[Python used linked here.](DataAnalysis.py)

Once I had transformed the data into an XML file I was able to use XPATH to find specific data in the file. I used XPATH to get each team’s corresponding statistics. Then, I created a list of dictionaries where each entry is a dictionary with the team’s name and statistic value. For each statistic, I sorted the list either in ascending or descending order depending on which made sense based on the context for the statistic. For example, I sorted the “goals against” in ascending order, since a team that has fewer goals against had a better performance defensively over the season. On the other hand, I sorted “goals for” in ascending order since it is better to score more goals.  

I also created statistics for the teams. These statistics all have to do with the difference between expected goals and actual goals. Expected goals and similar stats are calculated by looking at the chances a team generates on goal. One question I asked myself was “Are teams that score more goals than expected going to land higher on the table?” To do this, I compared each team’s expected goals and actual goals and created a new list of the differences between the teams. Then, I used the same function to sort them in both orders: teams with a bigger difference in expected goals to goals and teams with a smaller difference. I then did this for expected goals against and the expected goal differential. 

After I created every ranking of the teams by stats, I awarded them points based on their standing. The team in first place was awarded 12 points, second 11, and so on. I kept track of these values in a list of dictionaries containing the teams. This gave me a ranking of the teams based on each stat combined. 

To determine how accurate a statistic’s ranking was, I created a function that could see how far off each team was from its actual place in the final rankings. This function found the average amount of places that a team was off from its final spot, which is a number ranging from 0 to -6. With this information, I was able to understand which statistics are the most useful when predicting where each team will end up. The most accurate statistics were goals for, goal differential, and my points system, each with only a -0.5 score for accuracy. The least accurate stats were expected goal vs goals ranked with the lowest difference first, expected goals against vs goals against with the highest difference ranked first, and expected goal differential vs goal differential with the lowest ranked first. These all had a score of -5 or higher. 

### Data Visualization
[Graph 1 Python Linked Here.](GoalsForScatterPlot.py)
[Graph 2 Python Linked Here.](GoalsDifferentialScatterPlot.py)
[Graph 3 Python Linked Here.](ExpectedGoalDifferentialScatterPlot.py)


For my graphs, I wanted to chart these results using a scatter plot. The scatter plot was able to show if there was a correlation between statistics and the standings. For some of the statistics, like goals, the graph is close to a straight line. For some of the other statistics, the graphs are much more random. These graphs provided useful visuals for me to understand what the accuracy numbers meant. 

Overall, I learned that while there are some statistics in this specific scenario that are similar to how the standings ended up, there should be a better way to predict where a team will end up in the table. If I were to continue this project, I would attempt to find an algorithm that could predict where a team would end up in any table very accurately using the statistics that I examined in this project. 




### Works Cited

FBref. “2023-2024 Women’s Super League Stats | FBref.com.” FBref.com, 2023, fbref.com/en/comps/189/2023-2024/2023-2024-Womens-Super-League-Stats. Accessed 14 Dec. 2024.

