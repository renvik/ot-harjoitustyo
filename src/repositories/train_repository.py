#from datetime import date
import json
import requests

class TrainRepository:
    """class responsible for the https-request
    """

    def get_train_data(self, train_number, departure_date):
        """_summary_

        Args:
            train_number: train number that is a argument in the request
            departure_date: other argument in the request """

        train_data = requests.get(
            f'https://rata.digitraffic.fi/api/v1/trains/{departure_date}/{train_number}')
        print(train_data.status_code)      
        print(train_data.json())

        return train_data.json()

    def get_all_train_stations(self, train_number, departure_date):
        """returns specified values from the json-data

        Args:
            train_number: user input that is a argument in the request

        Returns:
            specified values from the json-data
        """
        return self.get_train_data(train_number, departure_date).json()[0]["timeTableRows"][0]["stationShortCode"]
#for testing:
# t = TrainRepository()
# t.get_all_train_stations(1, 2022-12-22)
# print(t.get_all_train_stations(1, 2022-12-22))
# train_repository = TrainRepository()
