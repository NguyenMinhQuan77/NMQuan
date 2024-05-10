from datetime import datetime

import flask
from flask import Blueprint
loaidongho = Blueprint('loaidongho', __name__)

from db_connection import get_database_connection
conn = get_database_connection()

#lay danh sach chat lieu
@loaidongho.route("/loaidh/getall", methods = ['GET'])
def getAllLoaiDH():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From LoaiDH")
        result = []
        keys = []
        for i in cursor.description:
            keys.append(i[0])
        for val in cursor.fetchall():
            result.append(dict(zip(keys, val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

# them chat lieu
@loaidongho.route("/loaidh/add", methods = ['POST'])
def adddchatlieu():
    try:
        tenloai=flask.request.json.get("TenLoai")
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        cusor.execute("INSERT INTO LoaiDH (TenLoai) VALUES (?)",tenloai)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#lay chat lieu theo ma
@loaidongho.route("/loaidh/getbyid/<id>", methods = ['GET'])
def getLoaiDhbyId(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From LoaiDH Where ID=? ",id)
        result = []
        keys = []
        for i in cursor.description:
            keys.append(i[0])
        for val in cursor.fetchall():
            result.append(dict(zip(keys, val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

#sua chat lieu
@loaidongho.route("/loaidh/update", methods = ['PUT'])
def updateKH():
    try:
        tenldh=flask.request.json.get("TenLoai")
        id=flask.request.json.get("ID")
        data=(tenldh,id)
        cusor=conn.cursor()
        cusor.execute("update LoaiDH set TenLoai = ? where ID = ?",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Sua thanh thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#xoa chat lieu theo id
@loaidongho.route("/loaidh/delete/<id>", methods=['Delete'])
def deleteChatLieu(id):
    try:
        #ma=flask.request.json.get("maKhach")
        cusor=conn.cursor()
        #data=(ma)
        cusor.execute("delete LoaiDH where ID=?",id)
        conn.commit()
        resp=flask.jsonify({"mess":"thanh cong"})
        return resp
    except Exception as e:
        print(e)
