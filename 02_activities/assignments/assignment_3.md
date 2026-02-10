# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  

The dataset i chose was from this website: 
https://data.ontario.ca/dataset/ontario-top-baby-names-male/resource/9571139d-e505-4a35-82fa-192af66c5714

This dataset is about Ontario top baby names (male).
The tools i used was Python and Google Sheet.

See my Assignment 3 ipynb doc for python code.
see this link for google sheet analysis. https://docs.google.com/spreadsheets/d/1GLQFEEPWy-6nAB5E_MTBAtT1gAzSU0TkH2iQRuExRxY/edit?gid=1596697244#gid=1596697244


For python:
- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?
    Visual Studio Code and Python.
    This visualization was created using Python, specifically the pandas library for data processing and matplotlib for plotting.
    > Who is your intended audience? 
    The intended audience includes parents, educators, and students who are interested in understanding long term trends in baby name popularity in Ontario.
    > What information or message are you trying to convey with your visualization? 
    This visualization shows how the popularity of selected male baby names in Ontario has changed over time between 2000 and 2023. It highlights both rising and declining naming trends rather than focusing on a single year snapshot.
    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    A line chart was chosen because it is well suited for representing change over time. Clear axis labels and a descriptive title were included to support interpretation. Different markers and line styles were used so that trends can be distinguished without relying only on color.
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    The visualization is reproducible because it is generated entirely through a Python script. The script reads fixed input files from Ontario’s Open Data Catalogue, applies deterministic cleaning and filtering steps, and saves the output figure programmatically.
    > How did you ensure that your data visualization is accessible?  
    Accessibility was considered by using readable font sizes, clear labels, and visual distinctions beyond color such as markers and line styles. The legend explicitly labels each name to avoid ambiguity.
    > Who are the individuals and communities who might be impacted by your visualization?  
    Parents and families may use this information when considering baby names. The visualization reflects male naming data as categorized in the original dataset, which represents binary sex classifications and should be interpreted within that limitation.
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    Only a small set of well known male names and years from 2000 to 2023 were included to reduce visual clutter and improve interpretability. Less frequent names were excluded to keep the focus on dominant trends.
    > What ‘underwater labour’ contributed to your final data visualization product?
    Underwater labour included cleaning bilingual column names, standardizing text formatting, filtering the dataset by year and sex, selecting representative names, and testing multiple design choices to ensure clarity.

For Google Sheet:
    > What software did you use to create your data visualization?
    This visualization was created using Google Sheets.
    > Who is your intended audience? 
   The intended audience is a general public audience, including parents and educators, who want a quick and accessible overview of popular male baby names in Ontario. 
    > What information or message are you trying to convey with your visualization? 
   This visualization shows the relative popularity of the top 10 male baby names in Ontario in a single recent year. It emphasizes comparison across names at one point in time. 
    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
   A bar chart was selected because it supports straightforward comparison across categories. A simple color palette, clear axis labels, and an informative title were used to reduce cognitive load and support readability. 
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
   Google Sheets visualizations are not fully reproducible in the same way as code based workflows. However, the chart can be recreated by applying the same documented steps, including filtering by year and sorting by frequency, to the publicly available dataset. 
    > How did you ensure that your data visualization is accessible?  
   The visualization uses clear text labels, a simple layout, and does not rely on color alone to communicate values. The chart is readable without prior technical knowledge. 
    > Who are the individuals and communities who might be impacted by your visualization?  
   Parents and families may be influenced by perceptions of name popularity. As with the Python visualization, the chart reflects male naming categories as defined in the dataset. 
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
   Only the top 10 names from a single year were included to keep the visualization focused and easy to interpret. Lower frequency names were excluded to avoid overcrowding. 
    > What ‘underwater labour’ contributed to your final data visualization product?
    Underwater labour included filtering the dataset by year, sorting by frequency, selecting a subset of names, and adjusting chart settings to improve clarity and presentation.

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
* Submission Due Date: `23:59 - 11/02/2025`
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
