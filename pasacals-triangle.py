times = 0
def ghy(number,limit):
	global times
	if (times <= int(limit)):
		newnumlis = ["1"]
		for i in range(len(number)-1):
			newnum = int(number[i]) + int(number[i+1])
			newnumlis.append(str(newnum))
		newnumlis.append("1")
		times += 1
		print(" ".join(newnumlis))
		ghy(newnumlis,limit)
inpu = input("Enter a Limit:")
print("1")
print("1 1")
ghy("11",inpu)	
		
	
