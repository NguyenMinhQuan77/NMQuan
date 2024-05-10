import flask
from flask import Blueprint
dongho = Blueprint('dongho', __name__)

from db_connection import get_database_connection
conn = get_database_connection()
#api get tat ca khach hang
@dongho.route("/dongho/getall", methods = ['GET'])
def getAllKH():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From DongHo")
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

#lấy đồng hồ theo thương hiệu
@dongho.route("/dongho/getbyidth/<id>", methods = ['GET'])
def getDHbythuonghieuId(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From DongHo Where ThuongHieu_ID=? ",id)
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

#lấy đồng ho theo tên tìm kiem
@dongho.route("/dongho/getbyname/<string:thuong_hieu>", methods=['GET'])
def getDHbyName(thuong_hieu):
    try:
        cursor = conn.cursor()
        search_term = '%' + thuong_hieu + '%'
        cursor.execute("SELECT * FROM DongHo WHERE TenDongHo LIKE ? OR MoTa LIKE ?", (search_term, search_term))
        result = []
        keys = [i[0] for i in cursor.description]
        for val in cursor.fetchall():
            result.append(dict(zip(keys, val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

#lay dong ho theo ma dongho
@dongho.route("/dongho/getbyidsp/<id>", methods = ['GET'])
def getDHbyIdDh(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From DongHo Where ID=? ",id)
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

#lay dong ho duoc mua nhieu
@dongho.route("/dongho/getbuymost", methods = ['GET'])
def getbuymost():
    try:
        cursor = conn.cursor()
        sql = "SELECT dh.TenDongHo, dh.HinhAnhDH, dh.DonGia, dh.ID, SUM(ct.SoLuong) AS SoLuong " + \
              "FROM DongHo dh " + \
              "JOIN DatHang_ChiTiet ct ON dh.ID = ct.DongHo_ID " + \
              "JOIN DatHang dhang ON ct.DatHang_ID = dhang.ID " + \
              "WHERE ct.SoLuong > 0 " + \
              "GROUP BY dh.TenDongHo, dh.HinhAnhDH, dh.DonGia, dh.ID " + \
              "ORDER BY SoLuong DESC"
        cursor.execute(sql)
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

#update số lượng đồng hồ
@dongho.route("/dongho/update", methods = ['PUT'])
def updateslDH():
    try:
        mk=flask.request.json.get("SoLuong")
        id=flask.request.json.get("ID")
        data=(mk,id)
        cusor=conn.cursor()
        cusor.execute("update DongHo set SoLuong = ? where ID = ?",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Sua thanh thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})
