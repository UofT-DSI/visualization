# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 

Data source: https://map.toronto.ca/wellbeing/#eyJ0b3Itd2lkZ2V0LWNsYXNzYnJlYWsiOsSAcGVyY2VudE9wYWNpdHnElzcwfSwiY3VzxIJtYcSTYcSXxIBuZWlnaGJvdXJob29kc8S2fcSrxIHEg8SFxIfEicSLdGFixYXEmCLEo3RpdmVUxZBJZMSXxYnEhMWPYi1pbmRpY2HEgnLFhcWIYWdzTWFwxLYiesWCbcSXMTPErHjEly04ODM3NzYzLjXGhDcyN8SsxKc6NTQxMjkzMS4yNMaDMjg1xYjFpMWmxajFqsWSxIDFmMWraW9uxJcyxKxzxaRnbGXFtMSucsSTxJ9UaW1lxZzEqMSsxZbGucajIjfFtMafxafFqcSDxZxzQcWlV8S5xLt0xZJbxIDEh8WexpQzIsSsd8eNaHTFucSsxJPGpXNlUG%2FEjnLEpcaOZmFsx6HEq8eSxZ06IjEwxbrHlyLHmcS6x5vHnSLHn8Sbx6HHo8elx6fEl8epx6tlfV3Fh8WIxr5lx6HHpsiLxYbErMazxrV0ScWlx4XFqk3Fg8axx7DGrW7Gr8axxYc%3D


- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?
        Python: I made two scatter plots in Python. One of them is an interactive graph, which is helpful for exploring neighborhood-level data, otherwise the legend is too long.
        R: I made a linear regression plot that reveals the relationship between the two selected variables.

    > Who is your intended audience? 
        General residents living in Toronto, community advocates, and urban policy researchers 

    > What information or message are you trying to convey with your visualization? 
    The visualizations were designed to explore the research question of "Is there an association between access to healthy food and early development scores across Toronto neighborhoods?." 

    The scatterplots were created more for an explortary purpose, wherase the linear regression plot actually reveal the relationship. In contrast, the linear regression plot provided a more formal and interpretable representation of the relationship by fitting a trend line, revealing both the direction and strength of the association.

    Notes:
    The healthy food index (also known as Modified Food Retail Environment Index) represents the closeness of the population to healthy food retail establishments across the City. 
    Lower scores in healthy food index indicate higher healthiness of the retail food environment. Higher scores in healthy food index indicate a more unhealthy retail food environment. 

    Early Development Instrument (EDI) indicates the proportion of participants who scored low on 2 or more domains (data for 3 years). 
    Lower numbers in early development instrument indicate better results of children's ability to meet age-appropriate developmental expectations. 
    Higher numbers for this indicator indicate worse results.  

    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    I focused on simpleness, color differentiation, and interactivitity when making visualization. 
    For the first graph, each dot was given a unique color to visually distinguish neighborhoods.
    For the second graph, I incorporated hover tooltips that display the neighborhood name, Healthy Food Index score, and Early Development Instrument score when pointing to a dot. This interactivity helps users explore neighborhood-level data more easily, especially when the number of neighborhood is large.

    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    The visualization is fully reproducible using the provided Python/R codes and open-access CSV data (link provided above). I used pandas for data wrangling and plotly.graph_objects for plotting scatterplot and ggplot for plotting the linear regression plot. The dataset has no missing data, requiring minial effort for data cleaning and preprocessing.

    > How did you ensure that your data visualization is accessible?  
    In scatterplots, I used large font sizes, clear axis labels, and different color, and interactivity to help avoid confusion caused by overlapping points.
    In linear gression plot, I also showed the intercept and slop of the regression line on the plot. 

    > Who are the individuals and communities who might be impacted by your visualization?  
     The visualization may be useful for community organizations advocating for healthy food access and education resources. It may raise awareness among residents and policymakers about source disparities across neighborhoods.

    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    I focused on two variables, Healthy Food Index and Early Development Instrument, based on my personal interest as well as their conceptual relevance. Other variables that are relevant to healthy food index could be income level and demographic factors. 
    
    > What ‘underwater labour’ contributed to your final data visualization product?
    Writing and debugging Python/R code.
    Iteratively testing the visual layout, color scheme, font sizes, legend clarity, etc.

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
