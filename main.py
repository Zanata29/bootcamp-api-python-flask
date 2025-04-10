from flask import Flask

app = Flask(__name__)

from swagger import swagger_ui_blueprint, SWAGGER_URL
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

from routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) 
