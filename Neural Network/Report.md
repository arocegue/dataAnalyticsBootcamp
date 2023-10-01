1. Overview of the analysis: Explain the purpose of this analysis.
- The purpose of this analysis is to help layout the steps taken to construct a model to help identify successful applicants to fund in their ventures.
2. Results: Using bulleted lists and images to support your answers, address the following questions:

- Data Preprocessing
  - What variable(s) are the target(s) for your model?
    - IS_SUCCESSFUL—Was the money used effectively
  - What variable(s) are the features for your model?
    -  EIN and NAME—Identification columns
    - APPLICATION_TYPE—Alphabet Soup application type
    - AFFILIATION—Affiliated sector of industry
    - CLASSIFICATION—Government organization classification
    - USE_CASE—Use case for funding
    - ORGANIZATION—Organization type
    - STATUS—Active status
    - INCOME_AMT—Income classification
    - SPECIAL_CONSIDERATIONS—Special considerations for application
    - ASK_AMT—Funding amount requested
  - What variable(s) should be removed from the input data because they are neither targets nor features?
    - I dropped EIN and NAME since these provide no benefit in the feature set.

- Compiling, Training, and Evaluating the Model
  - How many neurons, layers, and activation functions did you select for your neural network model, and why?
    - I added two hidden layers and one output layer. The first hidden layer I inputted the the input dimensions of the feature set and included the same number for the number of neurons. This was to account for each feature for one neuron. The second hidden layer I decreased the neurons to 8 so that parameter do not get flooded and cause an overfit situation. Both of these hidden layers used a relu activation function because we wanted to keep values between zero and one. The output layer contained one neuron because we only want one value back and used the sigmoid activation function.
  - Were you able to achieve the target model performance?
    - I was able to land a 72% success rate which is pretty good given the feature set.
  - What steps did you take in your attempts to increase model performance?
    - Changed amount of neurons and hidden layers. Also tried different activation functions. I also dropped organization and status as they seemed a bit as an outlier in the feature set.

3. Summary: Summarize the overall results of the deep learning model. Include a recommendation for how a different model could solve this classification problem, and then explain your recommendation.
- The overall results were pretty good for a neural network model however it is clear that there are still improvements to be made. I believe a KNN model can be another alternative instead of creating a deep learning model to help classify this problem with support vectors. 
