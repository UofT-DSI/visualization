# Data Visualization

## Assignment 1: Participation (Ongoing)

### Requirements:

## July 23rd session
- During every class, follow along with sample code from the slides. All code that you should be running in Python is formatted as follows:
  
  > If code in a slide looks like this, you should be running it to generate results.

#Importing required libraries to generate sample data and plotting.
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import scipy
  import PIL
  import requests

#Set Random Seed. 50 continuous x variables with y results randomized ranging from 0-100
np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0,100,50)

#Generate scatterplot on 5x3 figure size
fig, ax = plt.subplots(figsize = (5,3))
ax.scatter(x,y)

#Generate bar graph on 5x3 figure size
fig, ax = plt.subplots(figsize = (5,3))
ax.bar(x,y)

#Generate line graph on 5x3 figure size
fig, ax = plt.subplots(figsize = (5,3))
ax.plot(x,y)

#Generate histogram on 5x3 figure size
fig, ax = plt.subplots(figsize = (5,3))
ax.hist(y)


#Generate line plot, then set title name and axis labels
fig, ax = plt.subplots(figsize = (5,3))
ax.plot(x,y)

ax.set_title('Total growth over time')
ax.set_ylabel('Total growth (%)')
ax.set_xlabel('Years since start')


#Create fonts for use on graphing.
font1 = {'family':'sans-serif','color':'blue','size':20}
font2 = {'family':'monospace','color':'green','size':14}

#Generate line chart, with title and axis labels, using font1 for title, font 2 for axis labels
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y)
ax.set_title('Total Growth Over Time', fontdict = font1)
ax.set_ylabel('Total Growth', fontdict = font2)
ax.set_xlabel('Years Since Start', fontdict = font2)

#Generate a scatter plot using Star Marker & Indigo colour
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,
      y,
      marker = '*',
      color = 'indigo'
      )

#Generate a scatter plot using Star Marker & Indigo colour, linestyle '--', line width of '2'
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,
      y,
      marker = '*',
      color = 'indigo'
      linestyle = '--',
      linewidth = '2')


#Changing color, markeredgecolor, markerfacecolor from above graph
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,
      y,
      marker = '*',
      color = '#7425b9'
      linestyle = '--',
      linewidth = 2,
      markeredgecolor = '#fa9359'
      markerfacecolor = '#000000')

#Adding y axis grid lines to above graph
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,
      y,
      marker = '*',
      color = '#7425b9'
      linestyle = '--',
      linewidth = 2,
      markeredgecolor = '#fa9359'
      markerfacecolor = '#000000')

ax.grid(axis ='y')

#Changing axis lines to both X & Y lines, Gridlines are pink, dotted, line width 4
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,
      y,
      marker = '*',
      color = '#7425b9'
      linestyle = '--',
      linewidth = 2,
      markeredgecolor = '#fa9359'
      markerfacecolor = '#000000')

ax.grid(color = 'pink',linewidth = 4, linestyle = 'dotted')



##Activity

# libraries to generate data & plot simple area plot
import numpy as np
import matplotlib.pyplot as plt
 
# Create data
x=range(1,6)
y=[1,4,6,8,4]
 
# Area plot with titles using previously selected font sizes
fig, ax = plt.fill_between(x, y)
ax.set_title('Test Area Plot', fontdict = font1)
ax.set_ylabel('Y Axis', fontdict = font2)
ax.set_xlabel('X Axis', fontdict = font2)


##July 25th session

#Import Libraries
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd

#Generate Random Seed
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)

#Create Line Graph with 2 lines on the same axis. Add Legend on lower right with a frame, fontsize 12, horizontally aligned, with shadow.
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y1, label = "Person 1")
ax.plot(x,y2, label = "Person 2")
ax.legend(loc = "lower right",
        frameon = True,
        fontsize = 12,
        ncol = 2,
        shadow = True)

#Create a scatter plot from 0-10 on both axes
fig, ax = plt.subplots()
ax.axis([0,10,0,10])

#place "Data: (1,5)" where the data should be, place "Axes: (0.5,0.1)" on the axis coordinates are, place "figure: (0.2,0.2)" where the figure coordinates are. 
ax.text(1,5,"Data: (1,5)",transform=ax.transData)
ax.text(0.5,0.1,"Axes: (0.5,0.1)", transform = ax.transAxes)
ax.text(0.2,0.2,"figure: (0.2,0.2)", transform = fig.transFigure)

#Create a 5x3 size scatter plot, 1st dataset is "Person 1", 2nd dataset is "Person 2", add legend in bottom right.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend (loc = 'lower right')

#Add a Hotpink wedge as an arrow pointing to (10,95). Put text "This is Important!" on (20,94) so it is alongside the arrow.
ax. annotate ("This is Important!", xy = (10,95), xytext=(20,94),
              arrowprops = dict(arrowstyle = "wedge",
                                color = 'hotpink'))

#Remove y axis numbers and markers and remove x axis numbers only
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

#Create a 5x3 size scatter plot, 1st dataset is "Person 1", 2nd dataset is "Person 2", add legend in bottom right.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend (loc = 'lower right')
#Edit to only have 3 x axis markers
ax.xaxis.set_major_locator(plt.MaxNLocator(3))


#Create a 5x3 size scatter plot, 1st dataset is "Person 1", 2nd dataset is "Person 2", add legend in bottom right.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend (loc = 'lower right')

#Edit to have x markers every 5 data unit intervals 
ax.xaxis.set_major_locator(plt.MultipleLocator(5))

#Create a 5x3 size scatter plot, 1st dataset is "Person 1", 2nd dataset is "Person 2", add legend in bottom right.
fig, ax = plt.subplots(figsize=(5,3))
ax.scatter(x,y1, label = "Person 1")
ax.scatter(x,y2, label = "Person 2")
ax.legend (loc = 'lower right')

#Create a font family to be serif and indigo color, then make an x axis label "Shiny New X Axis!", fontsize 18 with the font family.
font1 = {'family':'serif','color':'indigo'}
plt.xlabel('Shiny New X Axis!',fontsize =18,fontdict=font1)

#Set to use the "classic" style on the graphs 
plt.style.use('classic')

#Create a Scatterplot to see the style
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y1)

#Reimporting libaries if needed
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd

#Generate Random Seed
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0,100,50)
y2 = np.random.randint(0,100,50)

#Create a 5x3 scatterplot with y1 as "Person 1", y2 as "Person 2", create a legend top right of the graph.
fig, ax = plt.subplots(figsize=(5,3))
ax.plot(x,y1, label = "Person 1")
ax.plot(x,y2, label = "Person 2")
ax.legend(loc = "lower left",
          bbox_to_anchor =(1,1))

- When there are individual or group activities in submodules, make notes of answers and key points from discussions
- Following each lesson with code, submit a document (either .py or a Jupyter notebook) containing the functioning code from that day's lesson, along with any written notes or comments.

#Reimporting libraries if needed
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import scipy
  import PIL
  import requests

#Generate a randomseed dataset & a defined dummy dataset
np.random.seed(613)
x1 = np.arange(50)
y1 = np.random.randint(0,75,50)
x2 = np.array(['Luffy','Zoro','Nami','Usopp','Sanji'])
y2 = np.array([110,180,240,99,220])

#Generate space for graphs side by side horizontally, 7x3 combined size.
fig, (ax1,ax2) = plt.subplots(ncols=2,
                              nrows =1,
                              figsize=(7,3))
#Create a scatterplot with dataset 1 and bar graph on dataset 2
ax1.scatter(x1,y1)
ax2.bar(x2,y2)

#Generate space for graphs side by side horizontally, 10x3 combined size.
fig, (ax1,ax2) = plt.subplots(ncols=2,
                              nrows =1,
                              figsize=(10,3))

#Set font family, Serif & Indigo color
font1 = {'family':'serif','color':'indigo'}
#Create scatter plot with title 'Last seen Chopper Appearances' using font family
ax1.scatter(x1,y1)
ax1.set_title('Last Seen Chopper Appearances',fontdict=font1)
#Create bar chart with x axis label saying '# of Hats', fontsize 18, using font family
ax2.bar(x2,y2)
ax2.set_xlabel('# of Hats',fontsize =18,fontdict=font1)

#Creating a 7x4 size Mosaic in a 2x2 grid with constrained layout. Ax1 top left, Ax2, bottom left, and AX3 for the entire right side 
fig, someaxes = plt.subplot_mosaic([['ax1','ax3'],
                                    ['ax2','ax3']],
                                     figsize = (7,4),
                                     layout = 'constrained')

#Creating Scatterplot for ax1, bar chart for ax2, plot for ax3. 
someaxes['ax1'].scatter(x1,y1)
someaxes['ax2'].bar(x2,y2)
someaxes['ax3'].plot(x1,y1)
#Giving x axis labels all size 18, "A big label" for ax1, "Another label" for ax2, Label 2: 2 Fast 2 Furious" for ax3.
someaxes['ax1'].set_xlabel("A Big Label!", fontsize=18)
someaxes['ax2'].set_xlabel("Another Label", fontsize=18)
someaxes['ax3'].set_xlabel("Label 2: 2 Fast 2 Furious", fontsize=18)

#Generate new Dummy Data & Calculate std error for y2 
x = np.array(['Luffy','Zoro','Nami','Usopp','Sanji'])
y1 = np.array([110,180,240,99,220])
y2 = np.array([170,100,90,130,50])
y2_sd = np.std(y2)

#Create a 7x3 chart
fig, ax = plt.subplots (figsize =(7,3))

#In the space provided, create a indigo Bar chart using Y1, red line chart using Y2. Apply light blue error bars to show std error every other point in the dataset. Error bars have with of 4, capsize 6, capthickness 4. 
ax.bar(x,y1,
       color = 'indigo')
ax.plot(x,y2,
        color = 'red')
ax.errorbar(x,
            y2,
            yerr = y2_sd,
            fmt = "none",
            ecolor = "lightblue",
            elinewidth = 4,
            capsize = 6,
            capthick = 4,
            errorevery = 2)

### Why am I doing this assignment?:

- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes:
*	Create and customize data visualizations from start to finish in Python
*	Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component          | Scoring                 | Requirement                                              |
|--------------------|-------------------------|----------------------------------------------------------|
| Completion         | Complete/Incomplete for each class| - All required work from a given class is included in the file |
| Markdown file format | Complete/Incomplete for each class| - File is readable and contains functional code, when needed |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Note:

* You should make a commit after each session with that lesson's code and notes. Your PR should have the same number of commits as there are sessions. It is important to make the commits to your branch in a timely manner right after each class.

### Submission Parameters:
* Submission Due Date: `last day of class`
* The branch name for your repo should be: `assignment-1`
* What to submit for this assignment:
    * The `participation` folder/directory should be populated with the above mentioned .py/.ipynb files along with any written notes or comments (preferably in .md or .txt format).
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-1`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack at `#cohort-3-help`. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
