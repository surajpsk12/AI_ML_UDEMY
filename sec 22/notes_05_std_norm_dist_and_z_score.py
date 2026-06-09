'''
Standard Normal Distribution and Z-Score:
The Standard Normal distribution, also known as the Z-distribution, is a special case of the Normal distribution where the mean (μ) is 0 and the standard deviation (σ) is 1. The probability density function (PDF) of the Standard Normal distribution is given by:
f(z) = (1 / sqrt(2 * π)) * exp(-z^2 / 2)
where z is the standard score or z-score, which represents the number of standard deviations a data point is from the mean. The z-score is calculated using the formula:
z = (X - μ) / σ
where X is the value of the data point, μ is the mean of the distribution, and σ is the standard deviation of the distribution. The Standard Normal distribution is widely used in statistics and machine learning for standardizing data and making comparisons across different datasets.

ex :
Suppose we have a dataset of test scores with a mean of 75 and a standard deviation of 10. If a student scored 85 on the test, we can calculate the z-score for this score using the formula:
z = (85 - 75) / 10 = 1
This means that the student's score is 1 standard deviation above the mean. We can also use the Standard Normal distribution to calculate the probability of a student scoring above 85 by finding the area under the curve to the right of z = 1. This can be done using the cumulative distribution function (CDF) of the Standard Normal distribution.
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm
# Parameters
mu = 75  # Mean test score
sigma = 10  # Standard deviation
# Generate Standard Normal random variables
data = norm.rvs(mu, sigma, size=1000)
# Plotting the PDF
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
pdf = norm.pdf(x, mu, sigma)
plt.plot(x, pdf, color='blue')
plt.xlabel('Test Score')
plt.ylabel('Probability Density')
plt.title('Normal Distribution PDF (μ=75, σ=10)')
plt.show()

use in ai ml : The Standard Normal distribution and z-scores are commonly used in machine learning and artificial intelligence for standardizing data and making comparisons across different datasets. For example, in feature scaling, we can use z-scores to standardize the features of a dataset, which can help improve the performance of machine learning algorithms that are sensitive to the scale of the data, such as k-nearest neighbors and support vector machines. Additionally, z-scores can be used in anomaly detection to identify outliers in data, as data points with z-scores that are significantly higher or lower than 0 may be considered anomalies. Overall, understanding the Standard Normal distribution and z-scores is essential for effectively preprocessing data and making informed decisions based on that data in various machine learning and AI applications.

case study :
Suppose we are developing a machine learning model to predict the likelihood of a customer making a purchase based on their browsing behavior on an e-commerce website. We can use z-scores to standardize the features of our dataset, such as the number of pages visited, time spent on the website, and previous purchase history. By calculating the z-scores for these features, we can ensure that they are on the same scale and improve the performance of our machine learning model. Additionally, we can use z-scores to identify outliers in our dataset, which may indicate unusual browsing behavior that could be indicative of fraudulent activity. Overall, using z-scores and the Standard Normal distribution can help us preprocess our data effectively and make informed decisions based on that data in our machine learning model.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Parameters
mu = 75  # Mean test score
sigma = 10  # Standard deviation
# Generate Standard Normal random variables
data = norm.rvs(mu, sigma, size=1000)
# Plotting the PDF
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
pdf = norm.pdf(x, mu, sigma)
plt.plot(x, pdf, color='blue')
plt.xlabel('Test Score')
plt.ylabel('Probability Density')
plt.title('Normal Distribution PDF (μ=75, σ=10)')
plt.show()


conclusion : The Standard Normal distribution and z-scores are fundamental concepts in statistics and machine learning that are essential for standardizing data and making comparisons across different datasets. By understanding how to calculate z-scores and use the properties of the Standard Normal distribution, we can effectively preprocess our data, identify outliers, and improve the performance of our machine learning models. The Standard Normal distribution provides a useful framework for analyzing data and making informed decisions based on that data in various machine learning and AI applications.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Parameters
mu = 75  # Mean test score
sigma = 10  # Standard deviation
# Generate Standard Normal random variables
data = norm.rvs(mu, sigma, size=1000)
# Plotting the PDF
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
pdf = norm.pdf(x, mu, sigma)
plt.plot(x, pdf, color='blue')
plt.xlabel('Test Score')
plt.ylabel('Probability Density')
plt.title('Normal Distribution PDF (μ=75, σ=10)')
plt.show()





'''