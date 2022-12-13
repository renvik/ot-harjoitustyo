import unittest
from repositories.train_repository import TrainRepository


class TestTrainnumber(unittest.TestCase):
    def setUp(self):
        self.train_repository = TrainRepository()
        print("set up goes here")

    # tests that api response status code is 200
    def test_api_response(self):
        kutsu = self.train_repository.get_train_data(1)
        vastaus = kutsu.status_code
        self.assertEqual(str(vastaus), "200")

