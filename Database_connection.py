import mysql.connector as db
conn=db.connect(host="localhost",user="root",passwd="jeevanjk4",database="jk")
if(conn.is_connected()):
    print("Success")
cur=conn.cursor()
cur.execute("SELECT * FROM demo")
datas=cur.fetchall()
for row in datas:
    print(row)
cur.close()
conn.close()