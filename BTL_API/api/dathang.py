from datetime import datetime

import flask
from flask import Blueprint
dathang = Blueprint('dathang', __name__)

from db_connection import get_database_connection
conn = get_database_connection()

#them dat hang
@dathang.route("/dathang/add", methods = ['POST'])
def adddathang():
    try:
        kh_id = flask.request.json.get("KhachHang_ID")
        dtgh = flask.request.json.get("DienThoaiGiaoHang")
        dcgh = flask.request.json.get("DiaChiGiaoHang")
        ndh_str = flask.request.json.get("NgayDatHang")
        ndh = datetime.strptime(ndh_str, "%a, %d %b %Y %H:%M:%S GMT").strftime("%Y-%m-%d %H:%M:%S")
        tt = flask.request.json.get("TinhTrang")
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        data=(kh_id,dtgh,dcgh,ndh,tt)
        cusor.execute("INSERT INTO DatHang ( KhachHang_ID, DienThoaiGiaoHang, DiaChiGiaoHang, NgayDatHang, TinhTrang) VALUES (?, ?, ?, ?, ?)",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#lay danh sach dat hang
@dathang.route("/dathang/getall", methods = ['GET'])
def getAllDH():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From DatHang")
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

@dathang.route("/dathang/getbyid/<id>", methods = ['GET'])
def getChatLieubyId(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From DatHang Where ID=? ",id)
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