#
#   PYTHON-SERVER für SE2P
#
#   HAWA iCYCLE
#

from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import g

import testmodul
import fileaccess as fa

app = Flask(__name__)

test = testmodul.testmodul()

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.errorhandler(500)
def special_exception_handler(error):
    return 'Database connection failed', 500

@app.route('/')
def hello_world():
    css=fa.listFiles(dir="/static/css/",ext=["css"],name="")
    
    pluginjs=fa.listFiles(dir="/static/js/plugins/",ext=[".js"],name="")
    basejs=("/static/js/jquery2.min.js","/static/js/bootstrap.min.js")
    return render_template('index.html', data={'css':css,'js':basejs,'pluginjs':pluginjs})

    
if __name__ == '__main__':
    app.run(debug=True)

