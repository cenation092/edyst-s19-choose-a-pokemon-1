from flask import *
import os

app = Flask(__name__)
@app.context_processor
def override_url_for():
    
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        print(values,filename,app.root_path)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/api/pokemon')
def home():
    return render_template("gun.html")
if __name__ == '__main__':
    app.run(port=8006,debug=True)

