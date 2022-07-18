from flask_restful import Resource
import logging as logger

class ProjectAPI(Resource):

    def get(self):
        logger.debug("Inside the post method of Task")
        projectDetails = {
            "healthcheck" : "ok"
        }
        return projectDetails,200

class ProjectAPI1(Resource):

    def get(self):
        logger.debug("Inside the post method of Task")
        projectDetails = {
            "message" : "Hi"
        }
        return projectDetails,200
