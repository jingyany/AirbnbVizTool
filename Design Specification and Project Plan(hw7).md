## Part 1: Components
This section should list the components that you expect to have in your project (not necessarily a complete list), what they do, and how their interfaces (e.g., functions with inputs and outputs). If the component is an existing package, then you should point to a documentation for the package. If the component is something that you'll build, then describe (maybe at a high level) the functions and their inputs and outputs.


### Componenet 1: Pricing Prediction
We have two components in our Machine Learning Model part, they are Price Predicting for Airbnb Costumers and Probability of Renting Predicting for Airbnb host. 

For Price Predicting, we will compare the accuracy of using Ridge Regression with gradient descent, Lasso regression with coordinate descent and Elastic Net Regularization, and We will select the better one to use as our price predicting model. 

#### Component Specification:
### Modeling Selecting and Feature Selecting 
Name: MinCoeff_Ridge/ MinCoeff_Lasso/ MinCoeff_Ent

What it does:  

- Fitting the data by sklearn.linear_model.RidgeCV/ LassoCV/ ElasticNetCV , and find the alpha(or l1_ratio) 
- Using the optimal alpha(or l1_ration) for sklearn.linear_model.Ridge/ Lasso/ ElasticNet, and find the optimal coefficients 

Input: 

- Y, price 
- X, Matrix of Variables

Output: 

The Optimal Coefficients by Ridge/Lasso/Elastic-Net regression 



Name: MinCoeff_Univariate/ MinCoeff_Recursive/ MinCoeff_Random

What it does:  

- Fitting the data by Univaruate Selection/ Recyrsuve Feture Elimination/ Randomized Logistic Regression 
- Use the selected variable to fit the logistic model
- Get the optimal Coefficients
 
Input: 

- Y, avaliable, 0 is no, 1 is yes  
- X, Matrix of Variables

Output: 

The Optimal Coefficients by Logistic Regression 


### Price and Probability Predicting 

Name: PricePredicting

What it Does: 

Pridecting price by selecting optimal coefficents from either MinCoeff_Ridgem MinCoeff_Lasso, or MinCoeff_Ent. 

Input: 

Features by your preference( eg. number of bedrooms..)

OutPut:

Price base on your preferences



Name: ProbabilityPredicting

What it Does: 

Pridecting probability of availability  by selecting optimal coefficents from either MinCoeff_Univariate/ MinCoeff_Recursive/ MinCoeff_Random.

Input: 

Features by your preference( eg. number of bedrooms..)

OutPut:

Probability of Availability  base on your input


#### Python Packages:

we will use scikit-learn python package for price predicting

Scikit-learn is a powerful machine learning library for Python. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with Python numerical and scientific libraries NunPy and SciPy. 



### Componenet 2: Text Analysis of Reviews

#### Component Specification:

##### Sub-component1: Sentiment Score of Reviews

name: SentimentOfReviews

what it does: Conduct sentiment analysis on guests' reviews

Input: review, a sentence string

Output: sentiment score, a float

##### Sub-component2: Number of Review per listing

name: CountReviews

what it does: Count the number of reviews per listing

Input: Listing id, an int

Output: count, an int

##### Sub-component3: Length of Review

name: LengthOfReview

what it does: Measure the length of review

Input: review, a sentence string

Output: length, an int

#### Python Packages:

In this component, we will use two python packages, py-corenlp and NLTK.

TextBlob: TextBlob is a Python (2 and 3) library for processing textual data. It provides a consistent API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, and more.

NLTK (Natural Language Toolkit): NLTK is a leading platform for building Python programs to work with human language data.



## Part 2: Interactions
You should have a subsection here for each use case in your functional specification (homework 6). In each subsection, you will describe how the components interact to accomplish the use case.

- Mapping all listings in Seattle area with selected features
- Mapping all neighborhoods in Seattle area showing average listing price of each neighborhood
- Scatter plot of predicted price according to the room type.
- Scatter plot of predicted price according to the neighborhood.
- Scatter plot of predicted price according to the housing amenities.
- Scatter plot of predicted price according to the room type.

#### User cases under component 2 (text analysis of reviews)
- Scatter plot of listing price and the sentiment score.
Use the result, sentiment score, from Sub-component1 and pricing to create a scatter plot. User can visualize the relationship between review and listing's price
- Scatter plot of listing price and the number of reviews per listing.
Use the result, number of reviews per listing, from Sub-component2 and pricing to create a scatter plot. User can visualize the relationship between number of reviews per listing and listing's price
- Scatter plot of sentiment score and the length of the reviews.
Use the result, length of review, from Sub-component3 and pricing to create a scatter plot. User can visualize the relationship betweenlength of review and listing's price
- Scatter plot of sentiment score and the length of the reviews.
Create a scatter plot based on the results from sub-component1 and sun-component3
- histogram of listing price and the length of the reviews.
Create a histigram based on the result from sub-component3

## Part 3: Project plan
Provide details for what you'll accomplish in the next two weeks, and higher level descriptions for the remaining weeks in the quarter so that the end result is that you have implemented and tested a system that accomplishes your use cases.

For the following week, We will implement those functions of text analysis and create visualization based on its results. We will select important features that are relevant to the lising pricing using machine learning model. Those features will be implemented on the user interface we build using bokeh. We will also build up our price prediction model. The predicted data will be input to our final visualization as well. The user interface need to be refined further after we have all predicted data. We will also explore more advanced feature of bokeh to make our final interactive visualization more informative and user-friendly.

In the last week, we will make sure all the codes following pep8 programming style, and add documentation to all the codes. Then, all project documentation on github need to be finalized and well organized. The final project report and presentation slides should be finished too.




## References
"Natural Language Toolkit." Natural Language Toolkit — NLTK 3.0 Documentation. N.p., n.d. Web. 18 May 2017.

"Tutorial: Quickstart¶." Tutorial: Quickstart — TextBlob 0.12.0 Documentation. N.p., n.d. Web. 19 May 2017.

David Cournapeau. "Scikit learn in python" GitHub. N.p., 19 May 2016. Web. 18 May 2017.
