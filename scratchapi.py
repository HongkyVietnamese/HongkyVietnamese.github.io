from flask import Flask
import requests
from os import environ

app = Flask('')

@app.route('/')
def home():
  return {'status': 'up'}

@app.route('/projectstats/<int:project_id>')
def projectstats(project_id):
    ser_res = requests.request('get', f'https://api.scratch.mit.edu/projects/{project_id}')
    return ser_res.json()

@app.route('/userstats/<string:username>')
def userstats(username):
    ser_res = requests.request('get', f'https://api.scratch.mit.edu/users/{username}')
    return ser_res.json()

app.run(host=environ['IP'], port=environ['PORT'])
