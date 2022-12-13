from repositories.train_repository import TrainRepository
# 
class TrainService:
    """The class is responsible for the app logic
    Attributes: 
        train_number: number of the train
    """
    def __init__(self):
        """constructor creates TrainRepository
        """
        self.train_repository = TrainRepository()

    def get_train(self, train_number):
        """passes the train number to the TrainRepository

        Args:
            train_number: a value that user gives
        """
        self.train_repository.get_train_data(train_number)
