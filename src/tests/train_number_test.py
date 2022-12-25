import unittest
import requests
from repositories.train_repository import TrainRepository


class TestTrainnumber(unittest.TestCase):
   
    def setUp(self):
        self.train_repository = TrainRepository()