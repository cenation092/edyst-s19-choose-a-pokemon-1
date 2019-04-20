#imports the required modules Flask,json
from flask import Flask
import json

app = Flask(__name__)

#handels the wrong url constructions.
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")

#main route for the api call i.e api/pokemon 
@app.route('/api/pokemon')
def home():
    
    data=["bulbasaur","charmander", "squirtle"]
    data={"pokemon":data}#dict that has the pokemon data
    return json.dumps(data)#dict converted to json format using dumps method.

if __name__ == '__main__':
    app.run(port=8006,debug=True)#check out the port in which app runs.

