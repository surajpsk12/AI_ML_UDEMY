'''
PROBABILITY FOR AI ML :  probability is the measure of the likelihood that an event will occur. It is quantified as a number between 0 and 1, where 0 indicates that the event will not occur and 1 indicates that the event will occur with certainty. In AI and ML, probability is used to make predictions, estimate uncertainties, and model complex systems. It plays a crucial role in various algorithms and techniques, such as Bayesian inference, decision trees, and neural networks.

this is useful for understanding how likely an event is to happen, which can help in making informed decisions and improving the performance of AI and ML models.
ye hme ml me use krna hota hai jab hme kisi event ke hone ke chances ko estimate krna hota hai, jaise ki kisi email ke spam hone ke chances, ya kisi customer ke product kharidne ke chances. Probability hme help krta hai ki hum apne models ko better banaye aur unke predictions ko zyada accurate banaye.

terms in probability:
1. Sample Space: The set of all possible outcomes of an experiment.
2. Event: A subset of the sample space, representing a specific outcome or a group of outcomes.
3. Probability of an Event: A measure of the likelihood that an event will occur, calculated as the ratio of the number of favorable outcomes to the total number of outcomes in the sample space.
4. Conditional Probability: The probability of an event occurring given that another event has already occurred.
5. Independent Events: Two events are independent if the occurrence of one event does not affect the probability of the other event occurring.
6. Dependent Events: Two events are dependent if the occurrence of one event affects the probability of the other event occurring.
7. Bayes' Theorem: A mathematical formula used to calculate the conditional probability of an event based on prior knowledge of conditions that might be related to the event.

ex of use in AI/ML:
1. Spam Detection: Probability is used to estimate the likelihood that an email is spam based on features such as the presence of certain keywords, the sender's address, and the email's structure.
2. Customer Churn Prediction: Probability is used to predict the likelihood that a customer will stop using a service or product based on their behavior, demographics, and past interactions.
3. Image Classification: Probability is used to assign a likelihood to each possible class label for an image, allowing the model to make predictions about what the image contains.
4. Naive Bayes Classifier: A machine learning algorithm that uses Bayes' theorem to classify data based on the probabilities of different features and their relationships to the target variable. 

Important Rules :
1. Addition Rule: The probability of the occurrence of at least one of two events is the sum of their individual probabilities minus the probability of their intersection (if they are not mutually exclusive). for ex : P(A or B) = P(A) + P(B) - P(A and B)
    - Mutually Exclusive Events: If two events cannot occur at the same time, then the probability of their intersection is zero, and the addition rule simplifies to P(A or B) = P(A) + P(B).
    - Non-Mutually Exclusive Events: If two events can occur at the same time, then the probability of their intersection is not zero, and the addition rule must account for this overlap to avoid double-counting.    

2. Multiplication Rule: The probability of the occurrence of two independent events is the product of their individual probabilities. For dependent events, the probability is the product of the probability of the first event and the conditional probability of the second event given that the first event has occurred. for ex : P(A and B) = P(A) * P(B) for independent events, and P(A and B) = P(A) * P(B|A) for dependent events.
    - Independent Events: If two events are independent, the occurrence of one event does not affect the probability of the other event occurring, and the multiplication rule simplifies to P(A and B) = P(A) * P(B).
    - Dependent Events: If two events are dependent, the occurrence of one event affects the probability of the other event occurring, and the multiplication rule must account for this relationship by using the conditional probability P(B|A) instead of P(B).
    
3. Bayes' Theorem: P(A|B) = (P(B|A) * P(A)) / P(B), where P(A|B) is the conditional probability of event A given event B, P(B|A) is the conditional probability of event B given event A, P(A) is the prior probability of event A, and P(B) is the prior probability of event B.  for ex : P(Disease|Symptom) = (P(Symptom|Disease) * P(Disease)) / P(Symptom)







'''