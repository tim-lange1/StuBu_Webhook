from flask import Flask
from views import views
import os

app = Flask(__name__)


if __name__ == "__main__":
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.register_blueprint(views)
    app.run(debug=True)