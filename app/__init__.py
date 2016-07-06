"""App init."""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.resources import HelloWorld

app = Flask(__name__)
api = Api(app)

app.config.from_object('settings')

db = SQLAlchemy(app)

if __name__ == '__main__':
	app.run()


api.add_resource(HelloWorld, '/')

