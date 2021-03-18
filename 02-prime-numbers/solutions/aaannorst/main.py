'''decide if the numbers on the list are primes'''
import sys

# open text wile with numbers
f = open(sys.argv[1], 'r')
sample = f.readlines()
f.close()

# sort numbers
for line in sample:
	if line.strip() ==  "":
		continue

	num = float(line.strip())

	is_prime = "1"
	if num == 0:
		is_prime = "-"
	elif num/(int(num)) != 1:
		is_prime = "-"
	elif num < 0:
		is_prime = "-"
	elif num == 1:
		is_prime = "0"
	elif num == 2 :
		is_prime = "1"
	elif num%2 == 0:
		is_prime = "0"
	else:
		guard = int(num/2)
		for n in range(3, guard, 2):
			if num%n == 0:
				is_prime == "0"
				break
	print("{} {}".format(num, is_prime))






