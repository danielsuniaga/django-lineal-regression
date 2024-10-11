
import apis.services.lineal_regression as cases_lineal_regression

import apis.services.data as cases_data

class controller_price_evaluation: 

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
    
    def generate_dataframe(self, data):

        return self.services_data.generate_dataframe(data)
    
    def apply_label_encoding(self, df):

        return self.services_data.apply_label_encoding(df)
    
    def get_model_predict(self, df):

        return self.services_lineal_regression.get_model_predict(self.model, df)
    
    def format_data(self, data):

        return {
            "Manufacturer": data.get("Manufacturer"),
            "Prod. year": data.get("Prod_year"),
            "Engine volume": data.get("Engine_volume"),
            "Mileage": data.get("Mileage"),
            "Cylinders": data.get("Cylinders"),
            "Gear box type": data.get("Gear_box_type"),
            "Drive wheels": data.get("Drive_wheels")
        }

    def evaluate_price(self, data):

        df = self.generate_dataframe(self.format_data(data))

        df = df[self.features]

        df = self.apply_label_encoding(df)

        suggested_price = self.get_model_predict(df)

        proposed_price = data.get("Proposed_price")

        evaluation = {
            "Proposed price": proposed_price,
            "Suggested price": suggested_price,
            "Reasonable": suggested_price <= proposed_price
        }

        return evaluation
