class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = {'password': password, 'email': None}

    def authenticate_user(self, username, password):
        if username not in self.users:
            return False
        return self.users[username]['password'] == password

    def update_user_email(self, username, email):
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        self.users[username]['email'] = email

    def get_user_email(self, username):
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username]['email']