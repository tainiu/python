#请将hello22hewe278字符串的数字取出，并输出成一个新的字符串。

str = "hello22hewe278"
num = ''
for s in str:
    #判断字符串里每个字符是否为数字
    if s.isdigit():
        #将得到的数字进行拼接.
        num += s
print(num)