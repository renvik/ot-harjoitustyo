import requests

class TrainRepository:
    """class responsible for the https-request
    """

    def get_train_data(self, train_number, departure_date):
        """_summary_

        Args:
            train_number: train number that is a argument in the request
            departure_date: departure date of the train """

        train_data = requests.get(
            f'https://rata.digitraffic.fi/api/v1/trains/{departure_date}/{train_number}')
        print(train_data.status_code)
        print(train_data.json())

        return train_data.json()
