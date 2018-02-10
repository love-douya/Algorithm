from time import sleep
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
a = power(5)
print(a)
sleep(1)
