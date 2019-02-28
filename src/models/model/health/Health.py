from json import dumps


class Health:

    def __init__(self):
        self.project = "User Management"
        self.status = "UP"

    def __str__(self):
        return dumps(Health().__dict__)
