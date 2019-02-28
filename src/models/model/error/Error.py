class Error:

    def __init__(self, message: str):
        self.__message = message

    @property
    def message(self):
        return self.__message

    def to_dict(self):
        return {
            "error": self.message
        }
