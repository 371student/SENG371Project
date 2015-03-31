import bottle
import json
from bottle.ext.mongo import MongoPlugin
import os
from bson.json_util import dumps


app = bottle.Bottle()
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
plugin = MongoPlugin(uri='mongodb://%s:%s@ds031278.mongolab.com:31278/seng371'%(db_user, db_pass), db="seng371", json_mongo=True)
app.install(plugin)

@app.get('/')
def index():
    return bottle.static_file("index.html",root="./")

@app.get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='./css')

@app.get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='./images')

@app.get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return bottle.static_file(filename, root='./js')

@app.get('/fonts/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return bottle.static_file(filename, root='./fonts')

"""
Post to this url to add a git repository to the queue
{
  "url": "<git url>",
}
"""
@app.post('/api/add')
def add_repo(mongodb):
  data = bottle.request.json
  if mongodb['repos'].find({'url': data['url']}).count() != 0:
    return
  else:
    mongodb['repos'].insert({'url': data['url'], 'status': 'queued', 'data': []})

"""
Get this url to get all repositories in the db
"""
@app.get('/api/repos')
def get_repos(mongodb):
  return dumps(mongodb['repos'].find())

# Expose WSGI app
application = app
