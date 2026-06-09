'''
Binomial Distribution :
The Binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. The distribution is parameterized by two parameters: n, which represents the number of trials, and p, which represents the probability of success in each trial. The probability mass function (PMF) of the Binomial distribution is given by:
P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)
where k is the number of successes (0 ≤ k ≤ n) and C(n, k) is the binomial coefficient, calculated as C(n, k) = n! / (k! * (n - k)!). The mean (expected value) of the Binomial distribution is given by n * p, and the variance is given by n * p * (1 - p). The Binomial distribution is often used in scenarios where we are interested in the number of successes in a fixed number of trials, such as the number of heads in a series of coin flips or the number of defective items in a batch of products.       

ex : 
Suppose we have a coin that is biased such that the probability of getting heads (success) is 0.7 and the probability of getting tails (failure) is 0.3. If we flip this coin 10 times, we can model the number of heads obtained using a Binomial distribution with n = 10 and p = 0.7.
The PMF of the Binomial distribution for this scenario would be:    
P(X = k) = C(10, k) * 0.7^k * 0.3^(10 - k)
where k can take values from 0 to 10. For example, the probability of getting exactly 7 heads (k = 7) would be:
P(X = 7) = C(10, 7) * 0.7^7 * 0.3^3 = 120 * 0.0823543 * 0.027 = 0.2668
This means that there is approximately a 26.68% chance of getting exactly 7 heads in 10 flips of this biased coin. The mean of this distribution would be n * p = 10 * 0.7 = 7, and the variance would be n * p * (1 - p) = 10 * 0.7 * 0.3 = 2.1.   


use in ml and ai : The Binomial distribution is commonly used in machine learning and artificial intelligence for modeling scenarios where we are interested in the number of successes in a fixed number of trials. For example, in a binary classification problem, we can use the Binomial distribution to model the number of correct predictions made by a classifier out of a fixed number of test samples. The Binomial distribution can also be used in A/B testing to model the number of successes (e.g., clicks, conversions) in two different groups (A and B) and compare their performance. Additionally, the Binomial distribution is often used in reinforcement learning to model the number of successful actions taken by an agent in a given environment. Overall, the Binomial distribution provides a useful framework for modeling count data and binary outcomes in various machine learning and AI applications.   
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
# Parameters
n = 10  # Number of trials
p = 0.7  # Probability of success
# Generate Binomial random variables
data = binom.rvs(n, p, size=1000)
# Plotting the PMF
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
plt.bar(x, pmf, color='blue')
plt.xticks(x)
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution PMF (n=10, p=0.7)')
plt.show()

case study :
Suppose we are developing a machine learning model to predict whether a customer will purchase a product (success) or not (failure) based on their browsing behavior on an e-commerce website. We can use the Binomial distribution to model the number of customers who make a purchase out of a fixed number of visitors to the website.
We can collect data on the number of visitors to the website and the number of those visitors who make a purchase. We can then use this data to estimate the parameters n (the total number of visitors) and p (the probability of a visitor making a purchase).
Once we have estimated n and p, we can use the Binomial distribution to make predictions about the number of customers who will make a purchase out of a given number of visitors. For example, if we estimate that n = 1000 and p = 0.3, we can predict that there is a 30% chance that a visitor will make a purchase, and we can also calculate the probability of getting a certain number of purchases (e.g., exactly 300 purchases) using the PMF of the Binomial distribution. We can also use the Binomial distribution to evaluate the performance of our model by comparing the predicted probabilities with the actual outcomes (the number of purchases made) and calculating metrics such as accuracy, precision, and recall. Overall, the Binomial distribution provides a useful framework for modeling count data and binary outcomes in machine learning applications, such as predicting customer behavior in e-commerce.


why we are studing it for ai ml : The Binomial distribution is a fundamental probability distribution that is widely used in machine learning and artificial intelligence for modeling scenarios where we are interested in the number of successes in a fixed number of trials. Understanding the Binomial distribution allows us to model and analyze binary outcomes, which are common in many machine learning applications, such as classification problems, A/B testing, and reinforcement learning. By studying the Binomial distribution, we can gain insights into the underlying probabilities of success and failure in various scenarios, which can help us make informed decisions and improve the performance of our models. Additionally, the Binomial distribution provides a basis for understanding more complex distributions and statistical methods that are used in machine learning and AI. Overall, studying the Binomial distribution is essential for building a strong foundation in probability theory and its applications in machine learning and artificial intelligence.    

real world example :
Suppose we are analyzing the performance of a new marketing campaign for an e-commerce website. We  can use the Binomial distribution to model the number of customers who make a purchase as a result of the campaign. We can collect data on the number of customers who were exposed to the campaign (n) and the number of those customers who made a purchase (k). By estimating the probability of success (p) based on this data, we can use the Binomial distribution to predict the likelihood of achieving a certain number of purchases in future campaigns. For example, if we estimate that p = 0.2, we can calculate the probability of getting at least 50 purchases out of 200 customers exposed to the campaign using the cumulative distribution function (CDF) of the Binomial distribution. This analysis can help us evaluate the effectiveness of the marketing campaign and make data-driven decisions for future campaigns.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
# Parameters
n = 200  # Number of customers exposed to the campaign
p = 0.2  # Probability of a customer making a purchase
# Generate Binomial random variables
data = binom.rvs(n, p, size=1000)
# Plotting the PMF
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
plt.bar(x, pmf, color='blue')
plt.xticks(x[::10])  # Show every 10th tick for better readability
plt.xlabel('Number of Purchases')
plt.ylabel('Probability')
plt.title('Binomial Distribution PMF (n=200, p=0.2)')
plt.show()



'''