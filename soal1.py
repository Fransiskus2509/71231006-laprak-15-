import re
from datetime import datetime, date

file_path = input("Masukkan path file: ")

try:
    with open(file_path, 'r') as file:
        text = file.read()
        pattern = r"\d{4}-\d{2}-\d{2}"
        matches = re.findall(pattern, text)
        today = date.today()

        for match in matches:
            date_obj = datetime.strptime(match, "%Y-%m-%d").date()
            formatted_date = date_obj.strftime("%d-%m-%Y")
            difference = (today - date_obj).days
            print(f"{formatted_date} 00:00:00 selisih {difference} hari")

except FileNotFoundError:
    print("File tidak ditemukan.")
