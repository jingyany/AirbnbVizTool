## Part 1: Components
This section should list the components that you expect to have in your project (not necessarily a complete list), what they do, and how their interfaces (e.g., functions with inputs and outputs). If the component is an existing package, then you should point to a documentation for the package. If the component is something that you'll build, then describe (maybe at a high level) the functions and their inputs and outputs.


### Componenet 1: Pricing Prediction
We have two components in our Machine Learning Model part, they are Price Predicting for Airbnb Costumers and Probability of Renting Predicting for Airbnb host. 

For Price Predicting, we will compare the accuracy of using Ridge Regression with gradient descent, Lasso regression with coordinate descent and Elastic Net Regularization, and We will select the better one to use as our price predicting model. 

#### Ridge Regression: 

Advantage:  was the most popular technique for improving prediction accuracy. Ridge regression improves prediction error by shrinking large regression coefficients in order to reduce overfitting. Ridge Regression are good at prediction accuracy. 

Disadvantage: Ridge cannot zero coefficients. Thus, it does not perform covariate selection and therefore does not help to make the model more interpretable.

#### Lasso Regression: 

Advantage: Lasso is able to achieve both prediction accuracy and covariate selection by forcing the sum of the absolute value of the regression coefficients to be less than a fixed value, which forces certain coefficients to be set to zero, effectively choosing a simpler model that does not include those coefficients which makes mode more interpretable. 

Disadvantage:  It may ignore some covariates which are highly correlated. Lasso can not do group selection. If there is a group of variables among which the pairwise correlations are very high, then the LASSO tends to arbitrarily select only one variable from the group. 

#### Elastic-Net Regularization:

Advantage: I t is hybrid of lasso and ridge regression.  It is trained with L1 and L2 prior regularize. The advantage of trading off between Lasso and Ridge is, it allows Elastic-Net to inherit some of Ridge’s stability under rotation. It solve the drawback of Lasso and Ridge, while including each as special cases. 

Disadvantage: For Elastic Net, two parameters should be tuned/selected on training and validation data set. For LASSO, these is only one tuning parameter. Although Elastic Net is proposed with the regression model, it can also be extending to classification problems (such as gene selection). 

### Componenet 2: Natural Language Processing

name: SentimentOfReviews
what it does: Conduct sentiment analysis on previous guests' reviews
Input: review, a sentence string
Output: score, a float

In this component, we will use two python packages, py-corenlp and NLTK.

py-corenlp: Python wrapper for Stanford CoreNLP. This simply wraps the API from the server included with CoreNLP 3.6.0

NLTK (Natural Language Toolkit): NLTK is a leading platform for building Python programs to work with human language data

#### Component Specification:



## Part 2: Interactions
You should have a subsection here for each use case in your functional specification (homework 6). In each subsection, you will describe how the components interact to accomplish the use case.






## Part 3: Project plan
Provide details for what you'll accomplish in the next two weeks, and higher level descriptions for the remaining weeks in the quarter so that the end result is that you have implemented and tested a system that accomplishes your use cases.


## References
"Natural Language Toolkit." Natural Language Toolkit — NLTK 3.0 Documentation. N.p., n.d. Web. 18 May 2017.

Smilli. "Smilli/py-corenlp." GitHub. N.p., 19 May 2016. Web. 18 May 2017.

