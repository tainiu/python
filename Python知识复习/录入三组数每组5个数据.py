###分别录入三组数据:使用循环控制，每组录入5个数据。录入结束，能够打印出所有信息。

all_list = [[],[],[]]
for i in range(0,3):
    list = all_list[i]
    for j in range(0,5):
        num = input("请输入第%d组的第%d个信息：\n"%(i+1,j+1))
        list.append(num)
print(all_list)
