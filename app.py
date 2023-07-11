import uvicorn
from fastapi import FastAPI
from input_data import Input_data
import numpy as np
import pandas as pd
import pickle
import traceback, sys
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


# import model, model columns, scaler and encoder
model = pickle.load(open("RF_model.pkl", "rb"))
imputer = pickle.load(open("imputer.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

# REST API
app = FastAPI()

#Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return 'Welcome to my Rest API, to see predictions for the input data go to /predict'

# Pass json data to make a prediction
@app.post('/predict')
def predict_response(data: Input_data):

    if model:
        try:
            data = pd.DataFrame([data.dict()])
            data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'])
            data['day'] = data.loc[:, 'Dt_Customer'].dt.day
            data['month'] = data.loc[:, 'Dt_Customer'].dt.month
            data['year'] = data.loc[:, 'Dt_Customer'].dt.year
            data.drop(['Dt_Customer'], axis=1, inplace=True)
            imputed = imputer.transform(data)
            # imputed = pd.DataFrame(imputed)
            imputed_df = pd.DataFrame(imputed, columns=['Income', 'ID', 'Year_Birth', 'Kidhome', 'Teenhome', 'Recency', 'MntWines',
       'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
       'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
       'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1',
       'AcceptedCmp2', 'Complain', 'Z_CostContact', 'Z_Revenue',
       'day', 'month', 'year', 'Education', 'Marital_Status', 'Response'])
            imputed_df['Years_Old'] = imputed_df['Year_Birth'].map(lambda x: (int(2023) - int(x)))
            imputed_df[['ID', 'Year_Birth', 'Kidhome',
       'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts',
       'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
       'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
       'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3',
       'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2',
       'Complain', 'Z_CostContact', 'Z_Revenue', 'day', 'month',
       'year']] = imputed_df[['ID', 'Year_Birth', 'Kidhome',
       'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts',
       'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
       'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
       'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3',
       'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2',
       'Complain', 'Z_CostContact', 'Z_Revenue', 'day', 'month',
       'year']].astype(int)
            # imputed_df = imputed_df.astype(data.dtypes.to_dict())

            for col in imputed_df.select_dtypes(include='O').columns:
                imputed_df[col] = encoder.fit_transform(imputed_df[col])

            imputed_df.drop(['Response'], axis=1, inplace=True)
            scaled_data = scaler.transform(imputed_df)
            prediction = model.predict(scaled_data)

            if prediction[0] == 0:
                predicted_class = 'The client will not respond to an offer'
            elif prediction[0] == 1:
                predicted_class = 'The client will respond to an offer'

            return f'The prediction is: {predicted_class}'

        except:
            return {'trace': traceback.format_exc()}

        else:
            return ('There is no model to use')






if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload