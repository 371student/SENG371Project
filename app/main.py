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
    return bottle.static_file("index.html",root="public/app/views")

@app.get('/app/views/pages/<filename:re:.*\.html>')
def pages(filename):
    return bottle.static_file(filename, root='public/app/views/pages')

@app.get('/app/views/pages/<filename:re:.*\.json>')
def json(filename):
    return bottle.static_file(filename, root='public/app/views/pages')

@app.get('/assets/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='public/assets/css')

@app.get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='public/assets/images')

@app.get('/assets/libs/<filename:re:.*\.js>')
def javascript_libs(filename):
    return bottle.static_file(filename, root='public/assets/libs')

@app.get('/app/controllers/<filename:re:.*\.js>')
def javascript_assets(filename):
    return bottle.static_file(filename, root='public/assets/js')

@app.get('/app/<filename:re:.*\.js>')
def javascript_app(filename):
    return bottle.static_file(filename, root='public/app')

@app.get('/app/controllers/<filename:re:.*\.js>')
def controllers(filename):
    return bottle.static_file(filename, root='public/app/controllers')

@app.get('/app/services/<filename:re:.*\.js>')
def services(filename):
    return bottle.static_file(filename, root='public/app/services')


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
