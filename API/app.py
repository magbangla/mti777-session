# -*- coding: utf-8 -*-
import os
from flask import Flask, url_for, redirect, render_template, request, abort
import pymysql
#from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash
from functools import update_wrapper
import json
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin


def crossdomain(origin=None, methods=None, headers=None,
				max_age=21600, attach_to_all=True,
				automatic_options=True):
	if methods is not None:
		methods = ', '.join(sorted(x.upper() for x in methods))
	if headers is not None and not isinstance(headers, basestring):
		headers = ', '.join(x.upper() for x in headers)
	if not isinstance(origin, basestring):
		origin = ', '.join(origin)
	if isinstance(max_age, timedelta):
		max_age = max_age.total_seconds()

	def get_methods():
		if methods is not None:
			return methods

		options_resp = current_app.make_default_options_response()
		return options_resp.headers['allow']

	def decorator(f):
		def wrapped_function(*args, **kwargs):
			if automatic_options and request.method == 'OPTIONS':
				resp = current_app.make_default_options_response()
			else:
				resp = make_response(f(*args, **kwargs))
			if not attach_to_all and request.method != 'OPTIONS':
				return resp

			h = resp.headers

			h['Access-Control-Allow-Origin'] = origin
			h['Access-Control-Allow-Methods'] = get_methods()
			h['Access-Control-Max-Age'] = str(max_age)
			if headers is not None:
				h['Access-Control-Allow-Headers'] = headers
			return resp

		f.provide_automatic_options = False
		return update_wrapper(wrapped_function, f)
	return decorator

mysql = MySQL()

# MySQL configurations

# Create Flask application
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'magbangla'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'mti777'
app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
mysql.init_app(app)
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app, resources={r"/getall": {"origins": "*"},r"/rescherche": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/', methods=['GET'])
def index():
	return "<b>API WORKS</>"

@app.route('/getall', methods=['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getall():
	try:
		sql = "SELECT * FROM annonces ORDER BY loyer ASC"
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(sql)
		rows = cursor.fetchall()
		photos_=None
		data=[]
		for l in rows:
			data_row={"id_annonces":l["id_annonces"],
					"titre_annonce":l["titre_annonce"],
					"adresse":l["adresse"],
					"loyer":l["loyer"],
					"details":l["details"],
					"url_annonce":l["url_annonce"],
					"disponibilite":l["disponibilite"],
					"thumbnail_url":l["thumb"]
			}
			data.append(data_row)
		resp = jsonify(data)
		resp.status_code = 200
		#return resp
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/recherche', methods=['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def recherche():
	data=request.json
	data['type_de_chambre']=""
	#constituer le sql de la requête
	sql = "SELECT * FROM annonces WHERE "
	if data["adresse"]!="":
	  param1="adresse like '%"+str(data["adresse"])+"%'"
	  sql=sql+param1+" AND "
	if data["type_de_chambre"]!="":
	  param2="type_chambre= "+str(data["type_de_chambre"])
	  sql=sql+param2+ " AND "
	if data["loyer"]!="":
	  param3="loyer BETWEEN "+str(data["loyer"][0])+" AND "+ str(data["loyer"][1])
	  sql=sql+ param3 +"  ORDER BY loyer ASC"
	print(sql)
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(sql)
		rows = cursor.fetchall()
		print (rows)
		photos_=None
		data=[]

		for l in rows:
			id=l['id_annonces']
			sql_=sql = "SELECT * FROM photos WHERE photos.id_annonce= '"+id+"'"
			cursor.execute(sql_)
			rows_photos = cursor.fetchall()
			photos_object=[]
			for ph in rows_photos:
				stg_photos={"url_images":ph["url_images"]}
				photos_object.append(stg_photos)
			data_row={"id_annonces":l["id_annonces"],
						"titre_annonce":l["titre_annonce"],
						"adresse":l["adresse"],
						"loyer":l["loyer"],
						"details":l["details"],
						"url_annonce":l["url_annonce"],
						"disponibilite":l["disponibilite"],
						"photos":photos_object
			}
			data.append(data_row)
		resp = jsonify(data)
		resp.status_code = 200
		#return resp
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/getphotos/<annonce>', methods=['GET'])
def getphotos(annonce):
	try:
		sql = "SELECT * FROM photos WHERE photos.id_annonce = '"+annonce+"'"
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(sql)
		rows_photos = cursor.fetchall()
		photos_object=[]
		for ph in rows_photos:
			stg_photos={"url_images":ph["url_images"]}
			photos_object.append(stg_photos)
		resp = jsonify(photos_object)
		resp.status_code = 200
		#return resp
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/getdetails/', methods=['POST'])
def getdetails():
	try:
		sql = "SELECT * FROM annonces ORDER BY loyer ASC"
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(sql)
		rows = cursor.fetchall()
		photos_=None
		data=[]
		for l in rows:
			id=l['id_annonces']
			sql_=sql = "SELECT * FROM photos WHERE photos.id_annonce= '"+id+"'"
			cursor.execute(sql_)
			rows_photos = cursor.fetchall()
			photos_object=[]
			for ph in rows_photos:
				stg_photos={"url_images":ph["url_images"]}
				photos_object.append(stg_photos)
			data_row={"id_annonces":l["id_annonces"],
					"titre_annonce":l["titre_annonce"],
					"adresse":l["adresse"],
					"loyer":l["loyer"],
					"details":l["details"],
					"url_annonce":l["url_annonce"],
					"disponibilite":l["disponibilite"],
					"thumbnail_url":l["thumb"],
					"photos":photos_object
			}
			data.append(data_row)
		resp = jsonify(data)
		resp.status_code = 200
		#return resp
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	# Start app
	app.run(debug=True,port="5891")
