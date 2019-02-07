#!/usr/bin/env python

from flask import Flask, url_for, json, render_template
from flask import Response
from flask import request
from flask import jsonify, make_response
from flask_restful import reqparse

from random import randint

from itertools import cycle
import requests
import sys 
import snakes.plugins
import snakes.pnml
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *

# here we copy the content of the 'from.py' file to include the dynamically created resources

from discovery import discovery # used to apply the discovery algorithm on the created resource graphs using BFS or DFS
from graphs_sim import graphs_sim # used to create the simulated function/resource graphs


app = Flask(__name__)

# here we copy the content of the 'appregister.py' file to complete the inclusion of the dynamically created resources

app.register_blueprint(discovery, url_prefix='')
app.register_blueprint(graphs_sim, url_prefix='')

sys.setrecursionlimit(100000)

@app.route('/')
def homePage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(threaded=True)
    app.run(debug=True)
