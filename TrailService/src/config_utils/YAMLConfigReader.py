import yaml
import os

class YAMLConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def read_yaml(self):
        if not os.path.exists(self.file_path):
            print(f"ERROR: Configuration file: {self.file_path} does not exist.")
            return False
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
        return True

    def get_dbfile_path(self):
        return self.config.get('config', {}).get('dbFilePath')

