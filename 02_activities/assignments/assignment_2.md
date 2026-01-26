# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.

    - How could this data visualization have been improved?  

The Good Example: https://www.economist.com/graphic-detail/2015/05/12/seeking-safety?fsrc=scn%2Ftw%2Fte%2Fbl%2Fed%2Fseeking_safety&%3Ffsrc%3Dscn%2F=tw%2Fdc

This visualization is an alluvial diagram showing flows of asylum seekers showing origin country, destination country, and decision. It was published by the Economist magazine on May 12, 2015. This is a good graphic because it (1) chooses the type of diagram deliberately, (2) is easy to interpret, (3) provides factual account in a relatively neutral way.

First, the choice alluvial diagram is very accurate. This type of diagram is good for expressing flows, especially when the origin and end points are relatively few. As a result, asylum seekers are a natural use case.  The authors include three pieces of information: the origin country, the destination country, the decision (accept/reject), and then again the origin country. Furthermore, the authors show the relationships between these three dimensions. This allows the reader to see a whole story: how many asylum seekers from country A go to country B. Of those in B how many are accepted/rejected. Of those accepted/rejected how many came from each country. This is a very concise way of presenting a lot of information. Consider instead a bar chart that tries to show the three dimensions. It would be hard to read and would also lose the relational aspect. As such, it would only tell one part of the picture.

Second, despite the information density of this diagram, it is actually easy to interpret. For example, the use of color and the ordering of flows from largest to smallest make it easy to grasp the main ideas quickly. For example, it is very easy to see that in 2014 Syria and Serbia were the largest origin countries of asylum seekers, most of whom went to Germany. A large share of Syrians were subsequently accepted, while most Serbians were rejected. A second read reveals more information: other origin/destination countries, specific numbers behind the flows, and a comparison between 2012 and 2014.

Lastly, this diagram tackles a highly politicised and polarising debate in Europe. The diagram does a good job of presenting the full picture in a way that is as non-partisan as possible. For example, it does not take a stance of whether the asylum seekers ought to be accepted or not. It also provides more comprehensive picture. Where much of the debate at the time was about the arival of Syrian refugees, it takes a broader perspective: many countries of origin, many destinations, showing both rejections and acceptances. 

In sum, the Economist magazine does an excellent job of presenting key facts about an important and politically charged topic in a way that is logical, easy to understand, while remaining as neutral as possible. 


The Bad Example: https://www.infocaptor.com/sending-and-receiving-money-across-the-world-remittances-between-countries
The specific graphic: https://www.infocaptor.com/wp-content/uploads/2014/10/image-371.jpg


This visualization is a chord diagram showing remittances by sending and receiving country. It is published on the blog of a dashboard software provider, infocaptor. This graphic is not very good because it is hard to interpret and is missing key information. It can be improved with different choice of diagram, more labeling, and clever use of colours.

The first issue is that this graphic is hard to read. For example, it is not immediately clear which countries are sending money, and which are receiving. Based on prior knowledge I can guess that the US is a sending country, but a graphic should not rely the readers' prior knowledge on the topic. Also, it is not clear why some countries are in orange and others are in blue. There are no labels with the magnitudes of these remittances. Only the title makes some vague reference to a number: 'Remittances greater than 5 billion USD'. Is that by sending country? By receiving country? Is that 5.5 billion or 55 billion? 

The second issue is that the diagram does not capture key information on the topic of remittances. For instance, there is no indication of how important the remittances are to the receiving country. All the receiving countries (e.g. Philippines, Mexico, China) have the same sliver of a line. In reality, these remittances are an important part of the Philippian economy but a small part of the Chinese economy. This is a dimension that is not at all captured. Equally, it is useful to know if remittances are a significant part of the source country's output. Based on the graph, it looks like immigrants in the US are sending over huge sums of money. But given that the US is the world's largest economy, that sum may be (and is) a relatively small fraction of output. These two questions have large political implications for both the sending and receiving countries.

This visualization can be improved by using a different type of diagram, better labeling, and better use of colours. Given that this diagram is again about flows (of money), I would recommend an alluvial diagram. This diagram would allow capturing the size of remittances for both the sending country and receiving country. Furthermore, I would consider presenting the figure in terms of percent of GDP (for the sending and receiving countries, respectively) and including a label for the absolute value of the remittances. This type of diagram would also allow for labelling the sending and receiving party clearly. This is especially important as some countries are both senders and receivers. Next, I would use one set of colors for sender (e.g. shades of orange, darker for larger flows) and another for receivers (e.g. blue). Additional labels can also indicate the size of the relevant ethnic community (e.g. number of people of given descent), which gives a better sense of scale than just dollar values. 

These changes would be a significant improvement in terms of interpretability and completeness of the information. 






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
* Submission Due Date: `23:59 - 01/26/2026`
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
