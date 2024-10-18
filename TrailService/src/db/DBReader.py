import csv
import os

class DBReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_csv(self):
        if not os.path.exists(self.file_path):
            print(f"ERROR: The file {self.file_path} does not exist.")
            return False
        
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append(row)
        return True

    def get_data(self):
        return self.data