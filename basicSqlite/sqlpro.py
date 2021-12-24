import sqlite3
from client import Client

bot1 = Client("192.168.1.159", 3000)
print(bot1.port)
conn = sqlite3.connect('test.db')
c = conn.cursor()
#Tạo bảng
# sql_create_table = """CREATE TABLE users (
#     id integer PRIMARY KEY,
#     ipadress text NOT NULL,
#     port integer NOT NULL);"""
# Thêm dữ liệu
# sql_insert = """INSERT INTO users (ipadress, port) VALUES ("192.168.1.11", 3000);"""
# Chọn dữ liệu
sql_select = """SELECT * FROM users """
# Update dữ liệu
# sql_update = """UPDATE users SET port = 3001 WHERE ipadress = "192.168.1.11" """
# Xoá dữ liệu
# sql_delete = """DELETE FROM users WHERE ipadress = "192.168.1.10" """
# thực thi câu lệnh SQL
# c.execute(sql_create_table)
# sql_insert = """INSERT INTO users (ipadress, port) VALUES ("192.168.1.11", 3000);"""
# # Set dữ liệu (cách 1)
sql_insert = f"""INSERT INTO users (ipadress, port) VALUES ("{bot1.ip}", {bot1.port});"""
# sql_insert =f"""-- INSERT INTO users (ipadress, port) VALUES (?,?);""" # Set dữ liệu (cách 2)
# sql_insert = f"""-- INSERT INTO users (ipadress, port) VALUES ("{bot1.ip}", {bot1.port});"""

try:
    c.execute(sql_insert)
    # c.execute(sql_insert, (bot1.ip, bot1.port)) # Cach 2
    # c.execute(sql_update)
    # c.execute(sql_delete)
    conn.commit()
    c.execute(sql_select)
    print(c.fetchall())
except IOError as e:
    print(f"Error: {e}")
# conn.commit()
conn.close()