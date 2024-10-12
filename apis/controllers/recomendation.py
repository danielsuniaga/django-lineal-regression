
import apis.services.lineal_regression as cases_lineal_regression

import apis.services.data as cases_data

class controller_recomendation: 

    services_data = None

    services_lineal_regression = None

    model = None
    
    features = None

    def __init__(self):

        self.init_features()

        self.services_data = cases_data.cases_data()

        self.services_data.load_label_encoder()

        self.services_lineal_regression = cases_lineal_regression.cases_lineal_regression()

        self.model = self.services_lineal_regression.load_model()

    def init_features(self):

        self.features = ['Manufacturer', 'Prod. year', 'Engine volume', 'Mileage', 
                         'Cylinders', 'Gear box type', 'Drive wheels']
        return True

    def get_budget(self,data):

        return data.get("Budget")
    
    def format_data(self, data):

        return {
            "Manufacturer": data.get("Manufacturer"),
            "Prod. year": data.get("Prod_year"),
            "Engine volume": data.get("Engine_volume"),
            "Mileage": data.get("Mileage"),
            "Cylinders": data.get("Cylinders"),
            "Gear box type": data.get("Gear_box_type"),
            "Drive wheels": data.get("Drive_wheels"),
            "Budget": data.get("Budget")
        }
    
    def apply_label_encoding(self, df):

        return self.services_data.apply_label_encoding(df)
    
    def generate_dataframe(self, data):

        return self.services_data.generate_dataframe(data)
    
    def load_all_cars(self):

        return self.services_data.load_csv_debug()
    
    def filter_cars(self, df, cars_df):


        filtered_cars = cars_df[
            (cars_df['Manufacturer'] == df['Manufacturer'].iloc[0]) &
            (cars_df['Prod. year'] == df['Prod. year'].iloc[0]) &
            (cars_df['Engine volume'] == df['Engine volume'].iloc[0]) &
            (cars_df['Cylinders'] == df['Cylinders'].iloc[0]) &
            (cars_df['Gear box type'] == df['Gear box type'].iloc[0]) &
            (cars_df['Drive wheels'] == df['Drive wheels'].iloc[0]) &
            (cars_df['Price'] <= df['Budget'].iloc[0])
        ]
        
        return filtered_cars
    
    def predict_price(self, df):

        df_encoded = self.apply_label_encoding(df)

        predicted_price = self.services_lineal_regression.get_model_predict(self.model, df_encoded)

        return predicted_price
    
    def predict_price_for_cars(self, cars_df):

        cars_df_encoded = self.apply_label_encoding(cars_df[self.features])

        cars_df['Predicted Price'] = self.services_lineal_regression.get_model_predict(self.model, cars_df_encoded)

        return cars_df

    def get_recommendations(self,data):

        df = self.generate_dataframe(self.format_data(data))

        df = self.apply_label_encoding(df)

        cars_df = self.load_all_cars()

        filtered_cars = self.filter_cars(df, cars_df)

        if filtered_cars.empty:

            df_clean = df[self.features]

            predicted_price = self.services_lineal_regression.get_model_predict(self.model, df_clean)

            return [{"Manufacturer": data["Manufacturer"], "Predicted Price": predicted_price}]

        filtered_cars_with_price = self.predict_price_for_cars(filtered_cars)

        return filtered_cars_with_price.to_dict(orient='records')
     
