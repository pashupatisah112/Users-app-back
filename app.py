from flask import Flask
from api import load_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
load_api(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)