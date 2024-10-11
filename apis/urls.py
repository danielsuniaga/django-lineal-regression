# apis/urls.py
from django.urls import path
from .views import DataView,OptimalPriceView,PriceEvaluationView,RecomendationView

urlpatterns = [

    path('check-data/', DataView.as_view()),  

    path('optimal-price/', OptimalPriceView.as_view(), name='optimal-price'),

    path('price-evaluation/', PriceEvaluationView.as_view(), name='price-evaluation'),

    path('recomendation/', RecomendationView.as_view(), name='recomendation')

]
