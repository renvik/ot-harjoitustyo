from datetime import date
import requests
import json

# this class is responsible for the https-request (fetching the train information)
class TrainRepository:
    # parametrisointi: pvm, junannumero - nämä servicelle ja tämä kutsuu sitä
    def get_train_data(self, train_number):
        today = date.today()
        print(today)
        train_data = requests.get(
            f'https://rata.digitraffic.fi/api/v1/trains/{today}/{train_number}')
        #status = r.status_code
        print(train_data.status_code)
        print(train_data.json())

        return train_data

    def get_all_train_stations(self, train_number):
        return self.get_train_data(train_number).json()[0]["timeTableRows"][0]["stationShortCode"]

t = TrainRepository() # creates object with a name t?
t.get_all_train_stations(1) # calls method
print(t.get_all_train_stations(1)) # fetches all train stations for a train number 1

train_repository = TrainRepository() # does what?