count = 1
while True:
    num = int(input("请输入1--20之间的数"))
    if num >= 1 and num <= 20:
        print('你已经输入%d个数字了,输入够十个会结束,你输入的数字是%s'%(count,num))
        count += 1
        if count > 10:
            print("你已经输入够10个了程序结束")
            break
    else:
        print("你输入的有误,请重新输入:")
