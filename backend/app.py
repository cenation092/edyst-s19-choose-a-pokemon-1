
from flask import Flask
import json

app = Flask(__name__)

@app.errorhandler(404)
def unknown(a):
    return "Please check your url and try again."

@app.route('/api/pokemon')
def home():
    data=["bulbasaur","charmander", "squirtle"]
    data={"pokemon":data}
    return json.dumps(data)

if __name__ == '__main__':
    app.run(port=8006,debug=True)

