# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  

### Database Selection: 
- Killed and Seriously Injured (KSI) Collisions – City of Toronto’s Open Data Portal_Toronto Police Service Open Data: https://data.torontopolice.on.ca/datasets/TorontoPS%3A%3Akilled-and-seriously-injured/about

### Visualization Description: 
- Visualization 1: Temporal Trend Analysis using Line chart for Annual number of KSI collisions in Toronto (2006–2024); 
- Visualization 2: Non-spatial comparison was used to accurately and transparently compare collision burden across Toronto neighbourhoods (2006–2024). Sorting and filtering were applied to highlight the top 15 neighbourhoods with the highest collision counts.

- For each visualization, describe and justify: 
    > What software did you use to create your data visualization? Python (pandas + matplotlib);Tableau Public

    > Who is your intended audience? 
    Policy analysts; Urban planners; Public health researchers; General Public

    > What information or message are you trying to convey with your visualization? 

    - Visualization 1: Despite infrastructure investments, serious traffic injuries in Toronto show uneven improvement over time, with clear spikes corresponding to systemic factors rather than random variation.

    - Visualization 2: Traffic injury risk is not evenly distributed across Toronto spatially, some neighbourhoods bear a disproportionate burden.

    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    - Clarity & Cognitive load: My primary design consideration was minimizing cognitive load so that viewers could quickly understand the main message without unnecessary interpretation. For the time-series visualization, a simple line chart was chosen to represent changes in KSI collisions over time, as line charts are well suited for displaying temporal trends. Gridlines were kept subtle, and unnecessary visual elements such as decorative icons or excessive annotations were avoided. 

    - Perceptual Effectiveness: Design choices were informed by research indicating that position along a common scale is one of the most accurate visual encodings for quantitative data. In the time-series plot, annual KSI counts were encoded using vertical position on a shared y-axis, allowing viewers to accurately compare values across years. In the choropleth map, spatial position and color intensity were used to represent geographic variation, enabling viewers to perceive regional patterns at a glance.

    - Layout and Visual Hierarchy: Visual hierarchy was established through size, placement, and emphasis. Titles were positioned prominently to communicate the main message of each visualization, while secondary elements such as gridlines and legends were visually de-emphasized. Consistent margins and spacing were applied to prevent overcrowding and to guide the viewer’s eye naturally from the title to the data.
    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 

    - I saved the fully reproducible Python script and generated the deterministic output from raw CSV. the environment is also version-controlled to ensure the generation of the same results based on the same code. With the raw data, one can re-produce the plot using other data visualization tool based on plot description. 

    - For the visualization 2, I created Tableau public workbook shared publicly. However the interactive filters cannot be version-controlled like python code so it might be mitigated by static export and methodological description.
    

    > How did you ensure that your data visualization is accessible?  

    I applied high-contrast default matplotlib palette with no reliance on color alone. Alt-text description and summary is also included in caption.
    
    > Who are the individuals and communities who might be impacted by your visualization?  

    Residents/potential house-buyers of high-risk neighbourhoods; Pedestrians and cyclists; Equity-seeking populations
    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    - For Visualization 1: I included year + severity to supports causal reasoning. I excluded factors of weather and lighting since secondary confounders not central to narrative

    - For visualization 2: I included neighbourhood, KSI count to demonstrate the distribution of KSI based on spatial map, and exluded the exact coordinates to ensure the protection of privacy & ethical consideration.
    
    > What ‘underwater labour’ contributed to your final data visualization product?
    Data Cleaning & Validation: 
    - Identifying missing or malformed values in ACCIDENT_YEAR; 
    - Ensuring consistent neighbourhood naming conventions; 
    - Removing non-informative fields like IDs, administrative metadata
    
    Data Transformation Decisions:
	- Aggregating raw collision-level data into yearly counts
    - Grouping incidents by neighbourhood boundaries
	- Choosing population-normalized rates over raw counts for spatial comparison
	- Deciding the appropriate temporal range to avoid partial-year bias

    Design Iteration & Testing 
    - Testing different ploting type before picking the optimal one for final visualization 
    - Evaluating color palettes for contrast and accessibility
    - Reducing text to minimize visual clutter

    Techinical & Reproducibility work on Python script testing and documenting data sources and processing steps


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
* Submission Due Date: `23:59 - 02/02/2026`
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
