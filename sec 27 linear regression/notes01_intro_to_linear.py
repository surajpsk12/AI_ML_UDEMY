'''
ek best fit line banate hai fir uska x axix ka value ke liye y axis ka value return karte hai , model y value return karta hai fir hum usko plot karte hai aur dekhte hai ki best fit line data ke sath kitna match kar rahi hai . 

aur jaane ke liye gen ai karo 


best fit line ka matlab hai ki hum data ke points ke beech me ek line draw karte hai jo ki un points ke beech me sabse acchi fit hoti hai . 


cost function ka matlab hai ki hum ek function define karte hai jo ki humare model ke predictions aur actual data ke beech me difference ko measure karta hai . usse fir hm error niklate hia ki kitna difference hai aur fir usse minimize karte hai taki humare model ke predictions aur actual data ke beech me difference kam se kam ho .

convergence algorithm ka matlab hai ki hum ek algorithm define karte hai jo ki humare model ke parameters ko update karta hai taki humare cost function ko minimize kar sake . aur fir hum usse iterate karte hai jab tak humare cost function ka value minimum na ho jaye .taaki predictions aur actual data ke beech me difference kam se kam ho jaye .to better rahega model like ekdum real ans predict karega .

multiple linear regression ka matlab hai ki hum ek model define karte hai jo ki multiple independent variables ke basis pe dependent variable ko predict karta hai . aur fir hum usse train karte hai taki humare model ke predictions aur actual data ke beech me difference kam se kam ho jaye .

jaise ki house prediction me hum multiple independent variables jaise ki house ka size , location , number of rooms , age of the house etc. ke basis pe dependent variable jaise ki house ka price ko predict karte hai . aur fir hum usse train karte hai taki humare model ke predictions aur actual data ke beech me difference kam se kam ho jaye .

in short , best fit line , cost function , convergence algorithm aur multiple linear regression ye sabhi concepts ek dusre se related hai aur ye sabhi concepts ek dusre ke sath milke ek accha model banate hai jo ki real world data ke sath match karta hai .


PERFORMANCE METRICS 
R SQUARE AND ADJUSTED R SQUARE :   

in simple words , R square is a statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model. It provides an indication of goodness of fit and therefore a measure of how well unseen samples are likely to be predicted by the model, through the proportion of explained variance.

dono ka jarurat hota hai kyuki R square ka value hamesha increase hota hai jab hum independent variable ko add karte hai , aur adjusted R square ka value decrease hota hai jab hum independent variable ko add karte hai .

ye model training ke liye important hai kyuki ye hume batata hai ki humare model ka performance kaisa hai aur humare model ke predictions aur actual data ke beech me difference kitna hai .


MSE , MAE , RMSE : ye sabhi performance metrics hai jo ki humare model ke predictions aur actual data ke beech me difference ko measure karte hai . 

MSE ka matlab hai ki humare model ke predictions aur actual data ke beech me difference ka square ka average nikalte hai .
usse fayda hota hai ki hm large errors ko jyada penalize karte hai aur fir humare model ke predictions aur actual data ke beech me difference ko minimize karte hai .nai to outliers ka effect jyada hota hai aur fir humare model ke predictions aur actual data ke beech me difference jyada ho jata hai .

MAE ka matlab hai ki humare model ke predictions aur actual data ke beech me difference ka absolute value ka average nikalte hai .isse fayda hota hai ki hm large errors ko jyada penalize nahi karte hai aur fir humare model ke predictions aur actual data ke beech me difference ko minimize karte hai .nai to outliers ka effect jyada nahi hota hai aur fir humare model ke predictions aur actual data ke beech me difference jyada nahi ho jata hai .

RMSE ka matlab hai ki humare model ke predictions aur actual data ke beech me difference ka square root ka average nikalte hai .isse fayda hota hai ki hm large errors ko jyada penalize karte hai aur fir humare model ke predictions aur actual data ke beech me difference ko minimize karte hai .nai to outliers ka effect jyada hota hai aur fir humare model ke predictions aur actual data ke beech me difference jyada ho jata hai .


Approach to model training :
1. Data Collection : sabse pehle hum data collect karte hai jo ki humare model ke liye important hai . data ko collect karne ke liye hum different sources ka use karte hai jaise ki kaggle , uci machine learning repository , government websites , etc.

2. Data Preprocessing : data ko collect karne ke baad hum usse preprocess karte hai taki humare model ke liye ready ho jaye . data preprocessing me hum missing values ko handle karte hai , outliers ko handle karte hai , data ko normalize karte hai , data ko encode karte hai , etc.

3. Model Selection : data ko preprocess karne ke baad hum model select karte hai jo ki humare problem ke liye best fit ho . model selection me hum different models ka use karte hai jaise ki linear regression , decision tree , random forest , etc.

4. Model Training : model select karne ke baad hum usse train karte hai taki humare model ke predictions aur actual data ke beech me difference kam se kam ho jaye . model training me hum different algorithms ka use karte hai jaise ki gradient descent , stochastic gradient descent , etc.

5. Model Evaluation : model train karne ke baad hum usse evaluate karte hai taki humare model ka performance kaisa hai aur humare model ke predictions aur actual data ke beech me difference kitna hai . model evaluation me hum different performance metrics ka use karte hai jaise ki R square , adjusted R square , MSE , MAE , RMSE , etc.

6. Model Tuning : model evaluate karne ke baad hum usse tune karte hai taki humare model ka performance aur better ho jaye . model tuning me hum different techniques ka use karte hai jaise ki hyperparameter tuning , feature selection , etc.

7. Model Deployment : model tune karne ke baad hum usse deploy karte hai taki humare model ke predictions real world data ke sath match kare . model deployment me hum different techniques ka use karte hai jaise ki flask , django , etc.
 
8. Model Monitoring : model deploy karne ke baad hum usse monitor karte hai taki humare model ka performance real world data ke sath match kare . model monitoring me hum different techniques ka use karte hai jaise ki logging , alerting , etc.

9. Model Maintenance : model monitor karne ke baad hum usse maintain karte hai taki humare model ka performance real world data ke sath match kare . model maintenance me hum different techniques ka use karte hai jaise ki retraining , updating , etc.

jab hme data milega usko 2 parts me divide karenge , ek part training ke liye aur dusra part testing ke liye . fir hum training data ko use karke model ko train karenge aur fir testing data ko use karke model ka performance evaluate karenge .


training data ko another two parts me divide karenge , ek part validation ke liye aur dusra part training ke liye . fir hum training data ko use karke model ko train karenge aur fir validation data ko use karke model ka performance evaluate karenge . aur fir hum model ko tune karenge taki humare model ka performance aur better ho jaye . aur fir hum testing data ko use karke model ka performance evaluate karenge .


OVERFITTING AND UNDERFITTING 

Overfitting ka matlab hai ki humare model ne training data ke sath itna fit ho gaya hai ki wo testing data ke sath match nahi kar raha hai . iska matlab hai ki humare model ne training data ke noise ko bhi learn kar liya hai aur fir wo testing data ke sath match nahi kar raha hai . iska solution hai ki humare model ko simplify kare taki wo testing data ke sath match kare .

Underfitting ka matlab hai ki humare model ne training data ke sath itna fit nahi ho gaya hai ki wo testing data ke sath match nahi kar raha hai . iska matlab hai ki humare model ne training data ke patterns ko bhi learn nahi kiya hai aur fir wo testing data ke sath match nahi kar raha hai . iska solution hai ki humare model ko complex kare taki wo testing data ke sath match kare . isme hai ki train hi thk se nai hua , overfitting me to train thk se hua tha but test me sahi perform kiya , but underfitting me train hi thk se nai hua tha , to test me bhi sahi perform nai kiya .




'''