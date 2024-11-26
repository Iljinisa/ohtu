from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        
        if (self.validate(username, password)):

            user = self._user_repository.create(
                User(username, password)
            )
            return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Username must be at least 3 characters long and contain only lowercase letters")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already taken")

        if len(password) < 8 or password.isalpha():
            raise UserInputError("Password must be at least 8 characters long and contain at least one non-letter character")
        
        return True
