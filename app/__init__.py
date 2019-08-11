from app.slide_generation.slide_maker import slide_maker

#
from flask import Flask

class create_legacy_app:
    def __init__(self):
        #slide_object = slide_maker()
        print("fonction slide desactive")

#class create_app:
def create_app():
    app = Flask(__name__)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    #from app import routes
    return app
    
if __name__ == '__main__':
    pass