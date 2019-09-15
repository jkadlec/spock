from server import create_app, init_app
from config import Config as conf

app = create_app(conf)
with app.app_context():
    init_app(app)
