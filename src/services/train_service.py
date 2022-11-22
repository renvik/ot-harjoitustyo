from repositories.train_repository import Trainrepository 

class TrainService: 
    def __init__(self):
        self.train_repository=Trainrepository()
    def get_train(self, train_number):
        self.train_repository.get_train(train_number)
        # tämän pitäisi palauttaa myös kutsun tulos (junaolio)
