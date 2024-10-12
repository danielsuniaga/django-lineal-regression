from unittest import TestCase, mock

import apis.controllers.recomendation as controller_recomendation

class TestControllerRecomendation(TestCase):

    mock_cursor = None

    controller = None

    def setUp(self): 

        self.mock_cursor = mock.MagicMock()

        self.controller = controller_recomendation.controller_recomendation()

    def test_get_recomendation(self):

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

        result = self.controller.get_recommendations()

        print(result)