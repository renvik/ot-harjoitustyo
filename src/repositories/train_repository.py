from datetime import date
import requests


class Trainrepository:

    # parametrisointi: pvm, junannumero - nämä servicelle ja tämä kutsuu sitä
    def get_train(self, train_number):
        today = date.today()
        print(today)
        r = requests.get(
            f'https://rata.digitraffic.fi/api/v1/trains/{today}/{train_number}')
        print(r.status_code)
        print(r.json())
