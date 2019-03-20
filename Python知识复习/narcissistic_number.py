
##输入一个100-999之间的数，判断是否是水仙花数

number = int(input("输入一个100-999之间的数:\n"));

		
for number in range(100,1000):
	#123
	ge =  number %10;#3
	#print(ge);
	shi = number // 10 %10;#2
	#print(shi);
	bai = number // 100 %10;#1
	#print(bai);
	if ge**3+shi**3+bai**3 == number:
		print("%d这个数是水仙花数！"%number);
	#else:
		#print("%d这个数不是水仙花数！"%number);