import csv
import re

class User:
    def __init__(self, user_id, username, first_name):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name

    def get_info(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "first_name": self.first_name
        }

    def update_username(self, new_username):
        self.username = new_username

    def __str__(self):
        return f"{self.first_name} (@{self.username})"

    def normalize_phone(self, phone):
        digits = re.sub(r"\D", "", phone)
        if len(digits) == 10:
            digits = "7" + digits
        if len(digits) == 11 and digits.startswith("8"):
            digits = "7" + digits[1:]
        if len(digits) != 11 or not digits.startswith("7"):
            return None
        return "+" + digits

    def load_contacts(self, file_path):
        students = []
        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                students.append(row)
        return students

    def find_by_phone(self, phone, file_path):
        phone = self.normalize_phone(phone)
        if phone is None:
            return None
        students = self.load_contacts(file_path)
        for student in students:
            student_phone = self.normalize_phone(student["phone"])
            if phone == student_phone:
                return student
        return None