# Vehicle Valuation API

## Project Description

The Vehicle Valuation API provides services to estimate optimal vehicle prices using a machine learning model, evaluate prices proposed by sellers, and recommend vehicles based on specifications and budgets. This system is designed to help users make informed decisions when buying or selling vehicles.

## Technologies Used

- **Programming Language**: Python
- **Framework**: Django
- **Libraries**:
  - Pandas (for data handling)
  - Scikit-learn (for Machine Learning models)
  - NumPy (for numerical operations)
- **Data Format**: JSON
- **Database**: CSV (for storing vehicle data)
- **Model**: pkl
- **Containerization**: Docker (used for packaging and deploying the application in a consistent environment)

## Endpoints

### 1. Optimal Price

**Method**: POST  
**Route**: `/optimal-price`  
**Description**: Given a series of vehicle characteristics, it returns the estimated optimal price.

```json
{
    "Manufacturer": "Toyota",
    "Prod_year": 2020,
    "Engine_volume": 2.0,
    "Mileage": 15000,
    "Cylinders": 4,
    "Gear_box_type": "Automatic",
    "Drive_wheels": "FWD"
}
```


### 2. Price Evaluation

**Method**: POST  
**Route**: `/evaluate-price 
**Description**: Evaluates the price proposed by a seller and suggests a reasonable price based on the analysis of the vehicle's characteristics.


```json
{
    "Manufacturer": "Honda",
    "Prod_year": 2019,
    "Engine_volume": 1.8,
    "Mileage": 20000,
    "Cylinders": 4,
    "Gear_box_type": "Manual",
    "Drive_wheels": "RWD",
    "Proposed_price": 20000
}
```

### 3. Purchase Recommendation

**Método**: POST  
**Ruta**: `/recommendation  
**Descripción**: Given a budget and desired specifications, it suggests the best available vehicle based on the data.

```json
{
    "Budget": 25000,
    "Manufacturer": "Ford",
    "Prod_year": 2021,
    "Engine_volume": 2.5,
    "Cylinders": 4,
    "Gear_box_type": "Automatic",
    "Drive_wheels": "AWD"
}

```

## Installation

To run this API locally, follow these steps:

1. **Clone the repository:**:

   ```bash
   git clone <https://github.com/danielsuniaga/django-lineal-regression/>
   cd <directorio-del-repositorio>

2. **Install the required dependencies:**:

   ```bash
   pip install -r requirements.txt