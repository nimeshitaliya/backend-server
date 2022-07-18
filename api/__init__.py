from flask_restful import Api
from app import flaskAppInstance
from .ProjectAPI import ProjectAPI, ProjectAPI1, ProjectAPI2



restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(ProjectAPI, "/")
restServerInstance.add_resource(ProjectAPI1,"/page/message")
restServerInstance.add_resource(ProjectAPI2,"/tab/message")
