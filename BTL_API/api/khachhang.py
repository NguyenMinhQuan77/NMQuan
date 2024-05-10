import flask
from flask import Blueprint
khachhang = Blueprint('khachhang', __name__)

from db_connection import get_database_connection
conn = get_database_connection()


#danh sach san pham mua hang
@khachhang.route("/khachhang/getorder/<id>", methods=['GET'])
def getorder(id):
    try:
        cursor = conn.cursor()
        sql = "SELECT dh.TenDongHo, dh.HinhAnhDH, ct.DonGia, kh.ID, ct.SoLuong, dhang.NgayDatHang, dhang.TinhTrang " + \
              "FROM DongHo dh " + \
              "JOIN DatHang_ChiTiet ct ON dh.ID = ct.DongHo_ID " + \
              "JOIN DatHang dhang ON ct.DatHang_ID = dhang.ID " + \
              "JOIN KhachHang kh ON dhang.KhachHang_ID = kh.ID " + \
              "WHERE kh.ID = ? " + \
              "ORDER BY dhang.NgayDatHang DESC"
        cursor.execute(sql, (id,))
        result = []
        keys = [i[0] for i in cursor.description]
        for val in cursor.fetchall():
            result.append(dict(zip(keys, val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

#lay khách hàng theo id
@khachhang.route("/khachhang/getkh/<id>", methods = ['GET'])
def getKHbyId(id):
    try:
        cusor = conn.cursor()
        cusor.execute("SELECT * FROM KhachHang WHERE ID=?", id)
        result = cusor.fetchone()  # Fetch one row
        keys = [i[0] for i in cusor.description]  # Extract column names
        if result:
            # Convert fetched row to dictionary
            result_dict = dict(zip(keys, result))
            resp=flask.jsonify(result_dict)
            resp.status_code=200
            return resp
        else:
            # Trả về mã lỗi 404 nếu không tìm thấy khách hàng
            return "Không tìm thấy thông tin khách hàng.", 404
    except Exception as e:
        print(e)

#sua khách hàng
@khachhang.route("/khachhang/update", methods = ['PUT'])
def updateKH():
    try:
        mk=flask.request.json.get("MatKhau")
        id=flask.request.json.get("ID")
        hoten=flask.request.json.get("HoVaten")
        dt = flask.request.json.get("DienThoai")
        dc = flask.request.json.get("DiaChi")
        tdn = flask.request.json.get("TenDangNhap")
        data=(mk,hoten,dt,dc,tdn,id)
        cusor=conn.cursor()
        cusor.execute("update KhachHang set MatKhau = ?,HoVaten=?, DienThoai=?,DiaChi=?,TenDangNhap=? where ID = ?",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Sua thanh thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#them khách hàng
@khachhang.route("/khachhang/add", methods = ['POST'])
def addKH():
    try:
        ht=flask.request.json.get("HoVaten")
        dt = flask.request.json.get("DienThoai")
        dc = flask.request.json.get("DiaChi")
        tdn = flask.request.json.get("TenDangNhap")
        mk=flask.request.json.get("MatKhau")
        cusor=conn.cursor()
        #cusor.execute("SET IDENTITY_INSERT tblQLKH ON")
        data=(ht,dt,dc,tdn,mk)
        cusor.execute("insert into KhachHang(HoVaten,DienThoai, DiaChi, TenDangNhap,MatKhau) values( ?, ?, ?,?, ?)",data)
        conn.commit()
        resp=flask.jsonify({"Mess":"Them moi thanh cong"})
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        return flask.jsonify({"error": "Internal Server Error"})

#xoa khach hang theo id
@khachhang.route("/khachhang/delete/<id>", methods=['Delete'])
def deletekhachhang(id):
    try:
        #ma=flask.request.json.get("maKhach")
        cusor=conn.cursor()
        #data=(ma)
        cusor.execute("delete KhachHang where ID=?",id)
        conn.commit()
        resp=flask.jsonify({"mess":"thanh cong"})
        return resp
    except Exception as e:
        print(e)