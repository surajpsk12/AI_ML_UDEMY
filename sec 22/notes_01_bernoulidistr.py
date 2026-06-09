'''

Bernoulli distribution : 
The Bernoulli distribution is a discrete probability distribution that models a random experiment with only two possible outcomes: success (usually denoted as 1) and failure (usually denoted as 0). The distribution is parameterized by a single parameter, p, which represents the probability of success.
The probability mass function (PMF) of the Bernoulli distribution is given by:
P(X = x) = p^x * (1 - p)^(1 - x)
where x can take the values 0 or 1. The mean (expected value) of the Bernoulli distribution is equal to p, and the variance is given by p * (1 - p). The Bernoulli distribution is often used in scenarios where there are only two possible outcomes, such as coin flips, success/failure experiments, or binary classification problems.

ex : 

Suppose we have a coin that is biased such that the probability of getting heads (success) is 0.7 and the probability of getting tails (failure) is 0.3. We can model this situation using a Bernoulli distribution with p = 0.7. 
The PMF of the Bernoulli distribution for this coin would be:
P(X = 1) = 0.7^1 * (1 - 0.7)^(1 - 1) = 0.7
P(X = 0) = 0.7^0 * (1 - 0.7)^(1 - 0) = 0.3
This means that the probability of getting heads (success) is 0.7, and the probability of getting tails (failure) is 0.3. The mean of this distribution would be 0.7, and the variance would be 0.7 * (1 - 0.7) = 0.21. 


use in ml and ai : The Bernoulli distribution is commonly used in machine learning and artificial intelligence for modeling binary classification problems. In such problems, the goal is to predict whether an instance belongs to a particular class (success) or not (failure). For example, in spam email detection, the Bernoulli distribution can be used to model the probability of an email being classified as spam (success) or not spam (failure). The Bernoulli distribution can also be used in logistic regression, where the output is a binary variable
indicating the presence or absence of a certain characteristic. Additionally, the Bernoulli distribution is often used in reinforcement learning to model the probability of taking a certain action (success) or not taking that action (failure) in a given state. Overall, the Bernoulli distribution is a fundamental tool for modeling binary outcomes in various machine learning and AI applications.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
# Parameters
p = 0.7  # Probability of success
# Generate Bernoulli random variables
data = bernoulli.rvs(p, size=1000)
# Plotting the PMF
x = [0, 1]
pmf = [bernoulli.pmf(0, p), bernoulli.pmf(1, p)]
plt.bar(x, pmf, color=['blue', 'orange'])
plt.xticks(x)
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title('Bernoulli Distribution PMF (p=0.7)')
plt.show()


case study :
Suppose we are developing a machine learning model to predict whether a customer will purchase a product (success) or not (failure) based on their browsing behavior on an e-commerce website. We can use the Bernoulli distribution to model the probability of a customer making a purchase.  
We can collect data on customers' browsing behavior, such as the number of pages visited, time spent on the website, and previous purchase history. We can then use this data to estimate the parameter p, which represents the probability of a customer making a purchase.
Once we have estimated p, we can use the Bernoulli distribution to make predictions about whether a new customer will make a purchase or not. For example, if we estimate that p = 0.3, we can predict that there is a 30% chance that a new customer will make a purchase based on their browsing behavior. We can also use the Bernoulli distribution to evaluate the performance of our model by comparing the predicted probabilities with the actual outcomes (whether the customer made a purchase or not) and calculating metrics such as accuracy, precision, and recall. Overall, the Bernoulli distribution provides a useful framework for modeling binary outcomes in machine learning applications, such as predicting customer behavior in e-commerce.





'''