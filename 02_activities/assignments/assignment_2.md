# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      GOOD:https://public.tableau.com/app/profile/dillon.brady/viz/HealthShortageinUnitedStatesHPSA/Dashboard1
      NOT-SO-GOOD: https://public.tableau.com/app/profile/robert.orr6104/viz/MappingHealthProfessionalShortageAreas/Sheet1
      
      While both graphs show similar information, the "good" visualization used state-specific colours, which helps viewers easily identify state lines. In comparison, the "not-so-good" visualization uses a monochromatic (red) scale, which makes it difficult to differentiate between states, especially when zoomed out and looking at the entire map. Also, due to a few outliers in the dataset, the redness is largely skewed towards lighter red, which makes it difficult to differentiate between the dots. I am also not clear about what the score being visualized actually is, as it’s not stated on or around the viz. Additionally, the “good" viz includes filters to focus on a specific state or states, as well as sort by HPSA (Health Professional Shortage Area) Score and by average % of population below the poverty line, which allows for some context when browsing through the map. Also, the use of a dichromatic (red and green) scale for both filters reduces cognitive load, as these colours are easy to interpret and widely understood. On the map itself, size of the dot is proportional to the score, which is intuitive and makes it easy to see relative differences between different health centres without focusing too much the actual score.

      
    - How could this data visualization have been improved?  
      ```
      For the “not-so-good” viz, I believe a non-linear (e.g.  logarithmic) colour scaling could have been applied to the dots to allow the audience to see greater resolution at the lower end of the scale, where most of the data appears to be clustered. Also, a dichromatic scale could  help make it more intuitive. Also, unless required by the intended audience, the coordinates of each city (that appear when hovering over a data point) might be a bit too much information for the average viewer. Adding some other data to contextualize the scores might add to the story – e.g. the % of pop below poverty line (as shown in the “good” viz), or some other measure of socioeconomic status. Also, when zooming out to see the entire map, it could be useful to collapse all the individual data points into one weighted average (e.g. based on population) to get a broad perspective of the entire country by state. There is not much that I would change about the “good” viz, other some of the colour choices, which make the map look somewhat busy.
      
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
* Submission Due Date: `23:59 - 06/07/2025`
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

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
