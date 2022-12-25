from repositories.train_repository import TrainRepository

class TrainService:
    """The class is responsible for the app logic
    Attributes:
        train_number: number of the train
        departuret_date: departure date of the train
    """
    def __init__(self):
        """constructor that creates TrainRepository
        """
        self.train_repository = TrainRepository()

    def get_train(self, train_number, departure_date):
        """passes the train number to the TrainRepository

        Args:
            train_number: a value that the user gives
            departure_date: a date that the user gives
        """
        return self.train_repository.get_train_data(train_number, departure_date)
