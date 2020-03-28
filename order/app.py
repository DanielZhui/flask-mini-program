from flask import Flask
from index import route

app = Flask(__name__)
app.register_blueprint(route, url_prefix='/api')

@app.route('/')
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run()