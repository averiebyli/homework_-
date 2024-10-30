import pymysql

class MySQLCommand(object):
    def __init__(self, host, port, user, passwd, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.database = database
        self.charset = charset

    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                                        port=self.port,
                                        user=self.user,
                                        passwd=self.password,
                                        db=self.database,
                                        charset=self.charset)
            self.cursor = self.conn.cursor()
        except Exception as e:
            self.conn = None
            self.cursor = None
            print('connect mysql error.', e)

    def queryMysql(self, sql_path):
        try:
            with open(sql_path, 'r', encoding='utf-8') as file:
                sql_script = file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    self.cursor.execute(statement)
            row = self.cursor.fetchall()
            return row
        except Exception as e:
            print(e)
            print(sql_path)
    # 添加类方法，可以直接运行sql语句字符串
    def queryMysql_str(self, sql_str):
        try:
            # with open(sql_path, 'r', encoding='utf-8') as file:
            #     sql_script = file.read()
            sql_script = sql_str
            for statement in sql_script.split(';'):
                if statement.strip():
                    self.cursor.execute(statement)
            row = self.cursor.fetchall()
            return row
        except Exception as e:
            print(e)
            print(sql_str)

    def insertMysql(self, sql_path):
        try:
            with open(sql_path, 'r', encoding='utf-8') as file:
                sql_script = file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    self.cursor.execute(statement)
            self.conn.commit()
        except Exception as e:
            self.cursor.rollback()
            print(e)
            print(sql_path)

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()
