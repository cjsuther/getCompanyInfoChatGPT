import logging
from os import environ as env
from dotenv import load_dotenv

class Base:
    def __init__(self, debug=False):
        load_dotenv()
        self.debug = (env['DEBUG'] == "true")
        logging.basicConfig(
            filename=env['LOG_FILE'],
            format=env['LOG_FORMAT'],
            datefmt=env['LOG_DATE_FORMAT'],
            level = logging.DEBUG if self.debug else logging.WARNING 
        )
        self.log = logging.getLogger('main').debug
        self.env = env
    
    def errorMessage(self, message, code=400):
        return {'status': 'error', 'code': code, 'message': message}

