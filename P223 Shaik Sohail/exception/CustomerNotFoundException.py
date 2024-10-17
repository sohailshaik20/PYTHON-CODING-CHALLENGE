class CustomerNotFoundException(Exception):
    def __init__(self, message="CustomerNotFoundException"):
        self.message = message
        super().__init__(self.message)