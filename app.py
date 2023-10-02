from flask import Flask
from flask_cors import CORS
from models import db
from config import Config
from views import views_bp


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

app.register_blueprint(views_bp, url_prefix='/')  # Указывайте url_prefix, если необходимо


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)
