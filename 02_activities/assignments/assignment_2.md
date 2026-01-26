# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      Good: https://datavizproject.com/wp-content/uploads/examples/Sk%C3%A6rmbillede-2016-02-03-kl.-14.15.25.png
      Bad: https://datavizproject.com/wp-content/uploads/examples/Sk%C3%A6rmbillede-2017-09-05-kl.-12.51.11.png

      Good:
      This is very nice and clear visualization. It has great colour contrast (even good for colour-blindness). It is easy to read, clearly labelled, and conveys data clearly and accurately. The stacked bars make it easy to determine whether the cases/mortalities are higher in the developed or developing world. Additionally, adding the actual number to the end of each bar per cancer allows easier interpretation of the data, compared to the readers having to line it up with the axis and guess. This graph represents its intended purpose well (showing the number of cases and mortalities associated with different types of cancers in developed vs developing countries).

      Bad:
      While the graph is straightforward (temperature changes across a time period in a set location), it is quite busy and hard to read. Many data points from Sep onwards are not visible. The Year & Month legends very squished together/overlapping. The colours might be misleading (usually warmer colours like yellow are associated with summer, so having them with the end-of-year colder months is a bit counter-intuitive). The temperature units are not specified (degrees F/C?). I understand they represented it as a 3D graph because of the 3 necessary comparison axes (temp/year/month), and to show monthly changes across a decade, but the easiest thing to interpret from this graph is that the warmer months have higher temps. It takes more work to interpret what’s going on between each year.  

      Sources:
      -course material/slides
      -https://www.dataspire.org/blog/7-essential-components-of-effective-data-visualization

      ```
    - How could this data visualization have been improved?  
      ```
      Good:
      This visualization is pretty good. The improvements I’m going to suggest are more of a personal choice. I would make the grey words/notes a slightly darker shade.  I understand that they wanted to centre the graph, and thus have the list of cancers in the centre, but it seems unbalanced since the “cases” has 10-60 demarcations while the mortality only goes to 20. This is done because there aren’t as many mortalities, but maybe keeping the demarcations from 10-60 on the right (“cases”) side as well would make the graph more visually balanced. I also think they should have added notes about Prostate cases (huge difference between developed and developing), Lymphoma/Nasopharynx cases/mortality (lowest ones), and Lung (around equal number of cases and mortality for both…a way to highlight the more visually interesting data). Finally, they could have described the criteria for developed vs developing countries, but maybe it’s stated in the article it’s published in.

      Bad:
      There are quite a few things I would change. First, the Year and Month labels should be rotated (or made vertical) so that each year and month are clearly readable. The colours would be changed to go from Light Blue in the early winter months, to Warm (red/orange/yellow) in the summer months, to Dark Blue in the later winter months. I would also add the units to the Temperature label. The heading is also slightly misleading. The title suggests there will be 100 years present, although the x-axis only has 10 years. It would be better to change the title to reflect that these are per decade (either averages or the beginning or whatever measurement they were referring to). Finally, I would want to change the hidden bars from Sep onwards. This is tricky, but there are a few ways to approach this: (A) split this into two graphs (Jan to Jun, and Jul to Dec), or (B) make it interactive by making it either rotate (to see the hidden bars) or make individual graphs per year and scroll through the years/graphs-per-year, or (C) make it into a line graph and flatten it into a 2D graph (x-axis = Year, y-axis = Temperature, legend = Months).

      Both are missing data source, but I’ll assume they give it in the article these were published in.

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
* Submission Due Date: `23:59 - 10/26/2025`
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
