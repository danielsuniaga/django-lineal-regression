from decouple import config

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

class cases_eda:

    name_dataset = None

    route_price_with_brand_max = None

    def __init__(self):

        self.init_name_dataset()

        self.init_route_price_with_data_max()

    def init_route_price_with_data_max(self):

        self.route_price_with_brand_max = config("ROUTE_EDA_PRICE_WITH_BRAND_MAX")

    def get_route_price_with_data_max(self):

        return self.route_price_with_brand_max

    def init_name_dataset(self):

        self.name_dataset = config("NAME_DATASET")

        return True
    
    def get_name_dataset(self):

        return self.name_dataset
    
    def get_csv(self):

        return pd.read_csv(self.get_name_dataset())

    def check_price_max(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=False)

        print("Los 10 autos más caros son:")

        for index, row in df_sorted.head(10).iterrows():

            print(f"Marca: {row['Manufacturer']}, Precio: {row['Price']}, Modelo: {row['Model']}, Año: {row['Prod. year']}")

        return True
    
    def check_price_min(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=True)

        print("Los 10 autos más baratos son:")

        for index, row in df_sorted.head(10).iterrows():

            print(f"Marca: {row['Manufacturer']}, Precio: {row['Price']}, Modelo: {row['Model']}, Año: {row['Prod. year']}")

        return True

    def check_price_with_brand_max(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=False).head(10)

        plt.figure(figsize=(12, 6))

        sns.barplot(x='Manufacturer', y='Price', data=df_sorted)

        plt.title('Relación entre Precio y Marca de los 10 Vehículos más Caros')

        plt.xlabel('Marca')

        plt.ylabel('Precio')

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(self.get_route_price_with_data_max())

        plt.close()

        return True
    
    def check_price_with_brand_min(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=True).head(10)

        plt.figure(figsize=(12, 6))

        sns.barplot(x='Manufacturer', y='Price', data=df_sorted)

        plt.title('Relación entre Precio y Marca de los 10 Vehículos más Baratos')

        plt.xlabel('Marca')

        plt.ylabel('Precio')

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(self.get_route_price_with_data())  

        plt.close()  

        return True

