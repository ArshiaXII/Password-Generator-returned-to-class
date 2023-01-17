import random
import string

class PasswordGenerator:
    def __init__(self, length, special_characters=False):
        self.length = length
        self.special_characters = special_characters
        self.allowed_characters = string.ascii_letters + string.digits
        if special_characters:
            self.allowed_characters += string.punctuation

    def generate_password(self):
        password = ""
        for i in range(self.length):
            password += random.choice(self.allowed_characters)
        return password

pg = PasswordGenerator(8, True)
print("Generated password: ", pg.generate_password())
