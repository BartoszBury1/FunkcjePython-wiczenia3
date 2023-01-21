import random
import string

def generate_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    characters = lowercase + uppercase + digits + special
    min_length = 8

    password = ''.join(random.sample(characters,min_length))

    return password

print(generate_password())
    
   
    