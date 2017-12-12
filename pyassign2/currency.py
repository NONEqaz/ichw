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
    assert("United States Dollars" in jstr)
    get_string("UUU","EEE","2.5")
    assert("invalid" in jstr) #简单判断是否得到正确字符串
def get_consequence(amt): #分离出结果的函数
    global l
    l=jstr[(12+len(amt)):] #字符串切片去除前面的输入数据
    con=""
    for eachChar in l:
        if eachChar in "0123456789.":
            con=con+eachChar  #得到后面需要的数据的字符串
    global c
    c=float(con) #转换成浮点数
def test_get_consequence():
    get_string("USD","EUR","2.5")
    get_consequence("2.5")
    assert(l[0] in " ") #简单判断切片是否成功
def exchange(source,target,amt): #执行的函数
    get_string(source,target,amt)
    get_consequence(amt)
def test_all():
    """test all cases"""
    test_get_string()
    test_get_consequence()
    print("All tests passed")
test_all() #测试
currency_from=str(input("请输入来源货币缩写:"))
currency_to=str(input("请输入目标换算货币缩写:"))
amount_from=str(input("请输入来源货币金额：")) #输入数据
exchange(currency_from, currency_to, amount_from) #执行
print("换算金额为:",c) #输出结果
    
    