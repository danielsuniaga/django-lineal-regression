import pandas as pd

from decouple import config

from sklearn.preprocessing import LabelEncoder
class cases_data:

    name_dataset = None

    name_dataset_debug = None

    column_to_remove = None

    def __init__(self):

        pass

    def init_name_dataset_debug(self):

        self.name_dataset_debug = config("DEBUG_NAME_DATASET")

        return True
    
    def get_name_dataset_debug(self):

        return self.name_dataset_debug

    def init_column_to_remove(self):

        self.column_to_remove = ['ID', 'Levy', 'Doors', 'Wheel', 'Color', 'Airbags']

        return True

    def get_column_to_remove(self):

        return self.column_to_remove

    def init_name_dataset(self):

        self.name_dataset = config("NAME_DATASET")

    def get_name_dataset(self):

        return self.name_dataset
    
    def check_cell_null(self,dataset):

        return dataset.isnull().sum()
    
    def get_columns(self,dataset):

        return dataset.columns
    
    def debug_dataset(self,dataset):

        self.init_column_to_remove()

        return dataset.drop(columns=self.get_column_to_remove())
    
    def save_dataset(self,dataset):

        self.init_name_dataset_debug()

        dataset.to_csv(self.get_name_dataset_debug(), index=False)

        return True
    
    def apply_label_encoding(df):

        le = LabelEncoder()

        categorical_cols = df.select_dtypes(include=['object']).columns

        for col in categorical_cols:

            df[col] = le.fit_transform(df[col])

        return df

    def check_data(self):

        self.init_name_dataset()

        df = pd.read_csv(self.get_name_dataset())

        le = LabelEncoder()

        print(df.head())

        print(self.check_cell_null(df))

        print(self.get_columns(df))

        self.save_dataset(self.apply_label_encoding(self.debug_dataset(df)))

        return True