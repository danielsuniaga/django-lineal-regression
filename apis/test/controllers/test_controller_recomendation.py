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
            "Prod_year": 2019,
            "Engine_volume": 2.0,
            "Mileage": 50000,
            "Cylinders": 4,
            "Gear_box_type": "Automatic",
            "Drive_wheels": "FWD",
            "Budget": 20000
        }

        result = self.controller.get_recommendations(data)

        print(result)