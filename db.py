import datetime
import mysql.connector
import pdb
pdb.set_trace()
cnx = mysql.connector.connect(user='root', database='test')
cursor = cnx.cursor()

query = ("SELECT * FROM sport")


cursor.execute(query)
for lane in cursor:
  print(lane)

cursor.close()
cnx.close()
