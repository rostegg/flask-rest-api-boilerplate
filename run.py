import os
from app import create_app
from app.api import api_v1

app = create_app(os.getenv('FLASK_CONFIG_TYPE') or 'dev')
app.register_blueprint(api_v1)

if __name__ == '__main__':
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get("PORT", 5000))

    app.run(host=host, port=port)