from app import app
from web.controllers.index import route_index
from web.controllers.login import login_page


app.register_blueprint(route_index, url_prefix='/')
app.register_blueprint(login_page, url_prefix='/')