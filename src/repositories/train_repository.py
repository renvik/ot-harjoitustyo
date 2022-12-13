from datetime import date
import json
import requests

# pitäisikö luokassa olla myös konstruktori??
class TrainRepository:
    """class responsible for the https-request
    """

    def get_train_data(self, train_number):
        """_summary_

        Args:
            train_number: user input that is a argument in the request"""
        today = date.today()
        print(today)
        train_data = requests.get(
            f'https://rata.digitraffic.fi/api/v1/trains/{today}/{train_number}')
        #status = r.status_code
        print(train_data.status_code)
        print(train_data.json())

        return train_data.json()

    def get_all_train_stations(self, train_number):
        """returns specified values from the json-data

        Args:
            train_number: user input that is a argument in the request

        Returns:
            specified values from the json-data
        """
        return self.get_train_data(train_number).json()[0]["timeTableRows"][0]["stationShortCode"]
#for testing:
#t = TrainRepository()
#t.get_all_train_stations(1)
#print(t.get_all_train_stations(1))
#train_repository = TrainRepository()
