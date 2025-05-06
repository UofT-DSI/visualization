# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify:

# Visualization 1: TTC Delays (Average Time in Minutes) by Direction Bound and Month of the Year

    > What software did you use to create your data visualization?
    
    I used Tableau Public to create this data visualization: https://public.tableau.com/views/2024AverageTTCDelaysbyDirectionandMonth/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

    > Who is your intended audience? 
    
    The intended audience is individuals who use the Toronto TTC system at any point during the year.
    
    > What information or message are you trying to convey with your visualization? 
    
    The visualization conveys information regarding average delay times in minutes by month of year and direction of the TTC vehicle.  
    
    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    
    I used a line plot to convey the continuous nature of time (e.g., the average delay time by minute) across another ordered variable of months of the year. I also thought it would be interesting to examine how these delay times across the year differed by the direction the train was going, so I plotted four different, distinct colored lines to represent each of the cardinal directions (North, South, East, West). I also included the minimum and maximum averages on figure to highlight this piece of information for the audience. By plotting all of lines together on a single pane, this allows for ease of comparison with longer delay times represented by higher peaks, and lower delay times represented by lower peaks. 
    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    
    To ensure that my data visualizations are reproducible I used a publicly accessible resource, Tableau Public, to create the visualization. The data is also publicly available at: https://open.toronto.ca/dataset/ttc-subway-delay-data/. I did not alter, clean, or drop any of the existing data from the original datafile, ensuring that the same visualization should be reproducible. 
    
    > How did you ensure that your data visualization is accessible?  
     
     I used a color-blind accessible color palette available through Tableau, and I also adjusted the line thickness so that the contrasting colours would be easier to perceive. To help facilitate understanding of the figure, I used labels and titles to describe what each axis depicts.
     
    > Who are the individuals and communities who might be impacted by your visualization?  
      
      The Toronto Transit Commission and individuals who take the subway system in toronto might be impacted by this visualization. In particular, those who need to commute Eastward or Westward, as those directions featured the maximum and minimum delay times in the visualization. 
    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
     
     I excluded an additional directions mentioned in the datafile,'B' which wasn't clear to me what it meant. Reading through the additional resources available alongside the datafile also did not seem too helpful in clarifying its meaning. Although I could have plotted figures for each train line rather than direction, this would have been visually very busy as there are many different train lines within the TTC system. Thus, I decided to use a more general grouping factor of direction bound to generally capture and present data regarding how delay times differ across the year depending on the directionality of train. One can extrapolate that different lines going the same direction experienced similar delay times as indicated by the line plot. 
    
    > What ‘underwater labour’ contributed to your final data visualization product?
     
     People who work for Tableau Public and host the visualization on their server, the Toronto government employees who collected and uploaded the data and ensure data quality. 

# Visualization 2: Top Reasons for TTC Delays in 2024

    > What software did you use to create your data visualization?
    
    I used Python to create this data visualization using the packages matplotlib and seaborn.

    > Who is your intended audience? 
    
    The TTC (Toronto Transit Commission), and individuals living in Toronto who use and/or are familiar with the transit system.
    
    > What information or message are you trying to convey with your visualization? 
    
    The visualization conveys information about the top reasons for TTC delays in 2024. 
    
    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
     
     Since I aimed to explore the reasons why the TTC was delayed in 2024, I compared the proportion of each type of delay (denoted by a code) in order to reveal any insights from the data, such as whether one type of delay is responsible for the majority of TTC delays in 2024. Because my variable of delay type was categorical, and I wanted to compare the proportions of each delay type, I decided to visualize the data through a donut chart -- a type of pie chart. I also used distinct colors as an identity channel to indicate categorical differences in types of delay, rather than gradient colors which would indicate differences in strength of an attribute. Because it may be more difficult to conceptualize the relative differences in delay type proportions by just comparing the size of the wedges alone, I also made sure to include the percentage labels within each wedge to make this piece of information more clear. I also wanted to highlight the ordered nature of proportional differences so the donut chart lists the delay type from highest to lowest percentage in counterclockwise order. 
    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 

    To ensure that my data visualizations are reproducible I used a publicly available a programming language and software, Python (in VS Code), to create the visualization. The data is also publicly available at: https://open.toronto.ca/dataset/ttc-subway-delay-data/. I annotated my code and also noted where and how I cleaned or dropped data.
    
    > How did you ensure that your data visualization is accessible?  
    
    I used the colorblind palette in seaborn, and I also included a limited number of categories to aid in visual clarity. I also bolded the percentages in black to make them easier to see, and included whitespace between the wedges to emphasize the different sections more clearly.I also tried to use simple and clear language in my title and labels, that balanced the specificity of the definitions mentioned for each code, as well as accommodated pre-existing knowledge an individual might have regarding the terminology related to transit (e.g., train door, track level).
     
    > Who are the individuals and communities who might be impacted by your visualization?  
      
      Those who are interested in evaluating TTC performance, and/or evaluating reasons for why there are delays might by impacted by this visualization. Specifically, TTC employees or those who live in Toronto might find it particularly relevant.
    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    
    First of all, I dropped all rows in the dataset for which a delay time of 0 minutes was reported, because I am only interested in evaluating the events that were causing delays. I also divide up the donut chart into just eight categories. Although there are many more different types of delays, I decided to reduce the number of different types to eight, including a grouped category which features all of the types of delays that each occur less than 3% of the time. This was done to reduce the visual clutter on the figure and to ensure that the information was still simple and clear to the audience. I reasoned that the seven distinct reasons for delays accounted for more than 50% of the delays in 2024, so the majority of delays were visually segmented, while the eighth 'other' segment accounted for the many different, more minor delay types, that, for the purposes of this particular visualization were not as relevant to be included as separate segments. 
    
    > What ‘underwater labour’ contributed to your final data visualization product?
        
    People who coded Python backend, and the Python visualization packages (matplotlib and seaborn), the people who contributed to Stack Overflow forums which provided me with coding references for my visualization, and the Toronto government employees who collected and coded the data. 

- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 09/05/2025`
* The branch name for your repo should be: `assignment-3`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_3.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
