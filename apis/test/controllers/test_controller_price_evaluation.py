from unittest import TestCase, mock

import apis.controllers.priceevaluation as controller_price_evaluation

class TestControllerPriceEvaluation(TestCase):

    mock_cursor = None

    controller = None

    def setUp(self): 

        self.mock_cursor = mock.MagicMock()

        self.controller = controller_price_evaluation.controller_price_evaluation()

    def test_evaluate_model(self):
        
        data = {
            "Manufacturer": "Toyota",
            "Prod_year": 2018,
            "Engine_volume": 2.0,
            "Mileage": 50000,
            "Cylinders": 4,
            "Gear_box_type": "Automática",
            "Drive_wheels": "FWD",
            "Proposed_price": 150000
        }

        result = self.controller.evaluate_price(data)

        print(result)