from unittest import TestCase, mock

import apis.controllers.optimalprice as controller_optimal_price

class TestControllerOptimalPrice(TestCase):

    mock_cursor = None

    controller = None

    def setUp(self): 

        self.mock_cursor = mock.MagicMock()

        self.controller = controller_optimal_price.controller_optimal_price()

    def test_generate_optimal_price(self):

        data = {
            "Manufacturer": "Toyota",
            "Prod. year": 2018,
            "Engine volume": 2.0,
            "Mileage": 50000,
            "Cylinders": 4,
            "Gear box type": "Automática",
            "Drive wheels": "FWD"
        }



        result = self.controller.generate_optimal_price(data)

        print(result)
