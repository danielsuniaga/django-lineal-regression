# API de Valoración de Vehículos

## Descripción del Proyecto

La API de Valoración de Vehículos proporciona servicios para estimar precios óptimos de vehículos, evaluar precios propuestos por los vendedores y recomendar vehículos basados en especificaciones y presupuestos. Este sistema está diseñado para ayudar a los usuarios a tomar decisiones informadas al comprar o vender vehículos.

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python
- **Framework**: Flask
- **Bibliotecas**:
  - Pandas (para manejo de datos)
  - Scikit-learn (para modelos de Machine Learning)
  - NumPy (para operaciones numéricas)
- **Formato de Datos**: JSON
- **Base de Datos**: CSV (para el almacenamiento de datos de vehículos)

## Endpoints

### 1. Precio Óptimo

**Método**: POST  
**Ruta**: `/optimal-price`  
**Descripción**: Dada una serie de características del vehículo, retorna el precio óptimo estimado.

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


### 2. Evaluación del Precio

**Método**: POST  
**Ruta**: `/evaluate-price`  
**Descripción**: Evalúa el precio propuesto por un vendedor y sugiere un precio razonable basado en el análisis de las características del vehículo.

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
`

### 3. Recomendación de Compra

**Método**: POST  
**Ruta**: `/recommendation`  
**Descripción**: Dado un presupuesto y especificaciones deseadas, sugiere el mejor vehículo disponible en función de los datos.

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

## Instalación

Para ejecutar esta API localmente, sigue estos pasos:

1. **Clona el repositorio**:

   ```bash
   git clone <https://github.com/danielsuniaga/django-lineal-regression/>
   cd <directorio-del-repositorio>
