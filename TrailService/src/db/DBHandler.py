from db.DBReader import DBReader

class DBHandler:
    _instance = None

    def __new__(cls, db_file):
        if cls._instance is None:
            cls._instance = super(DBHandler, cls).__new__(cls)
            if not (cls._instance._initialize(db_file)):
                return None
            
        return cls._instance

    def _initialize(self, db_file_path):
        self.db_reader = DBReader(db_file_path)
        if not self.db_reader.read_csv():
            return False

        self.data = self.db_reader.get_data()
        return True

    def get_filtered_data(self, predicates):
        filtered_data = self.data
        for predicate in predicates:
            filtered_data = [row for row in filtered_data if predicate(row)]
        return filtered_data