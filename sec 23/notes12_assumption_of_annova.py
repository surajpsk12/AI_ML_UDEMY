"""

topic : assumption of annova        

defination : The assumptions of ANOVA (Analysis of Variance) are the conditions that must be met for the results of an ANOVA test to be valid and reliable.
1. Normality of sampling distribution of mean : The data should be approximately normally distributed for each group being compared. This can be assessed using normality tests (e.g., Shapiro-Wilk test) or visual methods (e.g., Q-Q plots).
2. Homogeneity of variances : The variances of the populations being compared should be equal across groups. This can be tested using Levene's test or Bartlett's test.
3. absence of outliers : Outliers can significantly affect the results of ANOVA. It is important to identify and address any outliers in the data before conducting the analysis.
4. Independence of observations : The observations within each group should be independent of each other. This means that the data points should not be related or influenced by one another.

ex : A researcher wants to compare the mean test scores of students from three different schools. Before conducting an ANOVA, they must ensure that the assumptions of normality, homogeneity of variances, absence of outliers, and independence of observations are met.

real life case study : In a study examining the effectiveness of three different teaching methods on student performance, researchers collected test scores from students in three different classrooms. Before analyzing the data using ANOVA, they checked for normality using Q-Q plots, tested for homogeneity of variances with Levene's test, identified and removed any outliers, and ensured that the observations were independent by confirming that students were randomly assigned to each teaching method.

use in ai ml : In AI and ML, ANOVA can be used to compare the performance of different machine learning models or algorithms on a specific dataset. For example, if a data scientist wants to compare the accuracy of three different classification algorithms (e.g., Decision Tree, Random Forest, and Support Vector Machine) on a dataset, they can use ANOVA to determine if there are statistically significant differences in their performance. Before conducting the ANOVA, they would need to check the assumptions of normality, homogeneity of variances, absence of outliers, and independence of observations to ensure valid results.


real problem solved code : 
```python 
import numpy as np
import pandas as pd
from scipy import stats

# Sample data: test scores from three different schools
data = {
    'School A': [85, 90, 78, 92, 88],
    'School B': [80, 82, 79, 85, 87],
    'School C': [90, 91, 89, 93, 95]
}

df = pd.DataFrame(data)

# Check for normality using Shapiro-Wilk test
for school in df.columns:
    stat, p = stats.shapiro(df[school])
    print(f'School: {school}, Statistics={stat:.3f}, p={p:.3f}')
    if p > 0.05:
        print(f'{school} data is normally distributed.')
    else:
        print(f'{school} data is not normally distributed.')


        

conclusion  : The assumptions of ANOVA must be met to ensure the validity and reliability of the results. In this example, we checked for normality, homogeneity of variances, absence of outliers, and independence of observations. Meeting these assumptions is crucial for making accurate inferences about the differences between group means.




"""