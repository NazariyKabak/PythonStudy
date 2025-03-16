import random
import string

def random_password():
    password = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    return password
