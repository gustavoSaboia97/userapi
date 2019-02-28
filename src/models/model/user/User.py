class User:

    def __init__(self, user_id: str, name: str):
        self.__user_id = user_id
        self.__name = name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @user_id.setter
    def user_id(self, new_user_id):
        self.__user_id = new_user_id

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name
        }
