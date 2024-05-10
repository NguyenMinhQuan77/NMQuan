from datetime import datetime

import flask
from flask import Blueprint
nhanvien = Blueprint('nhanvien', __name__)

from db_connection import get_database_connection
conn = get_database_connection()

#lay danh sach xuat xu
@nhanvien.route("/nhanvien/getall", methods = ['GET'])
def getAllNhanVien():
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From NhanVien")
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
@nhanvien.route("/nhanvien/add", methods = ['POST'])
def addnhanvien():
    try:
        hoten=flask.request.json.get("HoVaTen")
        dienthoai = flask.request.json.get("DienThoai")
        diachi = flask.request.json.get("DiaChi")
        tendangnhap = flask.request.json.get("TenDangNhap")
        mk = flask.request.json.get("MatKhau")
        quyen = flask.request.json.get("Quyen")
        data = (hoten, dienthoai, diachi, tendangnhap, mk, quyen)
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        cusor.execute("INSERT INTO NhanVien (HoVaTen, DienThoai, DiaChi, TenDangNhap, MatKhau, Quyen) VALUES (?,?,?,?,?,?)",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#lay xuat xu theo ma
@nhanvien.route("/nhanvien/getbyid/<id>", methods = ['GET'])
def getNhanVienbyId(id):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * From NhanVien Where ID=? ",id)
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
@nhanvien.route("/nhanvien/update", methods = ['PUT'])
def updateNhanVien():
    try:
        hoten = flask.request.json.get("HoVaTen")
        dienthoai = flask.request.json.get("DienThoai")
        diachi = flask.request.json.get("DiaChi")
        tendangnhap = flask.request.json.get("TenDangNhap")
        mk = flask.request.json.get("MatKhau")
        quyen = flask.request.json.get("Quyen")
        id=flask.request.json.get("ID")
        data=(hoten, dienthoai, diachi, tendangnhap, mk, quyen,id)
        cusor=conn.cursor()
        cusor.execute("update NhanVien Set HoVaTen = ?, DienThoai = ?, DiaChi = ?, TenDangNhap = ?, MatKhau = ?, Quyen = ? where ID = ?",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Sua thanh thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#xoa nhan vien theo id
@nhanvien.route("/nhanvien/delete/<id>", methods=['Delete'])
def deleteChatLieu(id):
    try:
        #ma=flask.request.json.get("maKhach")
        cusor=conn.cursor()
        #data=(ma)
        cusor.execute("delete NhanVien where ID=?",id)
        conn.commit()
        resp=flask.jsonify({"mess":"thanh cong"})
        return resp
    except Exception as e:
        print(e)