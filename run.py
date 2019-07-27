from flask import Flask
from flask_cors import CORS

from app.user import user
from app.rose import rose


app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": "*"}})   # 允许所有域名跨域
CORS(app, supports_credentials=True)

app.register_blueprint(user, url_prefix = '/user')
app.register_blueprint(rose, url_prefix = '/rose')


if __name__ == '__main__':
    app.run(debug=True)