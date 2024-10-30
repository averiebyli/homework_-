from src.db import MySQLCommand

sql = MySQLCommand(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678',
    database='heart_disease',
    charset='utf8'
)
sql.connectMysql()

# sql.insertMysql('src/load_data.sql')
result = sql.queryMysql('src/test.sql')
print(result)

sql.closeMysql()
