# Data Visualization

## Assignment 4: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 
    - 1. Python --> Dynamic Bar Chart for Toronto Budgets by Ward **(Year 2010 to Year 2024)**

    > What software did you use to create your data visualization?
    - I used **Python** with Plotly for the data visualizations. The library offered the flexibility needed to manage dynamic data formats and produce insightful visuals for comparing annual budgets across Toronto wards.

    > Who is your intended audience? 
    - The intended audience includes city planners, budget analysts, and municipal stakeholders. The visualizations also target the general public to enhance transparency in budget allocation and changes over time.

    > What information or message are you trying to convey with your visualization? 
    - The visualization provides a **retrospective analysis** of how annual budgets for Toronto wards have evolved from 2010 to 2024. It emphasizes disparities and trends over this period, offering insights into budget allocation patterns and variations across wards.

    > What design principles (substantive, perceptual, aesthetic) did you consider when making your visualization? How did you apply these principles? With what elements of your plots? 
    - Substantive: Ensured data accuracy by cleaning and preparing relevant columns such as Ward/Project Number, Year, and budget values.
    - Perceptual: Used clear, distinct colors and labels for easy comparison between wards, and applied consistent scales and legends for readability. Implemented automatic playback to dynamically illustrate changes over time.
    - Aesthetic: Focused on a clean, uncluttered layout to ensure the visualizations are both functional and visually appealing. 
    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    - Reproducibility was ensured through Python scripts with version control, documenting the data preparation and visualization process and code in a Jupyter notebook with a project overview. **[Project_Documentation_(Python)](viz_by_python.ipynb).** This approach allows others to accurately recreate the visualizations.
    
    - If the tool used to make the data visualization is not reproducible, it could lead to inconsistencies in the results, making it difficult to verify or update the visualizations. This lack of reproducibility would hinder the ability to accurately replicate findings, reducing the reliability and credibility of the visualizations.

    > How did you ensure that your data visualization is accessible?  
    - Accessibility was ensured by using colorblind-friendly palettes and providing alternative text. Clear **labels**, **legends**, **descriptions**, and **changes in bar width** to reflect budget changes make color an auxiliary tool rather than essential for interpreting the visuals. Additionally, **sans-serif** fonts were used for improved readability.

    > Who are the individuals and communities who might be impacted by your visualization?  
    - The visualizations impact city residents, local officials, policy makers, and community groups advocating for equitable funding. These stakeholders can gain insights into budget allocation and its effects across wards.
    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    - Feature selection focused on those relevant to budget changes and ward comparisons, including Ward/Project Number and annual budget columns. Irrelevant columns and those with excessive missing data were excluded to maintain clarity.

    > What ‘underwater labour’ contributed to your final data visualization product?
    - To ensure reproducibility and reduce operational complexity, all processes, _such as the initial Python package installation, data file downloading and handling, formatting, data ETL and cleansing, data analysis, calculations, and final storage for generating the animated bar plot_, can be completed by running a single Jupyter notebook or Python script. All these processes are **100% automated**using Python.

    - 2. PowerBI --> Dynamic Bar Chart for Toronto Budgets by Project Category **(Year 2024 to Year 2033)**

    > What software did you use to create your data visualization?
    - I used Microsoft **PowerBI** Desktop for the data visualization, which provided robust tools for creating interactive and insightful plots.

    > Who is your intended audience? 
    - The intended audience includes city planners, budget analysts, and municipal stakeholders. The visualizations also aim to engage the general public, enhancing transparency and understanding of budget allocation and future projections.

    > What information or message are you trying to convey with your visualization? 
    - Unlike the previous visualization, which focused on historical budget analysis using Python, this visualization will show the projected budget trends for Toronto’s 44 wards over the next 10 years, from 2024 to 2033. It aims to highlight anticipated changes and trends in budget allocation, helping the audience understand **future financial directions** for the city.

    > What design principles (substantive, perceptual, aesthetic) did you consider when making your visualization? How did you apply these principles? With what elements of your plots? 
    - Substantive: Ensured data accuracy by cleaning and preparing relevant columns such as Ward/Project Number, Year, and budget values.
    - Perceptual: Used clear, distinct colors and labels for easy comparison between wards, and applied consistent scales and legends for readability. Implemented automatic playback to dynamically illustrate changes over time.
    - Aesthetic: Focused on a clean, uncluttered layout to ensure the visualizations are both functional and visually appealing. 
    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    - Reproducibility was ensured through a comprehensive Power BI (PBI) file with the plot and its configurations, Python scripts for data processing, and detailed procedural documentation in a single file. **[Project_Documentation_(PowerBI)](assignment_4_powerbi.ipynb)**. This approach allows others to accurately recreate the visualizations.
    
    - If the tool used to make the data visualization is not reproducible, it could lead to inconsistencies in the results, making it difficult to verify or update the visualizations. This lack of reproducibility would hinder the ability to accurately replicate findings, reducing the reliability and credibility of the visualizations.

    > How did you ensure that your data visualization is accessible?  
    - Accessibility was addressed by using color palettes friendly to colorblind users, and providing alternative text for key visual elements. Clear labels, legends, and descriptions were included to make the visualizations understandable to a broad audience.

    > Who are the individuals and communities who might be impacted by your visualization?  
    - The visualizations impact city planners, budget analysts, municipal stakeholders, and the general public. These stakeholders can gain insights into projected budget trends for the next decade, which helps in understanding future financial planning and its implications for different wards.
    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    - Features were selected based on their relevance to projecting future budget trends, focusing on projected budget data and categories pertinent to the next 10 years. 

    > What ‘underwater labour’ contributed to your final data visualization product?
    - The **data preparation** required calculation (aggregation) and was efficiently prepared through automated Python scripts, significantly enhancing accuracy and speed compared to manual methods.

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
* Submission Due Date: `HH:MM AM/PM - DD/MM/YYYY`
* The branch name for your repo should be: `assignment-4`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_4.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-4`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack at `#cohort-3-help`. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
