
from pydantic import BaseModel
import pandas as pd
import numpy as np

class Input_data(BaseModel):
    ID : int = 'NaN'
    Year_Birth: int = 'NaN'
    Education : object = 'NaN'
    Marital_Status : object = 'NaN'
    Income: float = 'NaN'
    Kidhome : int = 'NaN'
    Teenhome : int = 'NaN'
    Dt_Customer : object = 'NaN'
    Recency : int = 'NaN'
    MntWines : int = 'NaN'
    MntFruits : int = 'NaN'
    MntMeatProducts : int = 'NaN'
    MntFishProducts : int = 'NaN'
    MntSweetProducts : int = 'NaN'
    MntGoldProds : int = 'NaN'
    NumDealsPurchases : int = 'NaN'
    NumWebPurchases : int = 'NaN'
    NumCatalogPurchases : int = 'NaN'
    NumStorePurchases : int = 'NaN'
    NumWebVisitsMonth : int = 'NaN'
    AcceptedCmp3 : int = 'NaN'
    AcceptedCmp4 : int = 'NaN'
    AcceptedCmp5 : int = 'NaN'
    AcceptedCmp1 : int = 'NaN'
    AcceptedCmp2 : int = 'NaN'
    Complain : int = 'NaN'
    Z_CostContact : int = 'NaN'
    Z_Revenue : int = 'NaN'
    Response : int = 'NaN'

