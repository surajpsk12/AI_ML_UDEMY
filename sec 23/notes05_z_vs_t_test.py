'''
topic : Z vs T Test for Hypothesis Testing 

defination :  Z-test and T-test are both statistical tests used to determine whether there is a significant difference between the means of two groups. The choice between the two tests depends on the sample size and whether the population standard deviation is known.
- Z-test is used when the sample size is large (typically n > 30) and the population standard deviation is known. It relies on the standard normal distribution (Z distribution) to calculate the test statistic and p-value.
- T-test is used when the sample size is small (typically n ≤ 30) and the population standard deviation is unknown. It relies on the T distribution, which accounts for the additional uncertainty introduced by estimating the population standard deviation from the sample data. 

ex :  1. Suppose we want to test whether a new teaching method is more effective than the traditional method. We collect data on test scores from two groups of students: one group taught using the new method and another group taught using the traditional method. If the sample size is large and the population standard deviation is known, we can use a Z-test to compare the means of the two groups. However, if the sample size is small and the population standard deviation is unknown, we would use a T-test to compare the means and determine if there is a statistically significant difference in their performance.
    2. A company wants to know if a new marketing strategy has increased sales. They collect sales data from two different time periods: before and after implementing the new strategy. If the sample size is large and the population standard deviation is known, they can perform a Z-test to compare the average sales from both periods. However, if the sample size is small and the population standard deviation is unknown, they would use a T-test to analyze the data and determine if the new strategy has had a significant impact on sales performance.
    import numpy as np
    import scipy.stats as stats
    # Sample data: test scores from two groups of students
    group1_scores = np.array([85, 90, 78, 92, 88])
    group2_scores = np.array([80, 82, 78, 85, 90])
    # Calculate the means and standard deviations of both groups
    mean1 = np.mean(group1_scores)
    mean2 = np.mean(group2_scores)
    std1 = np.std(group1_scores, ddof=1)  # ddof=1 for sample standard deviation
    std2 = np.std(group2_scores, ddof=1)
    # Perform the Z-test (assuming population standard deviation is known)
    z_statistic, p_value = stats.ttest_ind(group1_scores, group2_scores)
    print(f"Z-statistic: {z_statistic}, P-value: {p_value}")
    # Interpretation of the results
    if p_value < 0.05:
        print("There is a statistically significant difference between the two groups. Reject the null hypothesis.")
    else:    print("There is no statistically significant difference between the two groups. Fail to reject the null hypothesis.")


real life scenario : A healthcare organization wants to evaluate the effectiveness of a new treatment for a specific medical condition. They conduct a clinical trial with two groups of patients: one group receives the new treatment, while the other group receives the standard treatment. After collecting data on patient outcomes, they perform a Z-test to compare the mean recovery times between the two groups if the sample size is large and the population standard deviation is known. However, if the sample size is small and the population standard deviation is unknown, they would use a T-test to analyze the data and determine whether the new treatment is significantly more effective than the standard treatment, guiding future decisions about patient care and treatment protocols.
                    1. In this scenario, the choice between a Z-test and a T-test depends on the sample size and the availability of population standard deviation. If the Z-test indicates a significant difference in recovery times, the healthcare organization may consider adopting the new treatment as a standard practice, ultimately improving patient outcomes and advancing medical care. Conversely, if the T-test does not show a significant difference, they may decide to iterate on the treatment or explore alternative solutions to improve patient outcomes.
                    2. Another example could be in the field of education, where researchers want to compare the effectiveness of two different teaching methods on student performance. They collect test scores from two groups of students, each taught using a different method, and perform either a Z-test or a T-test based on the sample size and availability of population standard deviation to determine if there is a significant difference in their average scores. The results can inform decisions about which teaching method to implement more widely in schools, ultimately enhancing educational outcomes for students. 

case study : A technology company is testing a new software feature to determine if it improves user engagement compared to the existing version. They conduct an A/B test with two groups of users: one group experiences the new feature, while the other group continues to use the existing version. After collecting data on user engagement metrics, such as time spent on the platform and click-through rates, they perform either a Z-test or a T-test based on the sample size and availability of population standard deviation to compare the means of these metrics between the two groups. The results help them determine whether the new feature has a statistically significant impact on user engagement, guiding decisions about whether to roll out the feature to all users or make further improvements based on the feedback received.
 - In this case study, the choice between a Z-test and a T-test depends on the characteristics of the data collected. If the Z-test indicates a significant improvement in user engagement, the company may choose to implement the new feature across their platform, enhancing the user experience and potentially increasing customer satisfaction and retention. Conversely, if the T-test does not show a significant difference, they may decide to iterate on the feature or explore alternative solutions to improve user engagement.
 - Another example could be in the field of marketing, where a company wants to compare the effectiveness of two different advertising campaigns. They run an A/B test with two groups of customers, each exposed to a different campaign, and perform either a Z-test or a T-test based on the sample size and availability of population standard deviation to analyze the differences in conversion rates between the two groups. The results can inform future marketing strategies and help optimize advertising efforts for better results. 

use in ai ml : In AI and machine learning, Z-tests and T-tests can be used to compare the performance of different models or algorithms. For example, when evaluating the accuracy of two classification models, researchers can perform either a Z-test or a T-test based on the sample size and availability of population standard deviation to determine if the difference in their performance metrics (such as accuracy, precision, or recall) is statistically significant. This helps in making informed decisions about which model to deploy in real-world applications, ensuring that the chosen model is not only effective but also statistically justified based on the data.
                - For instance, in a classification problem, researchers might compare the performance of two algorithms using either a Z-test or a T-test based on the characteristics of the data and calculate the p-value to determine if the observed difference in accuracy is statistically significant. This helps in making informed decisions about which model to deploy in real-world applications, ensuring that the chosen model is not only effective but also statistically justified based on the data.
                - In summary, Z-tests and T-tests play a crucial role in AI and machine learning by aiding in model evaluation and comparison, ultimately contributing to the development of more robust and effective models.
                - For example, in a regression problem, researchers might use either a Z-test or a T-test to compare the coefficients of two different models to determine if one model provides a significantly better fit to the data than the other. This can help in selecting the most appropriate model for making predictions and drawing conclusions from the data.
                - Additionally, Z-tests and T-tests can be used in feature selection to determine if the mean of a particular feature is significantly different between two classes in a classification problem. This can help in identifying important features that contribute to the model's performance and improving the interpretability of the model. For instance, in a binary classification problem, researchers might perform either a Z-test or a T-test

def solution using code : 
    import numpy as np
    import scipy.stats as stats
    # Sample data: test scores from two groups of students
    group1_scores = np.array([85, 90, 78, 92, 88])
    group2_scores = np.array([80, 82, 78, 85, 90])
    # Calculate the means and standard deviations of both groups
    mean1 = np.mean(group1_scores)
    mean2 = np.mean(group2_scores)
    std1 = np.std(group1_scores, ddof=1)  # ddof=1 for sample standard deviation
    std2 = np.std(group2_scores, ddof=1)
    # Perform the Z-test (assuming population standard deviation is known)
    z_statistic, p_value = stats.ttest_ind(group1_scores, group2_scores)
    print(f"Z-statistic: {z_statistic}, P-value: {p_value}")
    # Interpretation of the results
    if p_value < 0.05:
        print("There is a statistically significant difference between the two groups. Reject the null hypothesis.")
    else:
        print("There is no statistically significant difference between the two groups. Fail to reject the null hypothesis.")

conclusion : The choice between a Z-test and a T-test for hypothesis testing depends on the sample size and whether the population standard deviation is known. Z-tests are appropriate for large samples with known population standard deviations, while T-tests are suitable for small samples with unknown population standard deviations. Both tests play a crucial role in various fields, including healthcare, education, marketing, and AI/ML, by helping researchers and analysts make informed decisions based on data analysis. Understanding the differences between these tests and when to use each one is essential for drawing valid conclusions and making informed decisions in research and real-world applications.



'''