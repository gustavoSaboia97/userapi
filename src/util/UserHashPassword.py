import hashlib


class UserHashPassword:

    @staticmethod
    def hash_password(password: str):
        hash_control = hashlib.sha256()
        hash_control.update(bytes(password, "utf-8"))
        return hash_control.hexdigest()
