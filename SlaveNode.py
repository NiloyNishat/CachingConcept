from flask import Flask
from flask import request
from collections import defaultdict

app = Flask(__name__)

arr_website = defaultdict(int)


@app.route('/hello')
def getWebsiteData():
    website = request.args.get('website')
    arr_website[website] += 1
    return arr_website


app.run(host='0.0.0.0', port=81)
