
numbers = list()

def initializeList():
	f = open("input.txt", "r")
	for x in f:
		numbers.append(int(x))
  

def findSumOfTwo(sumNumber):
  i = int(0)
  sumNum = int(sumNumber)
  for num in numbers:
		i = i + 1
		#print str(i) + " check  " + str(num)

		for check in numbers[i:]:
			#print str(check)
			if num + check == sumNum:
				print " Found: " + str(num) + " + " + str(check) + " = " + str(sumNum) + " ==> " + str(num * check)
			
def findSumOfThree(sumNumber):
  i = int(0)
  j = int(0)
  sumNum = int(sumNumber)
  for num in numbers:
		i = i + 1
		#print str(i) + " check  " + str(num)
		for check in numbers[i:]:
			j = 0
			#print str(check)
			for three in numbers[j:]:
				if num + check + three == sumNum:
					print " Found: " + str(num) + " + " + str(check) + " + " + str(three) + " = " + str(sumNum) + " ==> " + str(num * check * three)

initializeList()
findSumOfTwo(2020)
findSumOfThree(2020)

print numbers
