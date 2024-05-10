from datetime import datetime

import flask
from flask import Blueprint
chatlieu = Blueprint('chatlieu', __name__)

from db_connection import get_database_connection
conn = get_database_connection()

#lay danh sach chat lieu
@chatlieu.route("/chatlieu/getall", methods = ['GET'])
def getAllChatLieu():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From ChatLieu")
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
@chatlieu.route("/chatlieu/add", methods = ['POST'])
def addchatlieu():
    try:
        tenChatLieu=flask.request.json.get("TenChatLieu")
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        cusor.execute("INSERT INTO ChatLieu (TenChatLieu) VALUES (?)",tenChatLieu)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#lay chat lieu theo ma
@chatlieu.route("/chatlieu/getbyid/<id>", methods = ['GET'])
def getChatLieubyId(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From ChatLieu Where ID=? ",id)
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
@chatlieu.route("/chatlieu/update", methods = ['PUT'])
def updateChatLieu():
    try:
        tencl=flask.request.json.get("TenChatLieu")
        id=flask.request.json.get("ID")
        data=(tencl,id)
        cusor=conn.cursor()
        cusor.execute("update ChatLieu set TenChatLieu = ? where ID = ?",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Sua thanh thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})
#xoa chat lieu theo id
@chatlieu.route("/chatlieu/delete/<id>", methods=['Delete'])
def deleteChatLieu(id):
    try:
        #ma=flask.request.json.get("maKhach")
        cusor=conn.cursor()
        #data=(ma)
        cusor.execute("delete ChatLieu where ID=?",id)
        conn.commit()
        resp=flask.jsonify({"mess":"thanh cong"})
        return resp
    except Exception as e:
        print(e)