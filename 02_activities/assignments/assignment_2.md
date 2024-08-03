# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
Your answer...
Visualization 1: https://public.tableau.com/app/profile/grow.with.google/viz/WorldHappiness_16003108197090/12_YearlyHappinessScoreChanges
- Overall good. Presents information well at a glance.
- Heat Map allows understanding of information at a quick glance and suggests patterns based on location of the country correlating with happiness.
- Happiness Difference is Clear and Ranked from highest to lowest change is easy to read, decipher, compare.

Visualization 2: https://public.tableau.com/app/profile/pradeepkumar.g/viz/SampleSuperstore-SalesPerformance/viz_
- Overall the visualization is appealing, has good information but focuses on the highlighting less relevant metrics.
- Specifically this is a great showcase of creator expertise, but I believe very poor to use in an actual business setting.
- Export to PDF is good function for Field Ops, but informaton is not targeted to Field Ops as interaction with Tooltips is required to give accurate information
- A lot of metrics don't explain what is happening... Ex. is this number YTD, what is this % based against?
- Title format is appealing but is actually distracting because the report lacks structure and direction + at a glance it looks like something.







      ```
    - How could this data visualization have been improved?  
      ```
  Your answer...

Visualization 1: https://public.tableau.com/app/profile/grow.with.google/viz/WorldHappiness_16003108197090/12_YearlyHappinessScoreChanges
- I would lock the map given data is only available for Europe
- I would default the year on the Happiness Map to 2017, given the Score change is calculating difference between 2015 and 2017
- Happiness Score Change would benefit from Data Labels for legibility, colour gradiant would make it look more appealing.
- Country Flags on the X axis data markers would help visibility.

Visualization 2: https://public.tableau.com/app/profile/pradeepkumar.g/viz/SampleSuperstore-SalesPerformance/viz_
- Let the user select year by year, but not select all of them together. 
  - This causes a major break in the scope consistency across the report. 
  - Then all the benchmarks are vs. Last Year to Date and completely solves this problem.
  - In my experience, there is rarely a need to bunch multiple years together unless it's a rolling timeframe which is not possible here anyway.
- In the Sales by State map, I would choose color only, having size bubble too makes it seem like there are 2 different metrics calculated and there isn't. There are also too many states to make reasonable comparisons on any other metric across 50 states using a size bubble unless you're catching major outliers.
- If this wasn't a portfolio showcase and actually a business report, I would only use one type of graph to display the same thing (choosing the simplist and non-flashy option), else it's harder to read than necessary. 
    - Sales by subcategory by month is actually near unreadable because tracking by colour depth obscures accuracy.
- I would add an option to flip all datasets to tables to get numbers easier if the user wanted to. Will show more data than top $ weights and allow for searching opportunites outside of top categories/states. 
- If 1st Manufacturer is "Other", better data quality is required but most likely wouldn't be the data visualizer's problem.


Citation: 
Google Career Certificates. (n.d.). World Happiness. Public.tableau.com. https://public.tableau.com/app/profile/grow.with.google/viz/WorldHappiness_16003108197090/12_YearlyHappinessScoreChanges 

Kumar G, P. (n.d.). Sample Superstore - Sales Performance | VOTD. Public.tableau.com. https://public.tableau.com/app/profile/pradeepkumar.g/viz/SampleSuperstore-SalesPerformance/viz_ 

      
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
