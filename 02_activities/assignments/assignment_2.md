# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
    1. Bad visualization 
     
As an example of a bad visualization, I have chosen a diagram illustrating money remittances between countries that exceed USD 1 billion (InfoCaptor, n.d.). This type of graph is called the chord diagram; it looks like a circle with pairs of data points connected by arcs (DataVizProject, n.d.). Although it is somewhat appealing visually, here are a few reasons why I think this type of graph is not very effective at conveying useful information. 
- It is quite hard to understand what is on the graph without at least some level of understanding of these types of graphs. This type of graph is rarely used, and as discussed in class, rare graph types can increase viewers’ cognitive load. 
- Next, we discussed that “What data is the user seeing?” is a key question. On this graph, some information is easier to understand than some other information. For example, it is clear that the USA amounts to a major share of the graph, but understanding how the designers visualize the connections between countries (the choice of marks, channels and encoding) is not always easy, especially with thinner lines.  
- As discussed in Gerend (2023), this type of graph only represents pairwise relationships, which may be limiting. In this case, it may be interesting to see clusters of countries (e.g. with most connections between them) rather than pairwise relationships. 
- This type of graph is probably not optimal for large datasets. it seems that by using a threshold of USD1 billion, the designers attempted to fit as many countries are possible into the graph, which leads to a cognitive overload. 
- Finally, the choice of colours is suboptimal. As discussed in class, the choice of colour can help provide visual popout, but in this case there are too many colours on the graph, and some colours are duplicated.
How could this visualization be improved? Although it may be challenging to present these specific data coherently on one graph, Miles (2019) suggests a solution. Without significantly altering the presentation, it is possible to essentially create multiple "mini-graphs" instead of one big graph. This may entail:
- Creating nodes that show multiple links between countries;
- Combining the nodes into groups with different sizes and colour-coding, and; 
- Prioritizing more significant connections, for example by using more prominent colours of lines (Miles, 2019).

DataVizProject. (n.d.). Chord Diagram. https://datavizproject.com/data-type/chord-diagram 

Gerend, N. (2023). Introducing the Multi-Chord Diagram: Visualizing Complex Set Relationships. https://towardsdatascience.com/introducing-the-multi-chord-diagram-visualizing-complex-set-relationships-c6fe6cc1cb8b 

InfoCaptor. (n.d.). Sending and receiving money across the world – remittances between countries.  https://www.infocaptor.com/sending-and-receiving-money-across-the-world-remittances-between-countries 

Miles, C. (2019). Bring chord diagrams to life with graph visualization. https://cambridge-intelligence.com/bringing-chord-diagrams-to-life-with-keylines

  2. Good visualization 

As a good example, I have chosen a diagram showing typical March snowfall volumes in three American cities to illustrate the abnormality of record March 2015 snowfalls in each of them (Enten, 2015). The visualization is a scatterplot that shows years of observation on the x-axis and inches of snowfall on the y-axis. The graph is both elegant and visually appealing, and informative as it is easy to see the information that it is trying to convey without a cognitive overload. 
-	A scatterplot is a type of graph that is used often and is relatively easy to understand compared to the previous example. 
-	The visualization has a rectangular shape which helps improve the readability and appeal of the graph. 
-	Answering the question “What data is the user seeing?”, the title clearly suggests that each dot is a separate snowfall event. 
-	Next, the graph is clearly separated into 3 sections, one for each city. Thus, the use of both vertical and horizontal space makes it possible to compare the cities directly on one graph, and do so in a meaningful way. And that in spite of a large number of observations visualized on the graph. 
-	Only one colour is used, and only shading (from dark to light blue) is used to convey different values. 
-	Transparency enables the viewer to see where the dots (marks) overlap. 
-	A dotted trend line with a number (in inches, in bold font) shows where the current snowfall is compared to the March norm. 
I think this graph is almost perfect. It would be hard to suggest improvements, but if I had to do that, I would suggest two possible changes: 
-	Improving the choice of marks, channels and encoding, e.g. by emphasizing outliers such as record snowfalls in a different colour to provide visual popup. This needs to be done carefully; as discussed in class, too many colours could distract the viewers and create clutter. 
-	Adding a simple legend to explain why the graph uses different shades of blue. 

Enten, H. (2015). New York And Philadelphia Are In The Middle Of Historically Snowy Months. https://fivethirtyeight.com/features/new-york-and-philadelphia-are-in-the-middle-of-historically-snowy-months/ 

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
* Submission Due Date: `23:59 - 30/04/2025`
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
