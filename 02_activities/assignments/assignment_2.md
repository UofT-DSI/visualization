# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
    Good one: https://public.tableau.com/app/profile/chimdi.nwosu/viz/MakeoverMondayWk43-TheMostReliableCarBrandsintheUS/Dashboard1

    This visualization was classified as good because it adheres to several principles of effective data visualization, as outlined by experts like Edward Tufte and Stephen Few.

    1. Clarity:

    - The visualization organizes data into distinct sections by country and brand, using headings, color coding, and a hierarchical layout. This aligns with Few's recommendation to simplify data displays and prioritize readability.
    - The bubble chart visually encodes data effectively, showing problems per 100 vehicles (PP100) along the x-axis, with larger bubbles for higher problem counts. 
  
    2. Accessibility:

    The use of color to distinguish performance categories (e.g., "Above Average," "Average," "Below Average") is intuitive and aligns with Tufte’s principle of making visual distinctions clear without unnecessary embellishments.
    
    3. Contextual Information:

    - Summary metrics (e.g., PP100 by country) and distance-from-average charts provide both high-level and granular views of the data, aiding in comprehension and context.
    - Legends and labels are provided for all visual elements.
  
   4. Design and Engagement:

   - The layout is visually appealing, with consistent use of colors and formatting. 
  
   Scholarly References
   - Edward Tufte’s "The Visual Display of Quantitative Information" emphasizes clarity and avoiding "chartjunk".
   - Stephen Few's "Information Dashboard Design" highlights the importance of simplicity, clear context, and actionable insights in data displays.
  
    Bad one: https://www.pinterest.com/pin/47639708534134635/

    Reason:
    1. Misleading Representation:

    - The use of 3D distorts the relative size of the pie slices, making it difficult to accurately compare proportions. This directly contradicts Few’s guideline that visualizations should "not distort what the data have to say."
    - Proportions are further skewed because slices in the foreground appear larger than those in the background, which is a known issue with 3D pie charts.

    2. Clutter and Overcomplication:

    The use of patterns (dots, lines, solid fills) instead of simple colors adds unnecessary complexity, violating Tufte’s principle of reducing "non-data ink."

    3. Lack of Context:

    - Percentages or proportions for each slice are missing from the chart. 
    - No explanation of the time frame or source of the data is provided, further limiting the visualization's utility.

    4. Accessibility Issues:

    The small size of text and overlapping slices make the chart difficult to read.
      ```
    - How could this data visualization have been improved?  
      ```
    Improvement measures of the good one:
    1. Proportional Scaling of Bubble Sizes:

    Currently, the bubbles for brands may not be proportional to the number of problems per 100 vehicles (PP100). Ensuring bubble size accurately represents data would improve interpretability.
    
    2. Gridlines for Easier Comparison:

    Adding light vertical gridlines in the bubble chart would help viewers compare brand positions more precisely along the x-axis.

    3. Interactive Features:

    If published online, hover-over tooltips could display additional information about each brand, such as specific PP100 values, or details about what contributes to their ranking.

    4. Color Accessibility:

    Ensure that the color palette is optimized for color-blind users by using patterns or alternative shades with distinct luminance levels.

    Improvement measures of the bad one:
    1. Replace 3D with 2D:

    A simple 2D pie chart would eliminate the distortion caused by perspective, ensuring accurate representation of proportions.

    2. Consider an Alternative Chart Type:

    Pie charts are not ideal for comparing multiple categories, especially with small differences. A bar chart or stacked bar chart would better represent the data and allow for easier comparison.
    
    3. Add Numeric Labels:

    Clearly label each segment with exact percentages or values to help viewers understand the distribution of traffic sources.

   4.Improve Visual Encoding:

   Replace patterns (dots, lines) with solid colors. Use a clean, color-blind-friendly palette to distinguish between categories.

      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `HH:MM AM/PM - DD/MM/YYYY`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack at `#cohort-3-help`. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
