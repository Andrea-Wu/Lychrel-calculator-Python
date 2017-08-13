import sys 

#in this program, all functions return numbers in string format. 
#this might lead to errors in other scenatios, but this program only deals with whole numbers.

def reverseString(num):
	#create a number string that is reverse of num called revNum
	List = [] 
	for digit in num: 
		List.append(digit)

	List.reverse()

	revNum = ""
	for number in List:
		revNum += number

	return revNum


def addPalindrome(num):
	#num is a string of digits ok

	#create a string that is reverse of num called revNum
	revNum = reverseString(num)

	#convert num and revNum to integers
	intNum = int(num)
	intRevNum = int(revNum)
	
	#add num and revNum
	intSum = intNum + intRevNum
	
	return str(intSum)


def isPalindrome(num):
	revNum = reverseString(num)
	if num == revNum:
		return 1

	return 0

	

def lychrel(number, times):
	print("original number: " + str(number))
	currTime = 0
	while currTime < int(times):
		number = addPalindrome(number)
		currTime = currTime + 1
		print("iteration: " +str(currTime) + ", number: " + number)
		if isPalindrome(number):
			print("number: " + number + ". DONE")
			break;
		 

if __name__ == '__main__':
	lychrel( str(sys.argv[1]), sys.argv[2] ) 
