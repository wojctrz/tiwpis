

class Controller:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate_output(self, error):
        pass