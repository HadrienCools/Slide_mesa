#from app import app
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return "index de l'application de creation de slides -> SLIDE_MESA"