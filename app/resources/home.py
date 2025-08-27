from flask import jsonify, Blueprint

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
  resp = jsonify("ok")
  resp.status_code = 200
  return resp