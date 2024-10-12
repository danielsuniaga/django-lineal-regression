# Django imports
from django.shortcuts import render
from django.db import connection

# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import apis.services.data as case_data
import apis.controllers.optimalprice as controller_optimal_price
import apis.controllers.priceevaluation as controller_price_evaluation
import apis.controllers.recomendation as controller_recomendation

class DataView(APIView):

    data = None

    def __init__(self):

        self.data = case_data.cases_data()

    def post(self, request, format=None):

        return Response(self.data.check_data())
    
class OptimalPriceView(APIView):

    controller = None

    def __init__(self):

        self.controller = controller_optimal_price.controller_optimal_price()
    
    def post(self, request):

        data = request.data

        return Response(self.controller.generate_optimal_price(data))
    
class PriceEvaluationView(APIView):

    controller = None

    def __init__(self):

        self.controller = controller_price_evaluation.controller_price_evaluation()
    
    def post(self, request):

        data = request.data

        return Response(self.controller.evaluate_price(data))
    
class RecomendationView(APIView):

    controller = None

    def __init__(self):

        self.controller = controller_recomendation.controller_recomendation()

    def post(self, request):

        return Response(self.controller.get_recommendations())

