from flask import Flask, jsonify, request, abort
import time
import requests
import json
import hashlib
import dataset

db = dataset.connect('sqlite:////var/www/flask/myDB')

app = Flask(__name__)


@app.route("/kvStore", methods=['GET', 'POST'])
def kvStore():
    key = request.values.get('key', type=str)
    value = request.values.get('value', type=str)
    kv={"key":key,"value":value}
    if db["kvStore"].find_one(key=key):
        db["kvStore"].update(kv,['key'])
    else:
        db["kvStore"].insert(kv)
    return jsonify(db["kvStore"].find_one(key=key))

@app.route("/kvGet", methods=['GET', 'POST'])
def kvGet():
    key = request.values.get('key', type=str)
    return jsonify(db["kvStore"].find_one(key=key))


@app.route("/kvDelete", methods=['GET', 'POST'])
def kvDelete():
    key = request.values.get('key', type=str)
    db["kvStore"].delete(key=key)
    return jsonify({"success": True})


@app.route("/kvList", methods=['GET', 'POST'])
def kvList():
    prefix = request.values.get('prefix', type=str)
    return jsonify(list(db["kvStore"].find(key={"like":prefix+"%"})))


@app.route("/kvBulkUpdate", methods=['GET', 'POST'])
def kvBulkUpdate():
    result=[]
    for i in range(100):
        key = request.values.get('key'+str(i), type=str)
        value = request.values.get('value'+str(i), type=str)
        if key is None:
            break
        kv={"key":key,"value":value}
        if db["kvStore"].find_one(key=key):
            db["kvStore"].update(kv,['key'])
        else:
            db["kvStore"].insert(kv)
        result+=[db["kvStore"].find_one(key=key)]        
    return jsonify(result)



@app.route("/kvBulkGet", methods=['GET', 'POST'])
def kvBulkGet():
    result=[]
    for i in range(100):
        key = request.values.get('key'+str(i), type=str)
        #quit when out of keys
        if key is None:
            break
        result+=[db["kvStore"].find_one(key=key)]        
    return jsonify(result)
