# 원격 데이터베이스 서버(MariaDB)와 연동 
# pip install mysqlclient    로 드라이버 파일 설치

import MySQLdb
"""
conn=MySQLdb.connect(host = '127.0.0.1', user = 'root', 
                     password='7hongdb73', database='test')
print(conn)
conn.close()
"""
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'7hongdb73',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    
    # 자료 추가
    # sql="insert into sangdata(code,sang,su,dan) values(10,'상품1',5,1000)"
    # cursor.execute(sql)
    # conn.commit()
    
    """
    sql="insert into sangdata values(%s,%s,%s,%s)"
    sql_data='11','상품2',12,2000
    cou=cursor.execute(sql, sql_data)
    conn.commit()
    print('cou: ', cou)
    if cou == 1:
        print('추가 성공')
    """
    """
    # 자료 수정
    sql="update sangdata set sang=%s, su=%s, dan=%s where code=%s"
    sql_data=('파이썬', 7, 5000, 10)   
    cursor.execute(sql, sql_data)
    conn.commit()
    """
    # 자료 삭제
    code='11'
    # sql injection 해킹이 될 수 있으므로 비권장 secure coding guideline에 위배
    # sql="delete from sangdata where code="+code 
    # sql="delete from sangdata where code='{0}'".format(code)    # 권장 1
    
    sql="delete from sangdata where code=%s"   # 권장 2
    cursor.execute(sql, (code,))
    conn.commit()
    # 자료 읽기
    sql="select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        # print(data)
        print('%s %s %s %s'%data)
    """    
    print()
    for r in cursor:
        # print(r)
        print(r[0], r[1], r[2], r[3])
    print()
    for(code, sang, su, dan) in cursor:
        print(code, sang, su, dan)
        
    print()
    for(a, b, c, d) in cursor:
        print(a, b, c, d)
    """    
except Exception as e:
    print('에러: ', e)
finally:
    conn.close()











