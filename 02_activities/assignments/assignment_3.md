# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 

Visualization #1
> What software did you use to create your data visualization?
        I used VS Code to create this visualization: ![python_visualization](image-3.png)
> Who is your intended audience? 
        My intended audience is people in healthcare including government workers. 
> What information or message are you trying to convey with your visualization? 
        My visualization shows how many people died in shelters across years separated by sex. 
        Specifically, we can see from the graph that the number of decedents for both males and females decreased again after the pandemic years. We can see that there were many deaths between 2019-2022, especially among males, in homeless shelters. Another interesting observation is that males died substantially more in pandemic years than females.
> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?  
        I wanted to ensure that we can see the number of deaths across all years and how it was changing (when the highest and lowest number of deaths were), so a line plot would be ideal in this case. I also wanted to show the male and female data separately so I plotted two lines of different colors (pink for female and blue for male). The chosen colors would also make it easier to understand and remember the graph since pink is associated with females and blue with males. The shade around the line is standard error of the mean. I also didn't use any strong language or add any arrows/pointers anywhere to ensure the visualization looks as neutral as possible.   
> How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
        My data visualization is reproducible because the raw data and code are easily accessible and I also commented my code. If people access the code and view the comments, which would help them understand how the data was analyzed and what each step means, then they should be able to reproduce it.   
> How did you ensure that your data visualization is accessible?  
        The code and the data are both accessible to public. They can be found on GitHub. 
> Who are the individuals and communities who might be impacted by your visualization?  
        My visualization indirectly points that the government support for people in need is susceptible to situations like lockdowns (although the deaths may also be linked to covid itself). Health care individuals are also impacted by this. 
> How did you choose which features of your chosen dataset to include or exclude from your visualization? 
        I didn't include the months and individual data. This data isn't very informative when it comes to understanding how people in shelters are doing over the years and whether there is any progress. 
> What ‘underwater labour’ contributed to your final data visualization product?
        Initially my data was in wide format (there were separate columns for males and females) so I had to manually change it to long format. I created a separate column called "Sex". With the wide format, I wouldn't be able to run my code the way I did. 

Visualization #2
> What software did you use to create your data visualization?
        I used JASP to create this visualization: ![JASP_Visualization](image-4.png)
> Who is your intended audience? 
        My intended audience is people in healthcare including government workers.
> What information or message are you trying to convey with your visualization? 
        My visualization shows how many males and females die in shelters in the last 3 years (2024-2026). The main focus is the difference between males and females in number of deaths in shelters after the pandemic. Males in shelters are more likely to die than females even after the pandemic. 
> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?  
        It is hard to design plots on JASP as there is no option to code. However, I tried to create a boxplot which each box representing sex. I also overlaid it with a violin plot to show where the individual data points mostly lie for each sex. The plot is color-coded for an easier visualization. I didn't use any strong language to ensure the visualization looks as neutral as possible.   
> How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
        The visualization is reproducable because I saved the JASP workbook with all the raw data and analyses I ran and made it accessible on GitHub. 
> How did you ensure that your data visualization is accessible?  
        The raw data as well as the JASP workbook are publically avaialble on GitHub.
> Who are the individuals and communities who might be impacted by your visualization?  
        In this case also it would be the healthcare workers especially those within the government sector. We want to understand why males have such high mortality rates: are they overlooked in some way? This is an issue even in the recent years. 
> How did you choose which features of your chosen dataset to include or exclude from your visualization? 
        I excluded the pandemic years and the years before that because I wanted to visualize how the data looks in the most recent years under normal conditions (without the influence of other external factors like covid and lockdown). If the data looks concerning even under normal conditions, then there are serious systematic issues that must be addressed. I also excluded the months because it's not important for the question I am asking.
> What ‘underwater labour’ contributed to your final data visualization product?
        On top of converting the data from wide format to long format and creating a "Sex" column, I had to also delete the entries corresponding to the years before 2024. 

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
* Submission Due Date: `23:59 -  2026-06-16`
* The branch name for your repo should be: `assignment-3`
* What to submit for this assignment:
    * A folder/directory containing:
        * Two distinct data visualizations (for example, PNGs, PDFs, or screenshots)
        * Two Markdown files answering all questions for each visualization (including a link to your dataset in both files)
        * One Python file contains the complete code and visualization, and another file (with or without code) contains the visualization.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
