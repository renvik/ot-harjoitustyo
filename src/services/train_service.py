from repositories.train_repository import TrainRepository
# The class is responsible for the app logic
class TrainService:
    def __init__(self):
        self.train_repository = TrainRepository()

    def get_train(self, train_number):
        self.train_repository.get_train_data(train_number)
        # tämän pitäisi palauttaa myös kutsun tulos (junaolio)
