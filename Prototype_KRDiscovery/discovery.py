#!/usr/bin/env python

from flask import Blueprint
from flask import Flask, url_for, json
from flask import Response
from flask import request
from flask import jsonify, make_response
from flask_restful import reqparse

from random import randint

from itertools import cycle
import requests
import numpy as np

import snakes.plugins
import snakes.pnml
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
import itertools
import json 
import time
import resource

discovery = Blueprint('discovery', __name__,)


@discovery.route('/resource/discovery', methods=["POST"]) # resource that calls bfs-based algorithm
def postRequest():
	time_start = time.time()
	global req; 
	req = request.get_json()
	discovered = disc_bfs() 
	time_elapsed = (time.time() - time_start)*1000
	print ('time ', time_elapsed)
	return 'ok'


@discovery.route('/resource/dfs', methods=["POST"]) # resource that calls dfs-based algorithm
def Request():
	time_start = time.time()
	req = request.get_json()	
	data = json.dumps(req)
	d = json.loads(data)
	global discovered; 
	discovered = []
	global visited; 
	visited = []
	global operations_array
	operations_array = []
	operations_url = []
	global stack
	stack = []
	current_position=0
	init_node = 0
	for item in d['operations']:
		operations_array.append(item)
	for u in d['url']:
		operations_url.append(u)
	global K 
	K = int(d['K'])
	global currentlink
	currentlink = operations_url[init_node]
	while operations_array:
		if (currentlink not in visited):
			disc_dfs(currentlink, visited, operations_array, K)
		else:
			init_node = init_node + 1
			currentlink = operations_url[init_node]
	time_elapsed = (time.time() - time_start)*1000
	print ('time ', time_elapsed)
	return 'ok'


def disc_dfs(currentlink, visited, operations_array, K): # function implementing the dfs algorithm
	if (currentlink not in visited) and (operations_array):
		visited.append(currentlink)
		resp = requests.head(currentlink)
		headers = {'dataType': 'json', 'Content-Type' : 'application/json'}
		descriptor = requests.get(resp.headers['Link'], headers=headers).text
		js = json.loads(descriptor)
		for f in js['Operation']:
			for j in range(len(operations_array)):
				if (operations_array[j] == f['functionality']):
					if 'Collection' in js:
						for r in js['Collection']['member']:
							discovered.append([operations_array[j], r['@id']])
							if (resFound(discovered, operations_array[j]) == K):
								operations_array.remove(operations_array[j])
								break
						break 
					else:
						discovered.append([operations_array[j], currentlink])
						if (resFound(discovered, operations_array[j]) == K):
							operations_array.remove(operations_array[j])
							break
		if 'Link' in js:	
			for l in js['Link']:
				if (("isComplementary" == l['relationType'] or "isSimilar" == l['relationType']) and l['@id'] not in visited):
					disc_dfs(l['@id'], visited, operations_array, K)
	return 'ok'

	
def disc_bfs(): # function implementing the bfs algorithm
	node_number = 0
	headers = {'dataType': 'json', 'Content-Type' : 'application/json'}
	data = json.dumps(req)
	d = json.loads(data)
	discovered = []
	visited = []
	operations_array = []
	operations_url = []
	bfsQueue = []
	current_position=0
	init_node = 0
	for item in d['operations']:
		operations_array.append(item)

	for u in d['url']:
		operations_url.append(u)
	
	global K 
	K = int(d['K'])
	leng = len(operations_array)
	length = 0
	currentlink = operations_url[init_node]
	while operations_array:
		if (currentlink not in visited):
			node_number = node_number + 1
			visited.append(currentlink)
			resp = requests.head(currentlink)
			descriptor = requests.get(resp.headers['Link'], headers=headers).text
			js = json.loads(descriptor)
			for f in js['Operation']:
				for j in range(len(operations_array)):
					if (operations_array[j] == f['functionality']):
						if 'Collection' in js:
							for r in js['Collection']['member']:
								node_number = node_number + 1
								discovered.append([operations_array[j], r['@id']])
								if (resFound(discovered, operations_array[j]) == K):
									operations_array.remove(operations_array[j])
									break
							break 
						else:
							discovered.append([operations_array[j], currentlink])
							if (resFound(discovered, operations_array[j]) == K):
								operations_array.remove(operations_array[j])
								break
			if 'Link' in js:	
				for l in js['Link']:
					if ("isComplementary" == l['relationType'] and l['@id'] not in visited and l['@id'] not in bfsQueue):
						bfsQueue.append(l['@id'])
					if ("isSimilar" == l['relationType'] and l['@id'] not in visited and l['@id'] not in bfsQueue):
						bfsQueue.append(l['@id'])
			if current_position < len(bfsQueue):
				currentlink = bfsQueue[current_position]
				current_position = current_position + 1
			print (operations_array)
		else:
			init_node = init_node + 1
			currentlink = operations_url[init_node]
	print (discovered)
	return discovered

def resFound(discovered, op): # function that counts the number of discovered resources providing the same function
	count = 0
	for d in range(len(discovered)):
		if (discovered[d][0] == op):
			count = count + 1
	return count


def ids(): # function that create a function dependencies list
	var = ''
	currentf  = ''
	d1 = range(1, 500)
	d2 = range(2, 501)
	
	col1 = np.array(d1)
	col2 = np.array(d2)

	fg = list(zip(col1, col2))
	return (fg)

@discovery.route('/resource/resfunn', methods=["POST"]) # compute the time for constructing the indexing schema
def poRequest():
	global req; 
	req = request.get_json()
	fg = ids()
	time_start = time.time()
	functions = []
	flat_list = [item for sublist in fg for item in sublist]
	flat = list(set(flat_list))
	for f in range(len(flat)):
		signature = ''
		for f_fg in range(len(fg)):
			if flat[f] == fg[f_fg][1]:
				signature = str(flat[f]) + "," +str(fg[f_fg][0])
				currentf = fg[f_fg][0]
				while str(currentf):
					enter = 'false'
					for f_fg in range(len(fg)):
						if currentf == fg[f_fg][1]:
							signature = signature + "," +str(fg[f_fg][0])
							currentf = fg[f_fg][0]
							enter = 'true'
							break
					if enter == 'false':
						currentf=''
		print (flat[f])
		print (signature)
	disc_resfun(flat_list)
	time_elapsed = (time.time() - time_start)*1000
	print ('time to get functions/resources signatures and relate the later them to functions', time_elapsed)
	usage=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss 
   	print ('usage to get resources signatures and related them to functions', usage)
	return 'ok'

def disc_resfun(flat_list): # function that retrieves the necessary resources with their provided functions for constructing the indexing schema
	resources = []
	compteur = 0
	headers = {'dataType': 'json', 'Content-Type' : 'application/json'}
	data = json.dumps(req)
	d = json.loads(data)
	visited = []
	operations_url = []
	bfsQueue = []
	current_position=0
	init_node = 0

	for u in d['url']:
		operations_url.append(u)

	currentlink = operations_url[init_node]
	while currentlink:
		if (currentlink not in visited):
			compteur = compteur +1
			function = ''
			signature = []
			visited.append(currentlink)
			resp = requests.head(currentlink)
			descriptor = requests.get(resp.headers['Link'], headers=headers).text
			js = json.loads(descriptor)
			for f in js['Operation']:
				function = f['functionality']
			if 'Link' in js:	
				for l in js['Link']:
					if ("isComplementary" == l['relationType'] and (l['@id'] not in signature)):
						signature.append(l['@id'])
					if ("isSimilar" == l['relationType'] and (l['@id'] not in signature)):
						signature.append(l['@id'])
					if (("isComplementary" == l['relationType']) and (l['@id'] not in visited) and (l['@id'] not in bfsQueue)):
						bfsQueue.append(l['@id'])
					if ("isSimilar" == l['relationType'] and l['@id'] not in visited and l['@id'] not in bfsQueue):
						bfsQueue.append(l['@id'])
			resources.append([currentlink, function, signature]) 
			if current_position < len(bfsQueue):
				currentlink = bfsQueue[current_position]
				current_position = current_position + 1
		else:
			currentlink = ''
	function_resource = []
	flat = list(set(flat_list))
	for f in range(len(flat)):
		f_res = []
		for r in range(len(resources)):
			if (str(flat[f]) == str(resources[r][1])):
				f_res.append(resources[r][0])
		function_resource.append([str(flat[f]), f_res])
	return 'ok'










