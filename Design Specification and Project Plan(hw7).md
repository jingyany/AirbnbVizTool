## Part 1: Components
This section should list the components that you expect to have in your project (not necessarily a complete list), what they do, and how their interfaces (e.g., functions with inputs and outputs). If the component is an existing package, then you should point to a documentation for the package. If the component is something that you'll build, then describe (maybe at a high level) the functions and their inputs and outputs.


### Componenet 1: Pricing Prediction
We have two components in our Machine Learning Model part, they are Price Predicting for Airbnb Costumers and Probability of Renting Predicting for Airbnb host. 

For Price Predicting, we will compare the accuracy of using Ridge Regression with gradient descent, Lasso regression with coordinate descent and Elastic Net Regularization, and We will select the better one to use as our price predicting model. 

#### Component Specification:
### Ridge Regression 
Name: MinCoeff_Ridge

What it does:  

- Fitting the data by sklearn.linear_model.RidgeCV , and find the alpha 
- Using the optimal alpha for sklearn.linear_model.Ridge, and find the optimal coefficients 

Input: 

- Y, price 
- X, Matrix of Variables

Output: 

The Optimal Coefficients by Ridge regression 

### Lasso 
Name: MinCoeff_Lasso

What it does:  

- Fitting the data by sklearn.linear_model.lassoCV , and find the optimal alpha 
- Using the optimal alpha for sklearn.linear_model.lasso, and find the optimal coefficients 

Input:

- Y, price 
- X, Matrix of Variables

Output: 

The Optimal Coefficients by Lasso 

### Elastic-Net 

Name: MinCoeff_Ent

What it does:  

- Fitting the data by sklearn.linear_model.ElasticNetCV , and find the optimal alpha and l1_ration 
- Using the optimal alpha and l1_ration for sklearn.linear_ElasticNetCV , and find the optimal Coefficients for price predicting model 

Input :

- Y, price 
- X, Matrix of Variables

Output : 

The Optimal Coefficients by Elastic-Net

### Price Predicting 

Name: PricePredicting

What it Does: 

Pridecting price by selecting optimal coefficents from either MinCoeff_Ridgem MinCoeff_Lasso, or MinCoeff_Ent. 

Input: 

Features by your preference( eg. number of bedrooms..)

OutPut:

Price base on your preferences


#### Python Packages:

we will use scikit-learn python package for price predicting

Scikit-learn is a powerful machine learning library for Python. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with Python numerical and scientific libraries NunPy and SciPy. 


### Componenet 3: Natural Language Processing

#### Component Specification:

name: SentimentOfReviews

what it does: Conduct sentiment analysis on previous guests' reviews

Input: review, a sentence string

Output: score, a float

#### Python Packages:

In this component, we will use two python packages, py-corenlp and NLTK.

py-corenlp: Python wrapper for Stanford CoreNLP. This simply wraps the API from the server included with CoreNLP 3.6.0. Stanford CoreNLP provides a set of natural language analysis tools. It can give the base forms of words, their parts of speech, whether they are names of companies, people, etc., normalize dates, times, and numeric quantities, mark up the structure of sentences in terms of phrases and word dependencies, indicate which noun phrases refer to the same entities, indicate sentiment, extract particular or open-class relations between entity mentions, get quotes people said, etc.

NLTK (Natural Language Toolkit): NLTK is a leading platform for building Python programs to work with human language data.





## Part 2: Interactions
You should have a subsection here for each use case in your functional specification (homework 6). In each subsection, you will describe how the components interact to accomplish the use case.






## Part 3: Project plan
Provide details for what you'll accomplish in the next two weeks, and higher level descriptions for the remaining weeks in the quarter so that the end result is that you have implemented and tested a system that accomplishes your use cases.

For the following week, we will select important features that are relevant to the lising pricing using machine learning model. Those features will be implemented on the user interface we build using bokeh. We will also build up our price prediction model. The predicted data will be input to our final visualization as well. The user interface need to be refined further after we have all predicted data. We will also explore more advanced feature of bokeh to make our final interactive visualization more informative and user-friendly.

In the last week, we will make sure all the codes following pep8 programming style, and add documentation to all the codes. Then, all project documentation on github need to be finalized and well organized. The final project report and presentation slides should be finished too.




## References
"Natural Language Toolkit." Natural Language Toolkit — NLTK 3.0 Documentation. N.p., n.d. Web. 18 May 2017.

Smilli. "Smilli/py-corenlp." GitHub. N.p., 19 May 2016. Web. 18 May 2017.

"Stanford CoreNLP – Core Natural Language Software." Stanford CoreNLP. N.p., n.d. Web. 18 May 2017.
