"""

topic : handling missing values

defination : Handling missing values is a crucial step in data preprocessing for machine learning. It involves identifying and addressing gaps or null entries in datasets to ensure the quality and reliability of the data used for model training.

ex : In a customer dataset, some customers may not have provided their age information, resulting in missing values.

real life case study : A healthcare dataset where some patients have not provided their blood pressure readings, leading to missing values.

use in ai ml : Handling missing values is essential in AI and ML to prevent biased models and improve prediction accuracy. Techniques like imputation, deletion, or using algorithms that can handle missing data are commonly employed.

real problem solved code : 


conclusion : 




isme data bahot tarah se missing ho sakte hia , by chance or by choice . so ab dekhna missing value ko kaise find kare . 

we use seaborn to visualise it , but sometime to load dataset . 
how we handle missing value : imputation technique 

1. imputation missing value | Mean Value Imputation : jisme bhi nan hai ya data nai hai usme mean value fill kar deenge . 
    steps : new column like banake means se replace kardo . ex : df['Age_mean']=df['age'].fillna(df['age'].mean())

    MEan Imputation Works Well when we have normally distributed data



"""