import os
from app import create_app
from app.api import api_v1
from waitress import serve

app = create_app(os.getenv('FLASK_CONFIG_TYPE') or 'dev')
app.register_blueprint(api_v1)

if __name__ == '__main__':
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get("PORT", 5000))

    serve(app, host=host, port=port) if (os.getenv('FLASK_CONFIG_TYPE') == 'prod') else app.run(host=host, port=port)