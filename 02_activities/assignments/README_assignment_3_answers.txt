For python visualization:

What software did you use to create your data visualization?
Answer: I used python to create the data vis, with the following packages: pandas, json, folium and branca. 

Who is your intended audience?
Answer: Officials (Toronto Municipality).

What information or message are you trying to convey with your visualization?
Answer: With the map, I am trying to convey the importance of bike infrastructure in locations that have been targeted by the Ontario government (eg Bloor St bike lanes). The idea is that a lot of people use the Bloor line and the Yonge line, so these streets should be targeted for better bike infrastructure, removal of potholes, bike lights etc. At the same time, we see the congestion of these roads mainly because there are no other alternatives, for example on Spadina Avenue, Jarvis etc.

What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?
Answer: I thought about visualizing the congestion on the map, which is why I used the map library folium, and colour to indicate low-high numbers. In addition, I thought about using a point visualization rather than a grid, because these counts are from detectors, not use of bikes in the area. Important things that I considered in the visualization were the size of the circles (bigger means larger numbers), colour (red means larger numbers), and date (I used 2024 data, because during the COVID period there was a dip in the use of non-motorized vehicles). I also added a way to interact with the figure, whereby you could press the circles, and the location name, number of counts and eastbound/northbound information would appear.

How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?
Answer: I tried to make the visualization as reproducible as possible. Here, I wrote text indicating the link where I downloaded the data from, I included the names of the files I downloaded. I also added the files in the repo, for ease of downloading. Another thing that I did was to use comments to explain my code, I created functions in order to not worry about inputting the wrong path for the files. Finally, I added a note on how to download packages that may need to be installed.

How did you ensure that your data visualization is accessible?
Answer: By adding the click function on the circles, I can show the location, numbers and eastbound/northbound information, regardless of the colour or circle size (the difference isn't that large).

Who are the individuals and communities who might be impacted by your visualization?
Answer: Everyone in the city could be impacted, especially the biking community. By showing the use of bikes in the city, better infrastructure can be built.

How did you choose which features of your chosen dataset to include or exclude from your visualization?
Answer: I decided to only use longitude, latitude, direction, location_dir_id, last_active and location_name because for the purposes of my visualization, nothing else was needed. I wanted location name, counts of rows that either went eastbound or northbound, and the location_dir_id that I could use to combine the geojson data to.

What ‘underwater labour’ contributed to your final data visualization product?
Answer: Some of the underwater labour that contributed to the final data visualization is designers who created the python libraries and colour palettes, the open source map, the people who organized the data in the website, the people who maintain the website. The families of these workers who had to help them emotionally, mentally and physically in order for them to be able to do work and be healthy, the people who maintain the servers on which the data is stored, the unseen cooperation required to keep a website like the City of Toronto database working, and more.




For Excel visualization:

What software did you use to create your data visualization?
Answer: I used excel to create the bar chart.

Who is your intended audience?
Answer: The officials at Toronto municipality.

What information or message are you trying to convey with your visualization?
Answer: I am trying to show the number of cyclists that have used bike lanes in different parts of the city, and which streets are busier. I am trying to show if Northbound or Eastbound detectors showed more activity, to show the flow of bike-related "traffic". 

What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?
Answer: For this visualization, I wanted to create a graph that excel can create, but also try to convey as much information as possible. Thus, I used a bar chart with colour, and I grouped the information by street name. Writing the location on each bar helps with accessibility, and the colours chosen are not red or green (the most common type of colour blindness). In order to convey size I used the horizontal axis to allow for better comparability. I also added grid lines in order to make it easier to understand what number each bar corresponds to on the x axis.

How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?
Answer: My visualization is not reproducible because in order to work with excel, I had to manually combine the datasets that I downloaded from the open source database. I also had to manually pick which streets and which detectors to analyze, and it is much harder to add notes for each action taken in excel. Because of this, it will be really hard to reproduce the figure, even if the data is all there. One way that I show which data I kept is through the title: (Looking at 2024 data), and the detector data, which correspond to specific streets and direction.

How did you ensure that your data visualization is accessible?
Answer: I used both colour and text to indicate what each bar corresponded to. I also used a gridded plot in order to make readability better.

Who are the individuals and communities who might be impacted by your visualization?
Answer: As before, all people who use bikes in the city will be impacted.

How did you choose which features of your chosen dataset to include or exclude from your visualization?
Answer: I had to pick one northbound and eastbound detector for each street, in order to make the graph less busy. Thus, I picked the detectors for which the numbers were not the same. In this way, I tried to show more variability, which exists in the dataset.

What ‘underwater labour’ contributed to your final data visualization product?
Answer: As before, the dataset "underwater labour" is the same. Some labour that was not mentioned above is the people who created videos on how to create bar charts on YouTube, people who work to keep Excel functional, and the people who helped them be able to work.