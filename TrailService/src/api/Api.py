from flask import Flask

app = Flask(__name__)

from api.GetTrail import register_get_routes

def register_routes(db_handler):
    register_get_routes(app, db_handler)
    