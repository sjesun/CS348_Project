import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
    )
    
cur = db.cursor(dictionary=True)

with open('create_db.sql', 'r') as sqlfile:
    query_iter = cur.execute(sqlfile.read(), multi=True)
    for q in query_iter:
        print("Running: ", q)
        print(f"{q.rowcount} rows changed")
    db.commit()


cur.execute("SHOW TABLES")
for item in cur:
    print(item)