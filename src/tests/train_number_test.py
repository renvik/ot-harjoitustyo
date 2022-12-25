import unittest
import requests
from repositories.train_repository import TrainRepository


class TestTrainnumber(unittest.TestCase):
   
    def setUp(self):
        self.train_repository = TrainRepository()

    # tests that the api response status code is 200 
    def test_api_response(self):
        train_data = requests.get(
            f'https://rata.digitraffic.fi/api/v1/trains/2022-12-24/1')
        response = print(train_data.status_code)
        self.assertEqual(str(response), "200")

