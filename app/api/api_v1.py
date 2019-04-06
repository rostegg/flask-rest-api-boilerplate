import json
from flask import (
    Blueprint
)
from app.api.utils import response
from app.api.cache import cache


test_response = [{
    'id': 1,
    'message': 'Hello'
}]

api_v1 = Blueprint(name='api_v1', import_name=__name__, url_prefix="/v1")

@api_v1.route('/test',methods=['GET'])
@cache.cached(timeout=60)
def test_result():
    return response(200,test_response)