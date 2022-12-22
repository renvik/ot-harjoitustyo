import unittest
from repositories.train_repository import TrainRepository


class TestTrainnumber(unittest.TestCase):
   
    def setUp(self):
        self.train_repository = TrainRepository()

    # tests that the api response status code is 200 
    def test_api_response(self):
        request = self.train_repository.get_train_data(1, 2022-12-22)
        response = request.status_code
        self.assertEqual(str(response), "200")

