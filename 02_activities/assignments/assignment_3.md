# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?

The first data visualisation was created on Python, whilst the other was created through Tableau Public. 

    > Who is your intended audience? 
Our intended audience for both visualisations were dog owners living in the Greater Toronto Area and/or general public interested in the register of dogs issued a dangerous dog order. 


    > What information or message are you trying to convey with your visualization? 
The first visualisation aimed to show the top 10 dog breeds with highest frequency of bite circumstances warranting a dangerous dog order over the span of 2017-2025. In addition, the visualisation was aimed to show the distribution of bite circumstances (e.g., severity of the bite) within each breed listed. 

The second visualisation aimed to show the number of dogs issued dangerous dog orders across 2017 to 2025 divided up by bite circumstances. The aim was to see whether there would be any periods of time where the frequency of dogs issued a dangerous dog order was higher or lower, and if so, what kind of bite circumstance was the most frequently occurring. 

    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    
In the first visualisation, accessibility was a key consideration of the design. Although initial hopes were to have a visualisation that would show the distribution of dog species, bite severity and location in one figure, it was deemed to be too complicated. Due to this, a simpler yet meaningful visualisation was planned. When coding the visualisation, another consideration for accessibility was the colour palette. Due to this, colourblind friendly palettes were used in the form of the viridis package from matplotlib. Additionally, a legend showing the different colours was also added to show the classification of bite severity. 

In the second visualisation, key concepts of design that was considered included contrast where each line was a different colour and clearly differentiated from the axis and grid lines. Additionally, a clean 2D layout with sufficient spacing was also considered and applied. 

Both figures ensured aesthetics were accessible and that the information was substantive in which with the labelling and legends, the visualisations could guide individuals in seeing the trends and distributions of dog breeds and dog orders overtime. 

    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 

In the first visualisation, to ensure that it was reproducible, python was used and the code was annotated with comments to ensure ease of understanding for what each line represented.

The second visualisation is not reproducible as it was conducted in Tableau which is a drag and drop program. Without an information sheet showing detailed steps on how the visualisation was created, reproducing or editing the visualisation will be extremely difficult. Tableau has an option to make visualisations publicly available however so its possible more details could be added to make it further reproducible (e.g., adding source of dataset etc)

    > How did you ensure that your data visualization is accessible?  

 To ensure that the data visualisation was accessible, large font size, colourblind friendly palettes and axis labelling were used for both visualizations. However, it must be noted that more can be done. Annotation of data values on the figure and a caption on the bottom of the figure showing what was displayed on the visualisation would have been beneficial.   

    > Who are the individuals and communities who might be impacted by your visualization?  

Individuals who are dog owners either living in or moving to Toronto who were concerned about dog safety would be impacted by the visualisation. Additionally, as the first visualisation specifies the dog species, breeders / owners of these dog breeds may be negatively impacted due to its implied message that their dogs are prone to biting. One aspect that must be noted is that this is a small sample and only shows extreme circumstances (e.g., where a report is made), and that it should not be used as a generalisation of stating that a certain dog breed is more dangerous than another. The second visualisation only shows frequency over time. However, as the data is still being collected and updated, 2025 may appear to show a drop-off in frequency, but in actual fact the data is incomplete. This could be misleading in that it can be perceived that the number of dog orders being issued is decreasing.      

    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 

Originally I hoped to include a large number of variables in the dataset including location/ward of incidence. However, due to concerns that this may result in overcomplication of the data visualisation, these variables were excluded. Additionally, for the first figure, all breeds were planned to be presented on the visualisation. However, as there were too many species to show on one x-axis, it was determined that the data would be filtered to only show the top 10 most frequent dog breeds. This filtering was not conducted on the second visualisation. Ideally the second visualisation on Tableau was hoped to also show a mapping of incidence reporting showing where in the GTA the incidents were reported. However, as the dataset did not have the full postal code, this was not achievable, hence was excluded.  

    > What ‘underwater labour’ contributed to your final data visualization product?

The individuals who reported the incidents and the data managers who update the dataset every two months are some examples of underwater labour that contributed to the final data visualisation. Additionally, city workers who log the incidents and register dogs that have two or more incidents into the registry are considered underwater labour as well.  

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
- [X] Create a branch called `assignment-3`.
- [X] Ensure that the repository is public.
- [X] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [X] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
