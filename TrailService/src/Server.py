from db.DBHandler import DBHandler
from config_utils.YAMLConfigReader import YAMLConfigReader
from api.Api import app, register_routes

config_reader = YAMLConfigReader('/app/config/config.yaml')
config_reader.read_yaml()
config_path = config_reader.get_dbfile_path()

db_handler = DBHandler(config_path)

register_routes(db_handler)

if __name__ == "__main__":
    print("NFO: starting the app")
    app.run(debug=False)  