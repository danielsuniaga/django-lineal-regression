from decouple import config

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error, r2_score

import pickle

import os

class cases_lineal_regression:

    name_dataset = None

    model = None

    def __init__(self):

        self.init_name_dataset()

    def init_name_dataset(self):

        self.name_dataset = config("DEBUG_NAME_DATASET")

    def get_name_dataset(self):

        return self.name_dataset
    
    def get_csv(self):

        return pd.read_csv(self.get_name_dataset())
    
    def preprocess_data(self,df):

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        
        features = ['Manufacturer', 'Prod. year', 'Engine volume', 'Mileage', 'Cylinders', 'Gear box type', 'Drive wheels']
        
        df = df.dropna(subset=features + ['Price'])  
        
        X = df[features]

        y = df['Price']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):

        self.model = LinearRegression()  
        
        self.model.fit(X_train, y_train)  
        
        return self.model
    
    def evaluate_model(self, X_test, y_test):

        y_pred = self.model.predict(X_test) 
        
        mae = mean_absolute_error(y_test, y_pred)
        
        r2 = r2_score(y_test, y_pred)
        
        return mae, r2
    
    def generate_training(self):

        df = self.get_csv()

        X_train, X_test, y_train, y_test = self.preprocess_data(df)

        self.train_model(X_train, y_train)

        mae, r2 = self.evaluate_model(X_test, y_test)
        
        print(f'MAE: {mae}, R2 Score: {r2}')

        return True