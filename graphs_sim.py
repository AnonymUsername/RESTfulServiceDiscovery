#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import request
import requests

from SPARQLWrapper import SPARQLWrapper, JSON
from collections import OrderedDict 
from rdflib import Graph

import numpy as np
import os.path

graphres = Blueprint('graphres', __name__,)

@graphres.route('/fct', methods=["POST"]) # creation of function graphs
def function():
	k = 1
	k2 = 2
	function = ''
	op = ''
	res = ''
	res2 = ''

	d1 = range(1, 50)
	d2 = range(2, 51)

	d11 = range(51, 100)
	d21 = range(52, 101)

	d12 = range(101, 150)
	d22 = range(102, 151)

	d13 = range(101, 150)
	d23 = range(102, 151)

	d14 = range(151, 200)
	d24 = range(152, 201)

	d15 = range(201, 250)
	d25 = range(202, 251)

	d16 = range(251, 300)
	d26 = range(252, 301)

	d17 = range(301, 350)
	d27 = range(302, 351)

	d18 = range(351, 400)
	d28 = range(352, 401)

	d19 = range(401, 450)
	d29 = range(402, 451)

	d110 = range(451, 500)
	d210 = range(452, 501)

	d111 = range(501, 550)
	d211 = range(502, 551)
	
	d112 = range(551, 600)
	d212 = range(552, 601)

	d113 = range(601, 650)
	d213 = range(602, 651)

	d114 = range(651, 700)
	d214 = range(652, 701)

	d115 = range(701, 750)
	d215 = range(702, 751)

	d116 = range(751, 800)
	d216 = range(752, 801)

	d117 = range(801, 850)
	d217 = range(802, 851)

	d118 = range(851, 900)
	d218 = range(852, 901)

	d119 = range(901, 950)
	d219 = range(902, 951)

	d120 = range(951, 980)
	d220 = range(952, 981)


	fct0 = [list(a) for a in zip(d1, d2)]
	for i in fct0:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct1 = [list(a) for a in zip(d11, d21)]
	for i in fct1:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct2 = [list(a) for a in zip(d12, d22)]
	for i in fct2:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct3 = [list(a) for a in zip(d13, d23)]
	for i in fct3:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct4 = [list(a) for a in zip(d14, d24)]
	for i in fct4:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct5 = [list(a) for a in zip(d15, d25)]
	for i in fct5:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct6 = [list(a) for a in zip(d16, d26)]
	for i in fct6:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct7 = [list(a) for a in zip(d17, d27)]
	for i in fct7:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct8 = [list(a) for a in zip(d18, d28)]
	for i in fct8:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct9= [list(a) for a in zip(d19, d29)]
	for i in fct9:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct10 = [list(a) for a in zip(d110, d210)]
	for i in fct10:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct11 = [list(a) for a in zip(d111, d211)]
	for i in fct11:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct12 = [list(a) for a in zip(d112, d212)]
	for i in fct12:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct13 = [list(a) for a in zip(d113, d213)]
	for i in fct13:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct14 = [list(a) for a in zip(d114, d214)]
	for i in fct14:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct15 = [list(a) for a in zip(d115, d215)]
	for i in fct15:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct16 = [list(a) for a in zip(d116, d216)]
	for i in fct16:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)


	function = ''
	fct17 = [list(a) for a in zip(d117, d217)]
	for i in fct17:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct18 = [list(a) for a in zip(d118, d218)]
	for i in fct18:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct19 = [list(a) for a in zip(d119, d219)]
	for i in fct19:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	function = ''
	fct20 = [list(a) for a in zip(d120, d220)]
	for i in fct20:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)
	
	return ''


@graphres.route('/ids', methods=["POST"]) # create the function dependencies for the indexing schema
def idss():
	k = 20
	var = ''
	res = ''
	currentf  = ''
	d1 = range(1, 500)
	d2 = range(2, 501)
	d3 = range(1, 501)
	
	col1 = np.array(d1)
	col2 = np.array(d2)

	fg = list(zip(col1, col2))

	function = ''
	for i in fg:
		function = function + '{"fct1": "'+str(i[0])+'","fct2": "'+str(i[1])+'"},'
	function = function[:-1]
	print (function)

	for i in d3:
		res = res + '{"fct": "'+str(i)+'","k": "'+str(k)+'"},'
	res = res[:-1]
	print (res)		
	return ''

@graphres.route('/vresource', methods=["POST"]) # creation of virtual resources
def vr():
	global req; 
	req = request.get_json()
	data = json.dumps(req)
	d = json.loads(data)
	drarr = os.listdir('/dynamic')
	global dynamic 
	for item in d['operations']:
		dynamic = ""
		dynamic_json = ""
		for i in range(len(drarr)):
			if (str(os.path.splitext(drarr[i])[0]) != '__init__' and str(os.path.splitext(drarr[i])[1]) != '.pyc'):
				dyn_res = os.path.splitext(drarr[i])[0]
				if (dyn_res.split('_')[1] == item):
					dynamic = dynamic+'{"@id": "http://localhost:5000/resource/'+dyn_res+'"},'
		dynamic_json = dynamic.rstrip(',')
		vr_name = 'VR_'+item
		content =  '''#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, url_for, json
from flask import Response
from flask import request
from flask import jsonify, make_response
from flask_restful import reqparse

from random import randint

from itertools import cycle
import requests


'''+vr_name+''' = Blueprint(\''''+vr_name+'''\', __name__,)

def gen_series(n, min_val, max_val):
 	x = []
 	for i in range(0, n):
 		x.append(randint(min_val, max_val))
 	return x

@'''+vr_name+'''.route('', methods=['GET', 'HEAD'])
def vresource():
	data = request.get_json()
	print (data)
	if request.method == 'GET':
		v = gen_series(10, 18, 24)
		resp = make_response(jsonify(data=v))
		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+vr_name+'''.md'
		return resp
	if request.method == 'HEAD':
		resp = make_response()
		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+vr_name+'''.md'
		return resp


@'''+vr_name+'''.route('/'''+vr_name+'''.md')
def rvirtual():
	myjson = """
 		{
 			"@context": "http://localhost:5000/resourceDescription/context.jsonld",
			"@id": "http://localhost:5000/resourceDescription/'''+vr_name+'''.md",
			"entrypoint": "http://localhost:5000/resource/'''+vr_name+'''",
			"Operation": [{
				"functionality": "'''+item+'''"
				}],
			"Collection": {
		 		"member": [
						'''+dynamic_json+'''
					]
			},
			"Link": []
 		}
 		"""
 	return myjson
	
				'''
		save_path = '/virtual'
		completeName = os.path.join(save_path, vr_name+".py")         
		fileres = open(completeName, "w")
		fileres.write(content)
		fileres.close()
	return ''


@graphres.route('/dresource', methods=["POST"]) # creation of dynamic resources
def dr():
	global req; 
	drarr = []
	req = request.get_json()
	data = json.dumps(req)
	d = json.loads(data)
	for item in d['koperations']:
		i = int(item['k'])
		for k in range(1,i+1):
			dr_name = 'DR_'+item['fct']+'_'+str(k)
			content =  '''#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, url_for, json
from flask import Response
from flask import request
from flask import jsonify, make_response
from flask_restful import reqparse

from random import randint

from itertools import cycle
import requests


'''+dr_name+''' = Blueprint(\''''+dr_name+'''\', __name__,)

def gen_series(n, min_val, max_val):
 	x = []
 	for i in range(0, n):
 		x.append(randint(min_val, max_val))
 	return x

@'''+dr_name+'''.route('', methods=['GET', 'HEAD'])
def dresource():
	data = request.get_json()
	print (data)
	if request.method == 'GET':
		v = gen_series(10, 18, 24)
		resp = make_response(jsonify(data=v))
		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+dr_name+'''.md'
		return resp
	if request.method == 'HEAD':
		resp = make_response()
		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+dr_name+'''.md'
		return resp


@'''+dr_name+'''.route('/'''+dr_name+'''.md')
def rdynamic():
	myjson = """
 		{
 			"@context": "http://localhost:5000/resourceDescription/context.jsonld",
			"@id": "http://localhost:5000/resourceDescription/'''+dr_name+'''.md",
			"entrypoint": "http://localhost:5000/resource/'''+dr_name+'''",
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "'''+item['fct']+'''"
				}]
 		}
 		"""
 	return myjson
	
				'''
			save_path = '/dynamic'
			completeName = os.path.join(save_path, dr_name+".py")         
			fileres = open(completeName, "w")
			fileres.write(content)
			fileres.close()
	return ''



@graphres.route('/insresource', methods=["POST"]) # creation of the resources necessary to construct the indexing schema
def insr():
	global req; 
	req = request.get_json()
	data = json.dumps(req)
	d = json.loads(data)
	
	total_sres = []
	for item in d['koperations']:
		i = int(item['k'])
		for k in range(1,i+1):
			sr_name = 'SR_'+item['fct']+'_'+str(k)
			total_sres.append([sr_name, item['fct']])

	
	for i in range(len(total_sres)):
		link = ""
		function = total_sres[i][1]
		for fun in d['dep_operations']:
			if fun['fct1'] == function:
				for j in range(len(total_sres)):
					if total_sres[j][1]==fun['fct2']:
						link=link+'''{
								"@id": "http://localhost:5000/resource/'''+total_sres[j][0]+'''",
								"method": "GET",
								"relationType": "isComplementary",
								"functionality": "'''+fun['fct2']+'''"
							},'''
		for l in range(len(total_sres)):
			if (total_sres[l][1] == function) and (total_sres[l][0] != total_sres[i][0]):
				link=link+'''{
								"@id": "http://localhost:5000/resource/'''+total_sres[l][0]+'''",
								"method": "GET",
								"relationType": "isSimilar",
								"functionality": "'''+function+'''"
							},'''

		link_res = link[:-1]
		content =  '''#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, url_for, json

from flask import Response
from flask import request
from flask import jsonify, make_response
from flask_restful import reqparse

from random import randint

from itertools import cycle
import requests


'''+total_sres[i][0]+''' = Blueprint(\''''+total_sres[i][0]+'''\', __name__,)

def gen_series(n, min_val, max_val):
 	x = []
 	for i in range(0, n):
 		x.append(randint(min_val, max_val))
 	return x

@'''+total_sres[i][0]+'''.route('', methods=['GET', 'HEAD'])
def sresource():
	data = request.get_json()
	print (data)
	if request.method == 'GET':
		v = gen_series(10, 18, 24)

		resp = make_response(jsonify(data=v))
		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+total_sres[i][0]+'''.md'
		return resp
	if request.method == 'HEAD':
		resp = make_response()

		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+total_sres[i][0]+'''.md'
		return resp


@'''+total_sres[i][0]+'''.route('/'''+total_sres[i][0]+'''.md')
def rstatic():
	myjson = """
 		{
 			"@context": "http://localhost:5000/resourceDescription/context.jsonld",
			"@id": "http://localhost:5000/resourceDescription/'''+total_sres[i][0]+'''.md",
			"entrypoint": "http://localhost:5000/resource/'''+total_sres[i][0]+'''",
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "'''+total_sres[i][1]+'''"

				}],
			"Link": ['''+link_res+''']
 		}
 		"""
 	return myjson
	
				'''
		save_path = '/init_static'
		completeName = os.path.join(save_path, total_sres[i][0]+".py")         
		fileres = open(completeName, "w")
		fileres.write(content)
		fileres.close()
	return ''





@graphres.route('/sresource', methods=["POST"]) # creation of static resources
def sr():
	global req; 
	req = request.get_json()
	data = json.dumps(req)
	d = json.loads(data)
	
	total_sres = []
	for item in d['koperations']:
		i = int(item['k'])
		for k in range(1,i+1):
			sr_name = 'SR_'+item['fct']+'_'+str(k)
			total_sres.append([sr_name, item['fct']])

	
	for i in range(len(total_sres)):
		link = ""
		function = total_sres[i][1]
		for fun in d['dep_operations']:
			if fun['fct1'] == function:
				for j in range(len(total_sres)):
					if total_sres[j][1]==fun['fct2']:
						link=link+'''{
								"@id": "http://localhost:5000/resource/'''+total_sres[j][0]+'''",
								"method": "GET",
								"relationType": "isComplementary",
								"functionality": "'''+fun['fct2']+'''"
							},'''
		for l in range(len(total_sres)):
			if (total_sres[l][1] == function) and (total_sres[l][0] != total_sres[i][0]):
				link=link+'''{
								"@id": "http://localhost:5000/resource/'''+total_sres[l][0]+'''",
								"method": "GET",
								"relationType": "isSimilar",
								"functionality": "'''+function+'''"
							},'''
		link=link+'''{
								"@id": "http://localhost:5000/resource/'''+'VR_'+function+'''",
								"method": "GET",
								"relationType": "isSimilar",
								"functionality": "'''+function+'''"
							},'''
		link_res = link[:-1]
		content =  '''#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, url_for, json
from flask import Response
from flask import request
from flask import jsonify, make_response
from flask_restful import reqparse

from random import randint

from itertools import cycle
import requests


'''+total_sres[i][0]+''' = Blueprint(\''''+total_sres[i][0]+'''\', __name__,)

def gen_series(n, min_val, max_val):
 	x = []
 	for i in range(0, n):
 		x.append(randint(min_val, max_val))
 	return x

@'''+total_sres[i][0]+'''.route('', methods=['GET', 'HEAD'])
def sresource():
	data = request.get_json()
	print (data)
	if request.method == 'GET':
		v = gen_series(10, 18, 24)
		resp = make_response(jsonify(data=v))
		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+total_sres[i][0]+'''.md'
		return resp
	if request.method == 'HEAD':
		resp = make_response()
		resp.headers['Link'] = 'http://localhost:5000/resourceDescription/'''+total_sres[i][0]+'''.md'
		return resp


@'''+total_sres[i][0]+'''.route('/'''+total_sres[i][0]+'''.md')
def rstatic():
	myjson = """
 		{
 			"@context": "http://localhost:5000/resourceDescription/context.jsonld",
			"@id": "http://localhost:5000/resourceDescription/'''+total_sres[i][0]+'''.md",
			"entrypoint": "http://localhost:5000/resource/'''+total_sres[i][0]+'''",
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "'''+total_sres[i][1]+'''"
				}],
			"Link": ['''+link_res+''']
 		}
 		"""
 	return myjson
	
				'''
		save_path = '/static'
		completeName = os.path.join(save_path, total_sres[i][0]+".py")         
		fileres = open(completeName, "w")
		fileres.write(content)
		fileres.close()
	return ''

@graphres.route('/importres') # fill both 'from.py' and 'appregister.py' files, which include references to the created resources (virtual, dynamic, and static)
def ir():
	fromcontent=""
	appregcontent=""
	srarr = os.listdir('/static')
	vrarr = os.listdir('/virtual')
	drarr = os.listdir('/dynamic')
	for s in range(len(srarr)):
		if (str(os.path.splitext(srarr[s])[0]) != '__init__' and str(os.path.splitext(srarr[s])[1]) != '.pyc'):
			fromcontent= fromcontent+"from servicesDescAuto.static."+str(os.path.splitext(srarr[s])[0])+" import "+str(os.path.splitext(srarr[s])[0])+"\n"
	for v in range(len(vrarr)):
		if (str(os.path.splitext(vrarr[v])[0]) != '__init__' and str(os.path.splitext(vrarr[v])[1]) != '.pyc'):
			fromcontent= fromcontent+"from servicesDescAuto.virtual."+str(os.path.splitext(vrarr[v])[0])+" import "+str(os.path.splitext(vrarr[v])[0])+"\n"
	for d in range(len(drarr)):
		if (str(os.path.splitext(drarr[d])[0]) != '__init__' and str(os.path.splitext(drarr[d])[1]) != '.pyc'):
			fromcontent= fromcontent+"from servicesDescAuto.dynamic."+str(os.path.splitext(drarr[d])[0])+" import "+str(os.path.splitext(drarr[d])[0])+"\n"

	path = '/from.py'        
	filefrom = open(path, "w")
	filefrom.write(fromcontent)
	filefrom.close()
	
	for s in range(len(srarr)):
		if (str(os.path.splitext(srarr[s])[0]) != '__init__' and str(os.path.splitext(srarr[s])[1]) != '.pyc'):
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(srarr[s])[0])+", url_prefix='/resource/"+str(os.path.splitext(srarr[s])[0])+"')\n"
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(srarr[s])[0])+", url_prefix='/resourceDescription')\n"
	
	for v in range(len(vrarr)):
		if (str(os.path.splitext(vrarr[v])[0]) != '__init__' and str(os.path.splitext(vrarr[v])[1]) != '.pyc'):
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(vrarr[v])[0])+", url_prefix='/resource/"+str(os.path.splitext(vrarr[v])[0])+"')\n"
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(vrarr[v])[0])+", url_prefix='/resourceDescription')\n"

	for d in range(len(drarr)):
		if (str(os.path.splitext(drarr[d])[0]) != '__init__' and str(os.path.splitext(drarr[d])[1]) != '.pyc'):
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(drarr[d])[0])+", url_prefix='/resource/"+str(os.path.splitext(drarr[d])[0])+"')\n"
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(drarr[d])[0])+", url_prefix='/resourceDescription')\n"

	pathre = '/appregister.py'        
	fileapp = open(pathre, "w")
	fileapp.write(appregcontent)
	fileapp.close()

	return ''


@graphres.route('/inimportres') # fill both 'infrom.py' and 'inappregister.py' files, which include references to the created resources used to construct the indexing schema
def inir():
	fromcontent=""
	appregcontent=""
	srarr = os.listdir('/init_static')
	for s in range(len(srarr)):
		if (str(os.path.splitext(srarr[s])[0]) != '__init__' and str(os.path.splitext(srarr[s])[1]) != '.pyc'):
			fromcontent= fromcontent+"from servicesDescAuto.static."+str(os.path.splitext(srarr[s])[0])+" import "+str(os.path.splitext(srarr[s])[0])+"\n"

	path = '/infrom.py'        
	filefrom = open(path, "w")
	filefrom.write(fromcontent)
	filefrom.close()
	
	for s in range(len(srarr)):
		if (str(os.path.splitext(srarr[s])[0]) != '__init__' and str(os.path.splitext(srarr[s])[1]) != '.pyc'):
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(srarr[s])[0])+", url_prefix='/resource/"+str(os.path.splitext(srarr[s])[0])+"')\n"
			appregcontent=appregcontent+"app.register_blueprint("+str(os.path.splitext(srarr[s])[0])+", url_prefix='/resourceDescription')\n"

	pathre = '/inappregister.py'        
	fileapp = open(pathre, "w")
	fileapp.write(appregcontent)
	fileapp.close()

	return ''
	

