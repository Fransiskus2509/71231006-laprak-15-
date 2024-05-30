import re
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=8))
    return password

file_path = input("Masukkan path file: ")

try:
    with open(file_path, 'r') as file:
        text = file.read()
        pattern = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"
        matches = re.findall(pattern, text)

        for match in matches:
            username, domain = match.split('@')
            password = generate_password()
            print(f"{match} username: {username} , password: {password}")

except FileNotFoundError:
    print("File tidak ditemukan.")
