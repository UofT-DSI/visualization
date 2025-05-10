**What software did you use to create your data visualization?**
> Python

**Who is your intended audience?**
> General public

**What information or message are you trying to convey with your visualization?**
> Using data from the City of Toronto’s Open Data Portal (https://open.toronto.ca/dataset/reducing-single-use-and-takeaway-items/), I wanted to investigate opinions on reducing single use and takeaway items. While this dataset contained responses to a number of questions, I chose to focus on the response to the reduction/restriction of single-use hot to-go cups as an intervention to minimize waste. Opinions on the scale of strongly opposed to strongly supported were plotted as a stacked bar graph for each sector, which revealed that although there was strong support overall to such restriction interventions, manufacturers of single-use items had the greatest proportion of responders that were strongly opposed, reflecting their financial interests in maintaining consumer demand for single-use items.

**What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?**
> I tried to make the viz as accessible as possible, using vivid high contrast colours for each stack of the bar graph to distinguish between opinions lying on a spectrum. I chose red and blue as the colours on the extremes as it evokes a feeling of opposition (hot-cold, political parties, etc), while maintaining accessibility for people with specific types of colourblindness. I also chose to manipulate the data from raw counts into a proportion out of 100%, so that it would be easier to compare across groups (sectors) with data normalized to the same scale given the differences in group sizes. 
    
**How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?** 
> Ensured reproducibility by writing a Python script on a Jupyter notebook which shows step-by-step how to reproduce the viz from the input data.
    
**How did you ensure that your data visualization is accessible?**
> By making data file (.csv) available with the Jupyter notebook.

**Who are the individuals and communities who might be impacted by your visualization?**
> The municipal government of Toronto may look at this visualization and come to the conclusion that majority (80+%) of respondees within the city (except for manufacturers) would support legislation to reduce single-use container usage, specifically single-use cups for hot beverages.

**How did you choose which features of your chosen dataset to include or exclude from your visualization?** 
> This dataset contained responses for various opinions towards multiple types of single-use items including cups for hot drinks, cups for cold drinks, plastic containers by colour, plastic bags, etc. I chose to focus on responses to the question regarding restrictions on usage as I felt this question would lead to the most concrete outcomes taken by the government, which would prompt people to answer more honestly rather than giving an answer influenced by virtue signalling. I also chose to focus on cups for hot drinks as it was the item that had the most complete responses. I also chose to exclude responders that identified with more than one category to reduce noise, and collapsed several categories together that I felt were related ("health organization"+"environmental organization", and "retail"+"restaurant").
    
**What ‘underwater labour’ contributed to your final data visualization product?**
> The people from Toronto's Solid Waste Management Services who designed, conducted, and collated data from this public survey, and myself in pre-processing the data (evident from the huge chunk of code just dedicated to cleaning up the (already truncated!) imported dataset).