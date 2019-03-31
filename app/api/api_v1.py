import json
from flask import (
    Blueprint
)
from app.api.utils import response

JSON_MIME_TYPE = 'application/json'

test_response = [{
    'id': 1,
    'message': 'Hello'
}]

api_v1 = Blueprint(name='api_v1', import_name=__name__, url_prefix="/api/v1.0")


@api_v1.route('/test',methods=['GET'])
def test_result():
    return response(200,test_response)