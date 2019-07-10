import flask
from flask import request
from collections import defaultdict
import csv

app = flask.Flask(__name__)

arr_website = defaultdict(int)


def readFromFile():
    with open('WebsiteLists.csv', mode='r') as file:
        reader = csv.reader(file)
        arr = {rows[0]: rows[1] for rows in reader}
    file.close()
    return arr


def writeInFile():
    with open('WebsiteLists.csv', 'w') as f:
        for key in arr_website.keys():
            f.write("%s,%s\n" % (key, arr_website[key]))
    f.close()


@app.route('/hello')
def getWebsiteData():
    website = request.args.get('website')
    if website in arr_website:
        val = int(arr_website[website])
        arr_website[website] = val+1
    else:
        arr_website[website] = 1
    writeInFile()
    return arr_website


arr_website = readFromFile()
app.run(host='0.0.0.0', port=81)
