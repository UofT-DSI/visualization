# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 

    Visualization No 1

    > What software did you use to create your data visualization?
    Python

    > Who is your intended audience? 
    The primary audience includes city planners, housing policy analysts, and community advocates. The chart is designed to communicate occupancy trends clearly and quantitatively, supporting discussions around service capacity and homelessness intervention strategies.

    > What information or message are you trying to convey with your visualization? 
    This line chart visualizes how average monthly occupancy rates change across different shelter sectors throughout 2025. The goal is to show which sectors operate near capacity and whether usage fluctuates seasonally. It highlights that nearly all sectors sustain occupancy rates above 90%, indicating persistent strain on Toronto's shelter system. The Family sector shows lower values due to incomplete reporting, an important contextual insight.

    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    This visualization follows the three essential qualities of good design: aesthetic, substantive, and perceptual integrity.

    Aesthetic:
    The plot uses a clean white grid, high-contrast colourblind-safe palette, and consistent line thickness. Labels are clear, and the y-axis range (60–100%) focuses on meaningful variation.  

    Substantive: 
    The plot accurately represents aggregated monthly averages without exaggeration or unnecessary smoothing. Missing values were handled transparently to maintain honesty in data representation.  

    Perceptual:
    The design leverages Gestalt principles of proximity and continuity, guiding the eye along each sector's trajectory. Cognitive load is minimized by limiting gridlines, providing a clear legend, and using consistent units.  

    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    All steps from data import to visualization are fully documented in the accompanying Python notebook. Because the workflow is code-based, it can be re-run on updated data from the City of Toronto Open Data Portal at any time. This supports open science and reproducible public policy research.

    > How did you ensure that your data visualization is accessible?  
    Colourblind-friendly palettes were applied. Axis labels use descriptive text and readable font sizes. The figure includes an informative title, caption, and alt-text for web publication. These choices follow accessible data design principles discussed by Fossheim (2020), ensuring readability for diverse audiences.

    > Who are the individuals and communities who might be impacted by your visualization?  
    This visualization represents data about individuals and families experiencing homelessness. It is therefore critical to treat the information ethically, as evidence of systemic housing issues rather than mere statistics. Audiences include service providers, policymakers, and advocates seeking equitable access to shelter services.

    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    The dataset was filtered to remove records with missing or zero occupancy values, and the analysis was aggregated by month and sector. This reduces noise while preserving core structure. Family-sector data were retained despite gaps to maintain representational completeness.

    > What ‘underwater labour’ contributed to your final data visualization product?
    This visualization builds on extensive 'underwater labour': data collection and entry by city shelter staff, open-data publication by municipal IT teams, and subsequent cleaning and processing within Python. Documenting these processes acknowledges that effective visualization relies on collective, often invisible, labour (D'Ignazio & Klein, 2020).


    Visualization No 2

    > What software did you use to create your data visualization?
    Microsoft Excel

    > Who is your intended audience? 
    The intended audience includes shelter administrators and public-sector managers who require a quick comparative overview of occupancy rates across service sectors and months.

    > What information or message are you trying to convey with your visualization? 
    This chart provides a categorical comparison rather than a time series. Each group of columns represents a sector (Families, Men, Mixed Adult, Women, Youth), and each coloured bar within that group represents a month. It shows that Women's shelters consistently maintain the highest occupancy (98–99%), followed by Men's and Mixed Adult sectors. Youth shelters operate slightly lower (92–95%), while Family shelters show missing or underreported months. The visualization communicates that service demand is persistently high across all sectors.

    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    Aesthetic: 
    The chart uses Excel's clustered column type to maintain a clean, side-by-side comparison. Gridlines were minimized, titles and axis labels added, and a colourblind-safe palette applied.  
    
    Substantive: 
    Data values were rounded to one decimal for clarity without misrepresenting percentages. The y-axis was limited to 60–100% to focus on meaningful differences.  
    
    Perceptual: 
    The clustered format supports intuitive comparison across sectors. Viewers can immediately see relative performance without decoding stacked bars or multiple scales.

    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    While Excel is not inherently reproducible like Python, reproducibility is maintained by documenting transformation steps and reusing the same cleaned dataset. Anyone with the file can regenerate the PivotTable following the described structure.

    > How did you ensure that your data visualization is accessible?  
    High-contrast colours, axis titles, and descriptive figure captions were used. The chart title includes the year for context, and the y-axis label ('Occupancy Rate (%)') uses direct language for non-experts. Gridlines and legend placement were optimized for screen readers and visual clarity.

    > Who are the individuals and communities who might be impacted by your visualization?  
    Like the Python visualization, this figure represents data about vulnerable populations. Care was taken not to sensationalize or oversimplify the human realities behind the statistics. By focusing on systemic patterns rather than individual outcomes, the visualization contributes to informed and ethical advocacy.

    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    Like the Python visualization, this figure represents data about vulnerable populations. Care was taken not to sensationalize or oversimplify the human realities behind the statistics. By focusing on systemic patterns rather than individual outcomes, the visualization contributes to informed and ethical advocacy.

    > What ‘underwater labour’ contributed to your final data visualization product?
    The creation of this chart relied on municipal data management, the cleaning process done in Python, and the visual design work completed in Excel. This iterative labour chain reflects the collaborative nature of civic data storytelling.

The charts reveal a clear message: Toronto's shelters consistently operate near or at capacity, with little seasonal relief. By combining quantitative precision with accessible design, the project exemplifies how visualization can act as both analysis and advocacy, translating public data into insight and empathy.

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
