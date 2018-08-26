import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "ctbu")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM tb_student \
       WHERE id > %d" % (1)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        password = row[2]
        score = row[3]

        # 打印结果
        print("id=%s,name=%s,password=%s,score=%d" % \
              (id, name, password,score))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()