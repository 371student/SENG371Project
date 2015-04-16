import bottle
import json
from bottle.ext.mongo import MongoPlugin
import os
from bson.json_util import dumps
import requests
import re


app = bottle.Bottle()
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
plugin = MongoPlugin(uri='mongodb://%s:%s@ds031278.mongolab.com:31278/seng371'%(db_user, db_pass), db="seng371", json_mongo=True)
app.install(plugin)

@app.get('/')
def index():
    return bottle.static_file("index.html",root="public/app/views")

@app.get('/assets/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='public/assets/css')

@app.get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='public/assets/images')

@app.get('/assets/libs/<filename:re:.*\.js>')
def javascript_libs(filename):
    return bottle.static_file(filename, root='public/assets/libs')

@app.get('/app/<filename:re:.*\.js>')
def javascript_app(filename):
    return bottle.static_file(filename, root='public/app')

@app.get('/app/views/pages/<filename:re:.*\.html>')
def pages(filename):
    return bottle.static_file(filename, root='public/app/views/pages')

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
  #Make sure the repo is not already in the db
  if mongodb['repos'].find({'url': data['url']}).count() != 0:
    return
  else:
    #Make sure the url is a properly formatted github url
    temp = re.match('https://github.com/([a-zA-Z0-9-]*)/([a-zA-Z0-9-]*)\.git', data['url'])
    if temp != None:
      #Make sure the url points to a real repository
      result = requests.get('https://github.com/%s/%s'%(temp.group(1), temp.group(2)))
      if result.status_code == 200:
        mongodb['repos'].insert({'url': data['url'], 'status': 'queued', 'data': []})

"""
Get this url to get all repositories in the db
"""
@app.get('/api/repos')
def get_repos(mongodb):
  return dumps(mongodb['repos'].find())

@app.post('/api/repo')
def get_one_repo(mongodb):
  data = bottle.request.json
  return dumps(mongodb['repos'].find_one({'url': data['url']}))

# Expose WSGI app
application = app
