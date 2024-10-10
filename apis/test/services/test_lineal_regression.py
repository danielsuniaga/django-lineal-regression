from unittest import TestCase, mock

import apis.services.lineal_regression as cases_lineal_regression

class TestServicesLinealRegression(TestCase):

    mock_cursor = None

    services = None

    def setUp(self): 

        self.mock_cursor = mock.MagicMock()

        self.services = cases_lineal_regression.cases_lineal_regression()
    
    def test_generate_training(self):

        result = self.services.generate_training()

        print(result)