class User(dict):
    def __init__(self, *args):
        self.uid = args[0]
        self.first_name = args[1]
        self.last_name = args[2]
        self.email = args[3]
        self.phone_number = args[4]
        self.login = args[5]
        self.password = args[6]
        self.user_type = args[7]
        self.documents = args[8]