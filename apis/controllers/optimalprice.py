import apis.services.lineal_regression as cases_lineal_regression

import apis.services.data as cases_data

class controller_optimal_price: 

    services_data = None

    services_lineal_regression = None

    model = None

    feature = None

    def __init__(self):

        self.init_feature()

        self.services_data = cases_data.cases_data()

        self.services_data.load_label_encoder()

        self.services_lineal_regression = cases_lineal_regression.cases_lineal_regression()

        self.model = self.services_lineal_regression.load_model()

        pass

    def init_feature(self):

        self.feature = ['Manufacturer', 'Prod. year', 'Engine volume', 'Mileage', 
                    'Cylinders', 'Gear box type', 'Drive wheels']
        
        return True
    
    def get_feature(self):

        return self.feature

    def generate_dataframe(self,data):
        
        return self.services_data.generate_dataframe(data)
    
    def apply_label_encoding(self,df):

        return self.services_data.apply_label_encoding(df)
    
    def get_model_predict(self,df):

        return self.services_lineal_regression.get_model_predict(self.model,df)
    
    def format_data(self,data):
        
        return {
            "Manufacturer": data.get("Manufacturer"),
            "Prod. year": data.get("Prod_year"),
            "Engine volume": data.get("Engine_volume"),
            "Mileage": data.get("Mileage"),
            "Cylinders": data.get("Cylinders"),
            "Gear box type": data.get("Gear_box_type"),
            "Drive wheels": data.get("Drive_wheels")
        }

    def generate_optimal_price(self, data):

        df = self.generate_dataframe(self.format_data(data))

        features = self.get_feature()

        df = df[features]

        df = self.apply_label_encoding(df)

        predicted_price = self.get_model_predict(df)

        return predicted_price
