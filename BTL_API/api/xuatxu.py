from datetime import datetime

import flask
from flask import Blueprint
xuatxu = Blueprint('xuatxu', __name__)

from db_connection import get_database_connection
conn = get_database_connection()

#lay danh sach xuat xu
@xuatxu.route("/xuatxu/getall", methods = ['GET'])
def getAllXuatXu():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From XuatXu")
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
# them xuat xu
@xuatxu.route("/xuatxu/add", methods = ['POST'])
def addchatlieu():
    try:
        tenQuocGia=flask.request.json.get("TenQG")
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        cusor.execute("INSERT INTO XuatXu (TenQG) VALUES (?)",tenQuocGia)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#lay xuat xu theo ma
@xuatxu.route("/xuatxu/getbyid/<id>", methods = ['GET'])
def getChatLieubyId(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From XuatXu Where ID=? ",id)
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

#sua xuat xu
@xuatxu.route("/xuatxu/update", methods = ['PUT'])
def updateChatLieu():
    try:
        tencl=flask.request.json.get("TenQG")
        id=flask.request.json.get("ID")
        data=(tencl,id)
        cusor=conn.cursor()
        cusor.execute("update XuatXu set TenQG = ? where ID = ?",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Sua thanh thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#xoa xuat xu theo id
@xuatxu.route("/xuatxu/delete/<id>", methods=['Delete'])
def deleteChatLieu(id):
    try:
        #ma=flask.request.json.get("maKhach")
        cusor=conn.cursor()
        #data=(ma)
        cusor.execute("delete XuatXu where ID=?",id)
        conn.commit()
        resp=flask.jsonify({"mess":"thanh cong"})
        return resp
    except Exception as e:
        print(e)