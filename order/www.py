from app import app
from web.controllers.index import route_index


app.register_blueprint(route_index, url_prefix='/')