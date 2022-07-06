import MySQLdb
import pickle
with open('mydb.dat', mode='rb') as obj:
    config=pickle.load(obj)
    
def login():
    try:
        conn=MySQLdb.connect(**config)
        cursor=conn.cursor()
        
        mem_no=input('사번: ')
        mem_name=input('직원명: ')
        
        sql="""
            select jikwon_name
            from jikwon
            where jikwon_no={0} 
        """.format(mem_no)
        cursor.execute(sql)
        jik_name=cursor.fetchone()  # cursor.fetchall()
        
        if mem_name==jik_name[0]:
            print('로그인 성공')
            sql="""
                select gogek_no,gogek_name,gogek_tel
                from gogek
                where gogek_damsano={0}
            """.format(mem_no)
            cursor.execute(sql)
            gogeks=cursor.fetchall()
          
            print('고객번호\t','고객명\t','고객전화\t')
            for gogek_no,gogek_name,gogek_tel in gogeks:
                print(str(gogek_no)+'\t'+str(gogek_name)+'\t'+str(gogek_tel))
            print('인원 수 : '+str(len(gogeks))+'명')
        
        else:
            print('로그인 실패')
    except Exception as e:
        print('err: ',e)
    finally:
        cursor.close()
        conn.close()

if __name__=='__main__':
    login()