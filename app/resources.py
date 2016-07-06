from flask_restful import Resource
from app import controllers as app_controllers


class HelloWorld(Resource):

    def get(self):
        print "in get method"
        return app_controllers.hello_world()

    def post(self):
        return app_controllers.post()
