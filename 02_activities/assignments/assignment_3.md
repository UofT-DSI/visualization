# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?
        For the total services available at Toronto Public Library, I used python for the bar graph visual. For interactive map of Toronto showing TPL locations and slicer to filter services, I used Power BI.


    > Who is your intended audience? 
        Bar graph in Python (Bar graph of Total Services): Intended audience is internal stakeholders like strategy team who need a quick summary of services available across all branches of TPL.

        Map in Power BI: Intended audience are TPL administration, city program planners, community stakeholders who need to visualize service availability across different library branches. It can also benefit the public if published as an interactive online report, to help them locate nearby branches offering specific programs.


    > What information or message are you trying to convey with your visualization? 
        Bar graph in Python: This conveys how many branches offer each service and summarizes the coverage of TPL branches that can help identify opportunity of exapansion or reduction.

        Map in Power BI:  It communicates the distribution of library programs and services across TPL branches. By selecting one or more services from the slicer, users can filter out which branches offer those programs. This can help in identifying service clusters and potential geographic gaps in accessibility.


    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
        Bar graph in Python:
             •	Direct labeling: Values printed at the end of each bar for exact counts.
            •	Legibility: Rotations avoided (horizontal labels), adequate padding, and clear title/axes labels.
            •	Appearance: Neutral bar color and avoided unnecessary gridlines or effects.
     
        Map in Power BI:
            •	Clarity and simplicity: The map uses a light background (Road white Canvas) to make branch points visible.
            •	Interactivity: A multi-select slicer lets users filter branches by service type.
            •	Hierarchical cues: Tooltips display branch name, address, postal code, and contact information when hovering over a marker, reducing on-screen clutter.
            •	Consistency: Branches are shown as uniform points rather to emphasize equality across services.
            •	Accessibility & color: High-contrast color palettes were chosen to ensure visibility for color-blind users.
            •	Text over color reliance: The slicer and tooltips rely on text labels rather than hue differences to communicate meaning.


    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
         Bar graph in Python: 
         Reproducibility is mainted through	the code that recomputes totals from the CSV using a consistent set of data cleaning, no manual working therefore the same inputs produce the same chart. If the process weren’t reproducible, decision-makers could question accuracy and the chart would be hard to refresh as data changes.


         Map in Power BI:
         Reproducibility is maintained through using a .pbix file that contains both the dataset link and all transformation steps in Power Query, clearly labelled fields and calculated so the process can be repeated with an updated dataset and maintained a consistent source file path that can be refreshed. If reproducibility were lost (e.g., manual edits without queries), it would reduce transparency for future users who wouldn’t know how filters were generated or which preprocessing rules were applied.


    
    > How did you ensure that your data visualization is accessible?  
        Bar graph in Python: To ensure that visualization is accessible, text labels on bars (counts) provide a non-color cue, horizontal layout supports long service names and screen zoom and high-contrast default text and sufficient font sizes are used.


         Map in Power BI: Following steps ensured that visualization is accessible: high-contrast colors and readable font sizes for branch markers and labels, interactive filters allow keyboard and mouse navigation without relying solely on visual distinction, and users can zoom or resize visuals freely in Power BI service for readability.


    > Who are the individuals and communities who might be impacted by your visualization?  
         Bar graph in Python: 
         Program managers and patrons who may decide based on these counts for expanding services.

         Map in Power BI: 
         •	Library patrons seeking access to specialized programs.
         •	Program planners deciding resource allocations based on service distribution.
         •	Community advocates analyzing neighborhood access gaps.



    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
         Bar graph in Python: Included service columns from the dataset and excluded Public Parking column as it is an amenity not a program. 

         Map in Power BI: Included branch names, addresses, contact info, and program availability fields (e.g., KidsStop, Youth Hub, etc.) so that the users can timely identify which branch has their desired program and its details. Excluded PublicParking, SquareFootage, and WardNumber because they do not directly support the visualization’s purpose and would clutter the map.



    > What ‘underwater labour’ contributed to your final data visualization product?
         Bar graph in Python: 
            •	Cleaned data by handling blanks.
            •	Verified that column headers match services.
            •	Included labels and tweaked layout for improved readability.
            •	Cross-checked totals against a quick tabulation.

         Map in Power BI:
            •	Used Power Query to unpivot service columns into a single  categorical field to create dynamic slicers.
            •	Verified that each slicer selection updated the map correctly.
            •	Adjusted map scaling, tooltip format, and slicer orientation for clarity and accessibility.
            •	Checked coordinates and removed rows with missing lat/long values.


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
