# 키보드로 부서번호 입력받아 해당 부서에 근무하고 있는 직원 출력
import MySQLdb

import pickle
with open('mydb.dat', mode='rb') as obj:
    config=pickle.load(obj)

def chulbal():
    try:
        conn=MySQLdb.connect(**config)
        cursor=conn.cursor()
        
        mem_job=input('직급 입력:')
        sql="""
            select jikwon_no,jikwon_name,jikwon_jik,buser_num
            from jikwon
            where jikwon_jik='{0}'
        """.format(mem_job)
        cursor.execute(sql)
        datas=cursor.fetchall()
        
        if len(datas)==0:
            print(str(mem_job)+'직급은 없어요')
        
        for jikwon_no,jikwon_name,jikwon_jik,buser_num in datas:
            print(jikwon_no,jikwon_name,jikwon_jik,buser_num)       
        
    except Exception as e:
        print('err: ',e)
    finally:
        cursor.close()
        conn.close()
        
if __name__=='__main__':
    chulbal()   