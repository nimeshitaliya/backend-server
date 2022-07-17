from flask_restful import Api
from app import flaskAppInstance
from .ProjectAPI import ProjectAPI, ProjectAPI1



restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(ProjectAPI, "/")
restServerInstance.add_resource(ProjectAPI1,"/page/message")
