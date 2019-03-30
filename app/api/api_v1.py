import json
from flask import (
    Blueprint,
    Response,
    jsonify,
)

JSON_MIME_TYPE = 'application/json'

test_response = [{
    'id': 1,
    'message': 'Hello'
}]

api_v1 = Blueprint(name='api_v1', import_name=__name__, url_prefix="/api/v1.0")


@api_v1.route('/test',methods=['GET'])
def test_result():
    response = Response(
        json.dumps(test_response), status=200, mimetype=JSON_MIME_TYPE)
    return response