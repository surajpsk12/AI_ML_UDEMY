'''
normal distribution :
The Normal distribution, also known as the Gaussian distribution, is a continuous probability distribution that is symmetric around its mean, μ, and characterized by its standard deviation, σ. The probability density function (PDF) of the Normal distribution is given by:
f(x) = (1 / (σ * sqrt(2 * π))) * exp(-((x - μ)^2) / (2 * σ^2))
where x is the variable, μ is the mean, σ is the standard deviation, and π is the mathematical constant approximately equal to 3.14159. The Normal distribution is widely used in statistics and machine learning due to its properties, such as the Central Limit Theorem, which states that the sum of a large number of independent and identically distributed random variables will approximate a Normal distribution, regardless of the original distribution of the variables.

ex : 
Suppose we have a dataset of heights of individuals in a population, and we find that the mean height is 170 cm with a standard deviation of 10 cm. We can model the distribution of heights using a Normal distribution with μ = 170 and σ = 10. The PDF of the Normal distribution for this scenario would be:
f(x) = (1 / (10 * sqrt(2 * π))) * exp(-((x - 170)^2) / (2 * 10^2))

This means that the heights of individuals in the population are likely to be around 170 cm, with most heights falling within the range of 160 cm to 180 cm (within one standard deviation from the mean). The mean of this distribution would be 170, and the variance would be 10^2 = 100.    

real world example :Suppose we are analyzing the test scores of students in a standardized exam. We find that the average test score is 75 with a standard deviation of 10. We can model the distribution of test
scores using a Normal distribution with μ = 75 and σ = 10. The PDF of the Normal distribution for this scenario would be:
f(x) = (1 / (10 * sqrt(2 * π))) * exp(-((x - 75)^2) / (2 * 10^2))
This means that the test scores of students are likely to be around 75, with most scores falling within the range of 65 to 85 (within one standard deviation from the mean). We can also calculate the probability of a student scoring above a certain threshold (e.g., 85) using the cumulative distribution function (CDF) of the Normal distribution. This analysis can help us understand the performance of students and identify areas for improvement in education.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Parameters
mu = 170  # Mean height
sigma = 10  # Standard deviation
# Generate Normal random variables
data = norm.rvs(mu, sigma, size=1000)
# Plotting the PDF
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
pdf = norm.pdf(x, mu, sigma)
plt.plot(x, pdf, color='blue')
plt.xlabel('Height (cm)')
plt.ylabel('Probability Density')
plt.title('Normal Distribution PDF (μ=170, σ=10)')
plt.show()


use in ai ml : The Normal distribution is commonly used in machine learning and artificial intelligence for modeling continuous data and making predictions. For example, in regression analysis, the Normal distribution can be used to model the residuals (the differences between observed and predicted values) to assess the goodness of fit of a regression model. In classification problems, the Normal distribution can be used in algorithms such as Gaussian Naive Bayes, where it is assumed that the features follow a Normal distribution. Additionally, the Normal distribution is often used in anomaly detection to identify outliers in data, as data points that fall far from the mean are considered anomalies. Overall, the Normal distribution provides a useful framework for modeling continuous data and making predictions in various machine learning and AI applications. 

conclusion : The Normal distribution is a fundamental probability distribution that is widely used in statistics, machine learning, and artificial intelligence for modeling continuous data and making predictions. It is characterized by its mean and standard deviation, which determine the shape of the distribution. The properties of the Normal distribution, such as the Central Limit Theorem, make it a powerful tool for analyzing data and understanding underlying patterns. By studying the Normal distribution, we can gain insights into the behavior of data and improve our ability to make informed decisions based on that data in various machine learning and AI applications.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Parameters
mu = 75  # Mean test score
sigma = 10  # Standard deviation
# Generate Normal random variables
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