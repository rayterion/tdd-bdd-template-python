

from unittest import TestCase
from unittest.mock import patch

from core.apiCaller import ApiCaller

class TestApiCaller(TestCase):
    def setUp(self):
        self.api = ApiCaller()
    
    @patch('core.apiCaller.requests.get')
    def testGetApiRandomRunmbers(self, myMock):
        """ returns a json response without errors """
        jsonData = { "data": [1, 5, 4, 2] }
        
        myMock.return_value.status_code = 200
        myMock.return_value.json.return_value = jsonData
        response = self.api.getApiRandomNumbers()
        self.assertEqual(response, jsonData)

    @patch('core.apiCaller.requests.get')    
    def testGetApiRandomNumbersRaises(self, getFunc):
        """ returns a status of 400 on exceptions """
        getFunc.side_effect = Exception("Random exception")
        response = self.api.getApiRandomNumbers()
        self.assertEqual(response["status_code"], 400)

