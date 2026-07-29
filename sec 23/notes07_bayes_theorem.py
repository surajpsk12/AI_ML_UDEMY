'''
topic : Bayes theorem 

definition : A theorem in probability theory that describes the probability of an event based on prior knowledge of conditions that might be related to the event.


ex : example : 1. Medical diagnosis: Given the symptoms of a patient, Bayes' theorem can be used to calculate the probability of a specific disease being present.
          2. Spam filtering: Bayes' theorem can be used to classify emails as spam or not spam based on the words present in the email. 


real life case study : 
    1. Medical diagnosis: A doctor uses Bayes' theorem to update the probability of a patient having a disease based on the patient's symptoms and test results.
    2. Search engines: Bayes' theorem is used to rank web pages based on the probability of relevance given a user's search query.
    3. Weather forecasting: Bayes' theorem is used to update the probability of different weather conditions based on new data and observations.
    4. Fraud detection: Bayes' theorem is used to calculate the probability of a transaction being fraudulent based on historical data and patterns.


use in ai ml :
    - Spam filtering: Bayes' theorem is used in spam filters to classify emails as spam or not spam based on the words present in the email.
    - Sentiment analysis: Bayes' theorem can be used to classify text as positive, negative, or neutral based on the words present in the text.
    - Recommendation systems: Bayes' theorem can be used to predict user preferences and recommend products or content based on their past behavior and preferences.
    - Anomaly detection: Bayes' theorem can be used to detect anomalies in data by calculating the probability of an observation being an outlier based on prior knowledge of the data distribution.
    - Fraud detection: Bayes' theorem can be used to calculate the probability of a transaction being fraudulent based on historical data and patterns.

code :
    import numpy as np
    def bayes_theorem(prior_A, prior_B, likelihood_A_given_B, likelihood_B_given_A):
        # Calculate the posterior probability of A given B using Bayes' theorem
        posterior_A_given_B = (likelihood_A_given_B * prior_A) / ((likelihood_A_given_B * prior_A) + (likelihood_B_given_A * prior_B))
        return posterior_A_given_B

        
conclusion : Bayes' theorem is a powerful tool in probability theory that allows us to update our beliefs about an event based on new evidence. It has numerous applications in various fields, including medical diagnosis, spam filtering, search engines, weather forecasting, fraud detection, and AI/ML. By understanding and applying Bayes' theorem, we can make more informed decisions and predictions based on prior knowledge and observed data.

'''