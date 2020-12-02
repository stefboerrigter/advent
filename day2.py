#from parse import parse
import re

passwords = list()

def initializeList():
	f = open("password.txt", "r")
	r = re.compile('[ \-\t\n\r:]+')
	for x in f:
		result = r.split(x)
		#print(result)
		value = {"min" : result[0],
						 "max" : result[1],
						 "letter" : result[2],
						 "password" : result[3]}
		passwords.append(value)

def validatePasswords():
	countValidPasswords = 0
	for password in passwords:
		#print (password)
		passwd = password["password"]
		letter = password["letter"]
		minVal = password["min"]
		maxVal = password["max"]
		count = 0
		for l in passwd:
			if l == letter:
				count = count + 1
		if count >= int(minVal) and count <= int(maxVal):
			#print(passwd + " contains " + letter + " within limits" + minVal + " <> " + maxVal)
			countValidPasswords = countValidPasswords + 1
	print("Task 1 Found %d valid passwords" % countValidPasswords)


def validatePasswords2():
	countValidPasswords = 0
	for password in passwords:
		#print (password)
		passwd = password["password"]
		letter = password["letter"]
		firstVal = password["min"]
		secondVal = password["max"]
		found = 0
		if passwd[int(firstVal)-1] == letter:
			#print("first letter is OK {} [{}]".format(passwd, letter))
			found = found + 1
		if passwd[int(secondVal)-1] == letter:
			#print("second letter is OK {} [{}]".format(passwd, letter))
			found = found + 1
		if found == 1:
			#print("One letter is OK {} [{}] [{} - {}]".format(passwd, letter, firstVal, secondVal))
			countValidPasswords = countValidPasswords + 1
	
	print("Task 2 Found %d valid passwords" % countValidPasswords)

initializeList()

validatePasswords()
validatePasswords2()
