NUM_BITS = 32

def reverse_bits(n):
    reversed_num = 0
    for i in range(NUM_BITS):
        j = n >> i & 1
        reversed_num += j << (NUM_BITS - i - 1)
    return reversed_num
    
def my_func_rev_bits(x):
	z = []
	retrn = ""
	for i in range(len(x)):
		if x[i] == '0':
			z.append(1)
		elif x[i] == '1':
			z.append(0)
	retrn = ''.join(str(elem) for elem in z)
	return retrn
		
u = my_func_rev_bits("110011")
print(u)
