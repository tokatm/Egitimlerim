# Function for nth Fibonacci number
'''import math

def fn (n):
    fnb = (((1 + math.sqrt(5))/2)**n - ((1 - math.sqrt(5))/2)**n) / math.sqrt(5)
    return fnb

print (fn(4))


def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


alt = Fibonacci(1) * Fibonacci(5)
print('Genel sonuc:', 1/alt)'''


'''def math():
	for i in range(100000,100999):
		if i%9127==0:
			print(i)

math()'''

'''amount = range(24,1000)'''
def change(amount):
	assert(amount>=24)
	if amount == 24:
		return [5,5,7,7]
	if amount == 25:
		return [5,5,5,5,5]
	if amount == 26:
		return [5,7,7,7]
	if amount == 27:
		return [5,5,5,5,7]
	if amount == 28:
		return [7,7,7,7]
	if amount == 29:
		return [5,5,5,7,7]
	if amount == 30:
		return [5,5,5,5,5,5]

	coins = change(amount -7)
	coins.append(7)
	print (coins)
	return coins

change(100)