# Module 12 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.
- The purpose of this analysis was to figure out a model to predict clients approval for a loan at an established bank.
* Explain what financial information the data was on, and what you needed to predict.
- The provided dataset had us look over loan size, interest rate, borrower income, debt to income, number of accounts, derogatory marks, total debt. With these features we needed to predict if they were approved for the loan.
* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).
- The loan approvals, which were 0 for healthy and 1 for high risk loans. This was under the loan status column.0:75036, 1: 2500
* Describe the stages of the machine learning process you went through as part of this analysis.
- We split the data with the feature set given (X) except loan status which was our label set (y). We then created a logistic regression model to fit our x and y training data to predict our loan status with our testing data. 

- Our next model followed the same procedure however it we resampled our X and y to create an even distribution between the healthy and high risk loans. And trained a logistic regression model to try to have a higher prediction success rate with an even amount of y.
* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).
- We used Logistic Regression models and one model saw a resampler to even out y distribution.
## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
- The balanced accuracy score gives us an overview of the accuracy of the logistic model we created and fitted with our training data by testing our split (20%) data predictions. This model gave us a 94% accuracy.
- The confusion matrix gives us almost a 99% True Negative, and a 89% True Positive.
- Running a classification report gave us an insight on precision and recall scores:
  - Precision saw a 100% accuracy on Healthy Loan and 87% precision score on high risk loans. This is something we saw with the confusion matrix, it lists the actual true predictions.
  - Recall saw a 100% recall score with healthy loans and an 89% on risk loans. Recall is the sum of all predictions. 


* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
- The balanced accuracy score gives us an overview of the accuracy of the logistic model we created and fitted with our training data by testing our split (20%) data predictions. This model gave us a 99% accuracy.
- The confusion matrix gives us almost a 99% True Negative, and a 99% True Positive.
- Running a classification report gave us an insight on precision and recall scores:
  - Precision saw a 99% accuracy on Healthy Loan and 99% precision score on high risk loans. This is something we saw with the confusion matrix, it lists the actual true predictions.
  - Recall saw a 99% recall score with healthy loans and an 99% on risk loans. Recall is the sum of all predictions. 
## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
- The second model seems to perform the best because of the resampling the data saw. It evenly distributes the amount of healthy and high risk loans there are which was a suggestion I had when running the first model. There wasnt enough high risk data points to help classify future predictions. With the resampling we saw an increase of high risk loans and more data points for the logistic regression model to train on. However, I am cautious with this approach as it is more synthetic data being put in which can lead to an overfitting situation.

* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )

- I would say it is more important to predict high risk loans as the model has no problem on handling healthy loans. Since high risk loans can cost the company money to untrustworthy clients.

If you do not recommend any of the models, please justify your reasoning.
 I do not recommend on using any of these models as there are mediations that need to occur when running a dataset with this. I pointed out our second model is synthetic due to the resampling which lead to higher success rate in high risk loans. High risk loans needs a bit more real world data and maybe someone to have a final call before applying the loan to these clients.