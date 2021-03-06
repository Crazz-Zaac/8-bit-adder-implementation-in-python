def intoBinary(num):
	"""
	bin() function converts decimal to binary but does not return value in 8 
	bits. So we need to add the remaining zeros in order to make it 8 bits, for
	which the 'switcher' dictionary is created. For instance if bin() returns 
	3 bits data, remaining 5 zeros are concatenated.
	
	Input:
	'num' as integer.
	
	Returns:
	Corresponding binary value of 'num'
	"""
	val = bin(num).replace('0b', "") 
	switcher = {
		1:"0000000",
		2:"000000",
		3:"00000",
		4:"0000",
		5:"000",
		6:"00",
		7:"0",
		8:""
	}
	#returns either number of zeros as per length or the value itself
	if len(val) > 8:
		final_value = val
	else:
		final_value = switcher.get(len(val), val)+val
		print("Binary value of {}: ".format(num),final_value)
	return final_value #returns string value

def intoDecimal(n): #converts the incoming character into decimal
	"""
	Input: 
	String value as 'n'
	
	Returns: 
	Corresponding decimal value of 'n'
	"""
	return int(n,2) 


def xorGate(a, b):
	"""
	Input: 
	a, b
	Two 1 bit values as 1/0
	
	Returns:
	1 if a is not equal to b otherwise 0
	"""

	if a != b:
		return 1
	else:
		return 0

def xnorGate(a, b):
	"""
	Input: 
	a, b
	Two 1 bit values as 1/0
	
	Returns:
	Negation of the value returned by XOR gate
	"""

	val = xorGate(a, b)
	return notGate(val)

def andGate(a, b):
	"""
	Input: 
	a, b
	Two 1 bit values as 1/0
	
	Returns:
	1 if both incoming bits are 1 otherwise 0
	"""
	if a == 1 and b == 1:
		return 1
	else:
		return 0

def nandGate(a, b):
	"""
	Input: 
	a, b
	Two 1 bit values as 1/0
	
	Returns:
	Negation of the value returned by AND gate
	"""
	val = andGate(a, b)
	return notGate(val)


def notGate(n):
	"""
	Input: 
	n
	Single 1 bit value, either 1 or 0
	
	Returns:
	0 if input is 1 otherwise 0
	"""
	if n == 0:
		return 1
	else:
		return 0

def orGate(a, b):
	"""
	Input: 
	a, b
	Two 1 bit values as 1/0
	
	Returns:
	1 if both bits are one otherwise 0
	"""
	if a == 1 or b == 1:
		return 1
	else:
		return 0



def calculation(num1, num2):
	"""
	Input value is converted into binary and later changed into list, so as to
	take bits one by one from the last position (not necessarily to be changed 
	as string is also array of characters and can be accessed in the same 
	fashion). Bits are sent to different gates and as per the model. 

	Input:
	Two integer numbers
	num1, num2
	
	Returns:
	Final sum after adding the two numbers
	
	Variables used:
	c_in = carry in
	c_out = carry out
	pos = position from to take the bit from the list
	first_val = first list value of num1 after being converted into binary
	second_val = second list value of num2 after being converted into binary
	"""

	result = ""
	c_in = 0
	c_out = 0
	pos = -1
	first_val = list(intoBinary(num1))
	second_val = list(intoBinary(num2))
	print("First value {} (in binary): ".format(num1),first_val)
	print("Second value {} (in binary): ".format(num2),second_val)
	print("\n")
	for x in range(8):
		print("Adder: ",x+1)
		bit1 = int(first_val[pos]) #converting string into integer
		bit2 = int(second_val[pos])

		print("bit 1: ",bit1)
		print("bit 2: ",bit2)
		
		xor_1  = xorGate(bit1, bit2)
		print("XOR gate value: ", xor_1)

		nand_1 = nandGate(xor_1, c_in)
		print("NAND gate value: ", nand_1)
		or_1 = orGate(xor_1, c_in)
		print("OR gate_1 value: ", or_1)
		sum_val = andGate(or_1, nand_1)
		print("sum_val value: ", sum_val)

		and_1 = andGate(bit1, bit2)
		print("AND gate_1 value: ", and_1)
		and_2 = andGate(xor_1, c_in)
		print("AND gate_2 value: ", and_2)

		xnor_1 = xnorGate(and_1, and_2)
		print("XNOR gate_1 value: ", xnor_1)
		c_out = notGate(xnor_1)
		print("Carry out value: ", c_out)

		result = str(sum_val) + result
		print("Result: ", result)
		c_in = c_out
		print("New carry in: ", c_in)
		pos -= 1
		print("Position value: ",pos)
		print("\n")

	result = str(c_out) + result
	answer = intoDecimal(result)
	print("\n\nSum: ", answer)
	return answer


if __name__ == '__main__':
	while True:
		num1 = input("Enter first number(0-255): ")
		num2 = input("Enter second number(0-255): ")
		try:
			#confirming that the input is not string
			num1 = int(num1)
			num2 = int(num2)

			#confirming that the value lies exactly between 0 and 255
			if (num1 <= 255 and num2 <= 255) and (num1 >= 0 and num2 >= 0):
				calculation(num1, num2)
			else:
				print('Expected value between 0 and 255. But {} and {} was given.'
				.format(num1, num2))
		
		except (ValueError, AttributeError):
			print('Expected integer value between 0 and 255. But {} and {} was given.'
			.format(num1, num2))

		choice = input("Do you want to continue? y/n: ")
		if choice == "n":
			break
