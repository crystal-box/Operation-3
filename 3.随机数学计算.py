import random
fuhao=['+','-','*','/']
zhengquelv=[]
for i in range(1,11):
    a = random.randint(1, 101)
    b = random.randint(1, 101)
    fuhao_choice=random.choice(fuhao)
    result=str(a)+fuhao_choice+str(b)+"="
    result1 =eval(str(a)+fuhao_choice+str(b)) #eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    print(result,"\t",end="")
    user_result =float(input("请输入结果:"))
    if user_result == result1:
        print("回答正确")
        zhengquelv.append(1)
    else:
        print("回答错误")
print("正确率为：{:.2%}".format(len(zhengquelv)/10))