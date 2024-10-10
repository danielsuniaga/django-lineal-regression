# apis/urls.py
from django.urls import path
from .views import DataView,OptimalPriceView  # Asegúrate de importar la vista correctamente

urlpatterns = [

    path('check-data/', DataView.as_view()),  
    path('optimal-price/', OptimalPriceView.as_view(), name='optimal-price')

]
