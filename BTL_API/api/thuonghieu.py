import flask
from flask import Blueprint
thuonghieu = Blueprint('thuonghieu', __name__)

from db_connection import get_database_connection
conn = get_database_connection()

# lấy tất cả thương hiệu
@thuonghieu.route("/thuonghieu/getall", methods = ['GET'])
def getAllThuongHieu():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From ThuongHieu order by TenThuongHieu")
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
#them thuong hieu
@thuonghieu.route("/thuonghieu/add", methods = ['POST'])
def addThuongHieu():
    try:
        tenThuongHieu=flask.request.json.get("TenThuongHieu")
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        cusor.execute("INSERT INTO ThuongHieu (TenThuongHieu) VALUES (?)",tenThuongHieu)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#lay thuong hieu theo ma
@thuonghieu.route("/thuonghieu/getbyid/<id>", methods = ['GET'])
def getThuongHieubyId(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From ThuongHieu Where ID=? ",id)
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

#sua thuonghieu
@thuonghieu.route("/thuonghieu/update", methods = ['PUT'])
def updateThuongHieu():
    try:
        tencl=flask.request.json.get("TenThuongHieu")
        id=flask.request.json.get("ID")
        data=(tencl,id)
        cusor=conn.cursor()
        cusor.execute("update ThuongHieu set TenThuongHieu = ? where ID = ?",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Sua thanh thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#xoa thuong hieu theo id
@thuonghieu.route("/thuonghieu/delete/<id>", methods=['Delete'])
def deleteChatLieu(id):
    try:
        #ma=flask.request.json.get("maKhach")
        cusor=conn.cursor()
        #data=(ma)
        cusor.execute("delete ThuongHieu where ID=?",id)
        conn.commit()
        resp=flask.jsonify({"mess":"thanh cong"})
        return resp
    except Exception as e:
        print(e)
