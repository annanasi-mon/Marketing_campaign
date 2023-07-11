# Marketing_campaign

This is a project concerning prediction whether the customer will repond to the offer for a product or service or not.

The dataset come from: https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign.

The data has been cleaned and preprocessed. The aforemrntioned steps, along with the modelling are covered in Marketing_Campaign_EDA_Preprocessing.ipynb file.
The project involves also a REST API for the model. The input to the API should be a dictionary with the input data. Preferably, all columns should be specified, however if some aren't present, they are replaced with the mean for continous variable, median for integer and most frequent value for categorical features. The output of the request is the prediction whether the customer will respond or not.
