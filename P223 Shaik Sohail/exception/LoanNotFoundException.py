
class LoanNotFoundException(Exception):
    def __init__(self, message="LoanNotFoundException"):
        self.message = message
        super().__init__(self.message)