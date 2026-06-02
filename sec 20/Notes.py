'''statistics in ai ml 

it is a field to collect ,organise ,analyse and interpret data to make informed decisions and predictions in the context of artificial intelligence and machine learning.
statistics is crucial in ai ml for several reasons:
1. Data Analysis: Statistics helps in understanding and summarizing data, identifying patterns, 
    and making sense of large datasets. It provides tools for descriptive statistics, such as mean, median, mode, 
    and standard deviation, which are essential for data exploration.

2. Model Evaluation: Statistics is used to evaluate the performance of machine learning models. 
    Metrics such as accuracy, precision, recall, and F1 score are derived from statistical principles 
    and help in assessing how well a model is performing on a given dataset.

3. Hypothesis Testing: In ai ml, hypothesis testing is used to determine if there is a significant 
    difference between groups or if a particular feature has a significant impact on the target variable. 
    This helps in feature selection and model improvement.

4. Probability Theory: Statistics provides the foundation for probability theory, which is
 essential for understanding uncertainty and making predictions in ai ml. Concepts like Bayes'
 theorem,probability distributions, and confidence intervals are crucial for building robust models.

5. Data Preprocessing: Statistics is used in data preprocessing steps such as handling missing values,outliers, 
    and scaling features. These steps are important for improving the quality of the data and the performance 
    of machine learning models.
    
Overall, statistics is an integral part of ai ml as it enables practitioners to make informed decisions,build accurate models, and derive meaningful insights from data.    



Types of stats : 
1. Descriptive Statistics: This type of statistics focuses on summarizing and describing the main features of a dataset. 
    It includes measures such as mean, median, mode, standard deviation, and range. Descriptive statistics help in understanding the central tendency and variability of the data.
2. Inferential Statistics: This type of statistics is used to make inferences and predictions about a population based on a sample of data.
    It involves techniques such as hypothesis testing, confidence intervals, and regression analysis. Inferential statistics
    allow us to draw conclusions and make predictions about a larger group based on a smaller subset of data.

    descriptive means data ke baare me batana aur inferential means data ke baare me kuch nishkarsh nikalna ya predict karna.

    
--- 
population : poore data ko population kehte hai
sample : population me se kuch data ko sample kehte hai

--- 
measure of central tendency : mean , median , mode used in descriptive statistics to describe the central point of a dataset.
measure of variability : standard deviation , range used in descriptive statistics to describe the spread or dispersion of a dataset.
measure of dispersion : standard deviation , range used in descriptive statistics to describe the spread or dispersion of a dataset.

variance : variance is a measure of how much the data points in a dataset vary from the mean. It is calculated as the average of the squared differences from the mean. A higher variance indicates that the data points are more spread out, while a lower variance indicates that they are closer to the mean.
standard deviation : standard deviation is the square root of the variance. It is a measure of how much the data points in a dataset deviate from the mean on average. A higher standard deviation indicates that the data points are more spread out, while a lower standard deviation indicates that they are closer to the mean. 

variance use karke hum data ke spread ko samajh sakte hai aur standard deviation use karke hum data ke average deviation ko samajh sakte hai.

variance batata hai spread ko aur standard deviation batata hai average deviation ko ki tm data ke kitna door hai mean se.
ye ai ml me important hai kyuki jab hum model banate hai to hume data ke spread aur deviation ko samajhna hota hai taki hum model ko acche se train kar sake aur accurate predictions kar sake.

RANDOM VARIABLES : it is a variable that can take on different values based on the outcome of a random event. In ai ml, random variables are used to model uncertainty and make predictions based on probabilistic models. They can be discrete (taking on specific values) or continuous (taking on any value within a range). Random variables are essential for understanding and working with probability distributions, which are fundamental in ai ml for tasks such as classification, regression, and clustering.
                it is of two types : discrete and continuous. discrete random variable takes on specific values while continuous random variable takes on any value within a range.


PERCENTILE AND QUARTILE : Percentiles and quartiles are measures of position in a dataset that help to understand the distribution of the data.
EX :  {"data": [10, 20, 30, 40, 50],
     "percentiles": {50: 30},  # 50th percentile is 30
     "quartiles": {25: 20, 50: 30, 75: 40}  # Quartiles
}

another ex : {"data": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
     "percentiles": {25: 15, 50: 25, 75: 35},
     "quartiles": {25: 15, 50: 25, 75: 35}
}

5 NUMBER SUMMARY :  ye ek statistical summary hota hai jo data ke distribution ko summarize karta hai. Isme 5 numbers hote hai: minimum, 
first quartile (Q1), median (Q2), third quartile (Q3), aur maximum. Ye summary data ke spread aur central tendency ko samajhne me madad 
karta hai. aur outlier ko identify karne me bhi madad karta hai.aur remove karne me bhi madad karta hai.
EX : {"data": [10, 20, 30, 40, 50],
     "five_number_summary": {
         "minimum": 10,
         "q1": 20,
         "median": 30,
         "q3": 40,
         "maximum": 50
     }
}


COVARIANCE : covariance is a measure of how two random variables change together. It indicates the direction of the relationship between the variables. A positive covariance means that the variables tend to increase or decrease together, while a negative covariance means that one variable tends to increase when the other decreases. A covariance of zero indicates that there is no relationship between the variables. In ai ml, covariance is used in various algorithms such as principal component analysis (PCA) and linear regression to understand the relationships between features and target variables.
    ye kaam aata hia jab hum feature selection karte hai ya dimensionality reduction karte hai taki hum apne model ko acche se train kar sake aur accurate predictions kar sake.
    iska advantage ye hai ki ye hume features ke beech ke relationship ko samajhne me madad karta hai aur hum apne model ko acche se train kar sakte hai. iska disadvantage ye hai ki ye sirf linear relationship ko capture karta hai aur non-linear relationship ko capture nahi karta hai.
for example, if we have two features X and Y, and we calculate the covariance between them, a positive covariance would indicate that as X increases, Y also tends to increase. A negative covariance would indicate that as X increases, Y tends to decrease. A covariance of zero would indicate that there is no relationship between X and Y.
real world example : if we have a dataset of house prices and we want to understand the relationship between the size of the house (feature X) and the price of the house (feature Y), we can calculate the covariance between these two features. If we find a positive covariance, it would indicate that larger houses tend to have higher prices. If we find a negative covariance, it would indicate that larger houses tend to have lower prices. If we find a covariance of zero, it would indicate that there is no relationship between the size of the house and its price.
import numpy as np
# Example dataset
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 6, 8, 10])

# Calculate covariance
covariance = np.cov(X, Y)[0, 1]
print("Covariance between X and Y:", covariance)

iska jo bhi ans aayega wo positive hoga kyuki X aur Y ke beech me positive relationship hai. jaise X badhta hai to Y bhi badhta hai. isliye covariance positive aayega.

CORRELATION : correlation is a measure of the strength and direction of the relationship between two random variables. It is a standardized version of covariance that ranges from -1 to 1. A correlation of 1 indicates a perfect positive relationship, a correlation of -1 indicates a perfect negative relationship, and a correlation of 0 indicates no relationship between the variables. In ai ml, correlation is used to understand the relationships between features and target variables, and it can help in feature selection and model building.
    iska advantage ye hai ki ye hume features ke beech ke relationship ko samajhne me madad karta hai aur hum apne model ko acche se train kar sakte hai. iska disadvantage ye hai ki ye sirf linear relationship ko capture karta hai aur non-linear relationship ko capture nahi karta hai.
for example, if we have two features X and Y, and we calculate the correlation between them, a correlation of 0.8 would indicate a strong positive relationship, meaning that as X increases, Y also tends to increase. A correlation of -0.8 would indicate a strong negative relationship, meaning that as X increases, Y tends to decrease. A correlation of 0 would indicate that there is no relationship between X and Y.
import numpy as np
# Example dataset
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 6, 8, 10])
# Calculate correlation
correlation = np.corrcoef(X, Y)[0, 1]
print("Correlation between X and Y:", correlation)
iska jo bhi ans aayega wo positive hoga kyuki X aur Y ke beech me positive relationship hai. jaise X badhta hai to Y bhi badhta hai. isliye correlation positive aayega.









'''