# apis/urls.py
from django.urls import path
from .views import DataView  # Asegúrate de importar la vista correctamente

urlpatterns = [

    path('check-data/', DataView.as_view()),  

]
