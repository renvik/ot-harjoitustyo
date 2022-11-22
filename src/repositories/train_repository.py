import requests

class Trainrepository:

    def get_train():

        r = requests.get('https://rata.digitraffic.fi/api/v1/trains/2017-01-01/1')
        print(r.status_code)
        print(r.json())