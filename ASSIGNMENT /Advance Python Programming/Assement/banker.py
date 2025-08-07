from user import User

class Banker(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
