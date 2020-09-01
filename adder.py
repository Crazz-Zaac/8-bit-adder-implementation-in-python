# from tests import run_tests
def intoBinary(num):
	val = bin(num).replace('0b', "") #converts decimal into binary
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
		print("returning value: ",final_value)
	return final_value #returns string value

def intoDecimal(n): 
    return int(n,2) 


def xorGate(a, b):
	if a != b:
		return 1
	else:
		return 0

def xnorGate(a, b):
	val = xorGate(a, b)
	return notGate(val)

def nandGate(a, b):
	val = andGate(a, b)
	return notGate(val)
	#if a == 1 and b == 1:
	#	return 0
	#else:
	#	return 1

def andGate(a, b):
	if a == 1 and b == 1:
		return 1
	else:
		return 0

def notGate(n):
	if n == 0:
		return 1
	else:
		return 0

def orGate(a, b):
	if a == 1 or b == 1:
		return 1
	else:
		return 0



def calculation(num1, num2):
	result = ""
	c_in = 0
	c_out = 0
	pos = -1
	first_val = list(intoBinary(num1))
	second_val = list(intoBinary(num2))
	print("First value: ",first_val)
	print("Second value: ",second_val)

	for x in range(8):
		bit1 = int(first_val[pos]) #converting into integer
		bit2 = int(second_val[pos])

		print(bit1)
		print(bit2)
		
		xor_1  = xorGate(bit1, bit2)
		print("xor gate value: ", xor_1)

		nand_1 = nandGate(xor_1, c_in)
		print("nand gate value: ", nand_1)
		or_1 = orGate(xor_1, c_in)
		print("or_1 gate value: ", or_1)
		sum_val = andGate(or_1, nand_1)
		print("sum_val value: ", sum_val)

		and_1 = andGate(bit1, bit2)
		print("and_1 value: ", and_1)
		and_2 = andGate(xor_1, c_in)
		print("and_2 gate value: ", and_2)

		xnor_1 = xnorGate(and_1, and_2)
		print("xnor_1 gate value: ", xnor_1)
		c_out = notGate(xnor_1)
		print("c_out value: ", c_out)

		result = str(sum_val) + result
		print("Result: ", result)
		c_in = c_out
		print("New c_in: ", c_in)
		pos -= 1
		print(pos)

	result = str(c_out) + result
	answer = intoDecimal(result)
	print("Output: ", answer)
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
				print('Expected value between 0 and 255. But {} and {} was given.'.format(num1, num2))
		
		except (ValueError, AttributeError):
			print('Expected integer value between 0 and 255. But {} and {} was given.'.format(num1, num2))

		choice = input("Do you want to continue? y/n: ")
		if choice == "n":
			break
