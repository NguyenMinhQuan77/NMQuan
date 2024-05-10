import flask
from flask import Blueprint
dathangchitiet = Blueprint('dathangchitiet', __name__)

from db_connection import get_database_connection
conn = get_database_connection()

#them dat hang chi tiet
@dathangchitiet.route("/dathangchitiet/add", methods = ['POST'])
def adddhct():
    try:
        dh_id = flask.request.json.get("DatHang_ID")
        dho_id = flask.request.json.get("DongHo_ID")
        sl = flask.request.json.get("SoLuong")
        dg=flask.request.json.get("DonGia")
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        data=(dh_id,dho_id,sl,dg)
        cusor.execute("INSERT INTO DatHang_ChiTiet ( DatHang_ID, DongHo_ID, SoLuong, DonGia) VALUES (?, ?, ?, ?)",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#lay dat hang chi tiet
@dathangchitiet.route("/dathangchitiet/getall", methods = ['GET'])
def getAllDHCT():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From DatHang_ChiTiet")
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
