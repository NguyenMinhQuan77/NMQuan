import pyodbc

def get_database_connection():
    connect_str = 'DRIVER={SQL Server};SERVER=THICHNGUYEN\SQLEXPRESS04;DATABASE=ShopDongHo;Trusted_Connection=yes'
    conn = pyodbc.connect(connect_str)
    return conn