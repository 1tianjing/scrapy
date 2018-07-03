import pymysql
db = pymysql.connect("localhost","root","bc123","pet_bbs",charset='utf8' )
def luntan():
    while True:
        print("欢迎来到宠物论坛\n管理员请选择1,\n用户请选择2,\n退出界面请选择其他")
        print('*'*25)
        p2 = int(input("请输入你要选择的序号："))
        print('+'*25)
        if p2 == 1:
            roots()
        elif p2 == 2:
            users()
        else:
            break
    db.close()
    print('*'*25)
def roots():
    cursor = db.cursor()
    params = input("请输入管理员账号:")
    sql = "SELECT * from roots where lname='%s'"%params
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id_name = row[0]
            lname = row[1]
            pwd = row[2]
            print('*'*25)
        while True:
            
            if lname == params:
                rpwd = int(input("请输入管理员密码："))
                if pwd == rpwd:
                    print("管理员登录成功")
                    print('*'*25)
                    while True:
                        print("管理员界面请选1,\n用户管理界面请选2,\n退出请选其他")
                        p1 = int(input('请输入你要选择的序号：'))
                        print('+'*25)
                        if p1 == 1:
                            while True:
                                print('注册管理员帐号请选1,\n删除管理员帐号请选2,\n修改管理员帐号请选3,\n查询管理员帐号请选4,\n退出管理员界面请选5.')
                                p = int(input('请输入你要选择的序号:'))

                                print('*'*25)
                                if p == 1:
                                    roots_a()
                                elif p == 2:
                                    roots_b()
                                elif p ==3:
                                    roots_c()
                                elif p == 4:
                                    roots_d()
                                elif p == 5:
                                    break
                        elif p1 == 2:
                            while True:
                                print('注册用户帐号请选1,\n删除用户帐号请选2,\n修改用户帐号请选3,\n查询用户帐号请选4,\n退出用户管理界面请选5.')
                                p = int(input('请输入你要选择的序号:'))
                                print('*'*25)
                                if p == 1:
                                    users_a()
                                elif p == 2:
                                    users_b()
                                elif p ==3:
                                    users_c()
                                elif p == 4:
                                    users_d()
                                elif p == 5:
                                    break
                        else:
                            break
                elif pwd == None:
                    print("管理员密码输入为空，请重新输入。")
                else:
                    print("管理员密码输入错误，请重新输入。")
            elif lname == None:
                print("管理员帐号输入为空，请重新输入。")
            else:
                print("管理员帐号输入错误，请重新输入。")
            break
            print('*'*25)
    except Exception as e:
        print("Error: unable to fetch data")
        print('*'*25)
def roots_a():
    cursor = db.cursor()
    a = str(input("请输入名字："))
    c = int(input('请输入密码：'))
    params = [a,c]
    sql = "INSERT INTO roots values(%s,%d);"
    try:
        cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def roots_b():
    cursor = db.cursor()
    params = input("请输入你要删除的名字：")
    sql = "delete from roots where lname='%s'"%params
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def roots_c():
    cursor = db.cursor()
    a = input("请输入你要修改的名字：")
    b = input("请输入你的新名字：")
    params = [b,a]
    sql = "update roots set lname=%s where lname=%s;"
    try:
        cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def roots_d():
    cursor = db.cursor()
    params = str(input("请输入你要查询的名字："))
    sql = "SELECT * from roots where lname='%s'"%params
    try:
        
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            a = row[1]
            b = row[2]
            print('帐号=%s,密码=%s'%(a,b))
            print('*'*25)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)   
        print('*'*25)     
def users_a():
    cursor = db.cursor()
    a = str(input("请输入名字："))
    b = int(input("请输入邮箱："))
    c = int(input('请输入密码：'))
    d = int(input('请输入生日：'))
    e = str(input('请输入性别：'))
    params = [a,b,c,d,e]
    sql = "INSERT INTO users values(%s,%d,%d,%d,%s);"
    try:
        cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def users_b():
    cursor = db.cursor()
    params = str(input("请输入你要删除的名字："))
    sql = "delete from users where uname='%s'"%params
    try:    
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def users_c():
    cursor = db.cursor()
    a = str(input("请输入你要修改的名字："))
    b = str(input("请输入你的新名字："))
    params = [b,a]
    sql = "update users set uname=%s where uname=%s;"
    try:
        count2 = cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def users_d():
    cursor = db.cursor()
    a = str(input("请输入你要查询的名字："))
    sql = "SELECT * from users where uname='%s'"%a
    try:
        
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            #uid = row[0]
            uname = row[0]
            email = row[1]
            pwd = row[2]
            birt = row[3]
            sex = row[4]
            
       # 打印结果
            print("名字=%s,邮箱=%d,密码=%d,生日=%d,性别=%s"%(uname,email,pwd,birt,sex))

        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # db.close()
    print('*'*25)
def users():
    cursor = db.cursor()
    sql = "SELECT * from users;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            uname = row[0]
            pwd = row[2]
        while True:
            params = str(input("请输入用户账户:"))
            if uname == None:
                print("用户帐号输入为空，请重新输入。")
            elif uname == params:
                rpwd = int(input("请输入用户密码："))
                if rpwd == None:
                    print("用户密码输入为空，请重新输入。")
                elif rpwd == pwd:
                    print("用户登录成功")
                    print('*'*25)
                    while True:
                        print("账户管理请选1\n信息管理请选2\n退出请选择其他")
                        p3 = int(input("请输入你要选择的序号："))
                        print('+'*25)
                        if p3 == 1:
                            while True:
                                print('注册用户帐号请选1,\n删除用户帐号请选2,\n修改用户帐号请选3,\n查询用户账号请选4,\n退出请选择其他')
                                p = int(input('请输入你要选择的序号:'))
                                print('+'*25)
                                if p == 1:
                                    users_a()
                                elif p == 2:
                                    users_b()
                                elif p ==3:
                                    users_c()
                                elif p == 4:
                                    users_d()
                                else:
                                	break
                        elif p3 == 2:
                            while True:
                                print("增加信息请选1,\n删除信息请选2，\n修改信息请选3,\n查询信息请选4,\n退出请选择其他")
                                p4 = int(input("请输入你要选择的序号:"))
                                print('+'*25)
                                if p4 == 1:
                                    message_a()
                                elif p4 == 2:
                                    message_b()
                                elif p4 == 3:
                                    message_c()
                                elif p4 == 4:
                                    message_d()
                                else:
                                    break
                        else:
                            break
                        break
                else:
                    print("用户密码输入错误，请重新输入。")
            else:
                print("用户帐号输入错误，请重新输入。")
            break
            print('*'*25)
    except Exception as e:
        print("Error: unable to fetch data")
        print('*'*25)
def message_a():
    cursor = db.cursor()
    a = str(input("请输信息标题："))
    b = str(input("请输入信息内容："))
    params = [a,b]
    sql = "INSERT INTO message values(0,%s,%s)"
    try:
        cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def message_b():
    cursor1 = db.cursor()
    params = str(input("请输入你要删除的信息标题："))
    sql = "delete from message where mname=%s;"
    try:    
        cursor1.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def message_c():
    cursor = db.cursor()
    a = str(input("请输入你要修改的信息标题："))
    b = str(input("请输入你新的信息标题："))
    params = [b,a]
    sql = "update message set mname=%s where mname=%s;"
    try:
        count2 = cursor.execute(sql,params)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)  
        print('*'*25)  
def message_d():
    cursor = db.cursor()
    a = str(input("请输入你要查询的信息标题："))
    sql = "SELECT * from message where mname='%s'"%a
    try:
        
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            mname = row[1]
            m_decl = row[2]
        
            print("信息标题=%s,信息内容=%s"%\
                (mname,m_decl))
            print('*'*25)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        print('*'*25)
def main():
    luntan()





if __name__ == "__main__":
    main()


