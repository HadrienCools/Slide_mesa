from app.api import bp

@bp.route('/ack/<int:id>', methods=['GET'])
def get_ack(id):
    return("ack"+str(id))