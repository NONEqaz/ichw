def get_string(source,target,amt): #在线得到汇率换算结果的函数
    t="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=" + source + "&to=" + target + "&amt=" + amt
    #得到需要的url
    from urllib.request import urlopen
    doc = urlopen(t)
    docstr = doc.read()
    doc.close()
    global jstr
    jstr = docstr.decode('ascii') #从url获得数据并转换为字符串(方法来自作业)
def test_get_string():
    get_string("USD","EUR","2.5")
    assert("true" in jstr)
    get_string("UUU","EEE","2.5")
    assert("invalid" in jstr) #简单判断是否得到正确字符串
def get_result(jstr): #分离出结果的函数
    l=jstr.find("to")
    To=jstr[(l+7):] #去除所需结果前面的部分
    m=To.find(" ")
    global con
    con=To[:m] #去除所需结果后面的部分
def test_get_result():
    get_result('to" : "3.1415926 god')
    assert(con in "3.1415926")    #测试是否得到正确数据
def check_the_result(): #检查
    if "invalid" in jstr:
        print("你输入的货币缩写或金额有误!") #输出错误
    else:
        print("换算金额为:",con)  #输出结果
    #判断型函数，不写assert了
def exchange(source,target,amt): #执行的函数
    get_string(source,target,amt)
    get_result(jstr)
    check_the_result()
def test_all():
    """test all cases"""
    test_get_string()
    test_get_result()
    print("All tests passed")
test_all() #测试
currency_from=str(input("请输入来源货币缩写:"))
currency_to=str(input("请输入目标换算货币缩写:"))
amount_from=str(input("请输入来源货币金额：")) #输入数据
exchange(currency_from, currency_to, amount_from) #执行
    
    