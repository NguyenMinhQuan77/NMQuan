import flask
from flask_cors import CORS


from dongho import dongho
from thuonghieu import thuonghieu
from khachhang import khachhang
from dathangchitiet import dathangchitiet
from dathang import dathang
from chatlieu import chatlieu
from loaidongho import loaidongho
from xuatxu import xuatxu
from nhanvien import nhanvien
app=flask.Flask(__name__)
CORS(app)

app.register_blueprint(dongho)
app.register_blueprint(thuonghieu)
app.register_blueprint(khachhang)
app.register_blueprint(dathang)
app.register_blueprint(dathangchitiet)
app.register_blueprint(chatlieu)
app.register_blueprint(loaidongho)
app.register_blueprint(xuatxu)
app.register_blueprint(nhanvien)
if __name__ == "__main__":
    app.run()