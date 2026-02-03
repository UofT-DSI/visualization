## dataset link: 

https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/

## What software did you use to create your data visualization?
graphpad - prism

## Who is your intended audience? 
the general public of the GTA

## What information or message are you trying to convey with your visualization? 
I would like to show the rates of occupancy per sector, driving home the message that regardless of sector most shelters are at 100% occupancy right now (can see this with the concentration of points at the upper limit). There is thankfully fewer families needing shelters (fewer dots) and lower occupancy rates. However youth, women and men are usually shelters relatively equally.

## What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
I wanted to make sure that each shelter is represented so I chose a scatter plot, and I wanted to emphasize that most shelters are at occupancy therefore I made the dots semi-transparent so a concentration of colour would draw the viewers attention.
I wanted to reduce visual anxiety so labels and titles are as minimal as possible. 
I also used the viridis colour package to accomodate colour blind viewers.
additionally, I used flat graphics vs 3D to reduce visual load and included the bars along with the individual dots to help the viewers see that women, men, and youth are relatively equal ( = everyone needs help)

## How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
While my visualization was created on prism, I provide the excel workbook with the data I used and sheets to show how I manipulated the data to be processed for the graphs as well as a data_info sheet to explain
## How did you ensure that your data visualization is accessible?  
1. I used viridis colour package
2. texts are all at least 12 pt font
3. I used a dyslexia friendly font type (verdana)
    
## Who are the individuals and communities who might be impacted by your visualization?
I hope to impact the unhoused community with this visualization as the visualization is made to influence some positive change in the shelter situation in the GTA.  
    
## How did you choose which features of your chosen dataset to include or exclude from your visualization? 
I did not want the graph to be too busy and I wanted to drive home a clear message so I only included 2 variables and did not include any excess information. I chose to include shelters with bed occupancy instead of rooms because this data type shows exactly how many individuals are impacted as one bed = one person. With rooms you cannot grasp how many people are impacted from a glance.
    
## What ‘underwater labour’ contributed to your final data visualization product?
- work by the shelter staff to report these numbers
- work by city analysts to coalesce and clean the data
