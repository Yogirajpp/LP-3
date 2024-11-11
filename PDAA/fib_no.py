def rec_fib(n):
	if n<=1 :
		return n
	else :
		return rec_fib(n-1) + rec_fib(n-2)

def non_rec_fib(n):
	first=0
	second=1
	print(first)
	print(second)
	while n-2>0:
		third = first + second
		first=second
		second=third
		print(third)
		n-=1

if __name__ == "__main__":
	n=int(input("enter number of terms u need in fib seq"))
	
	print("\nrec_fib:")
	for i in range(n):
		print(rec_fib(i))
	print("\nnon_rec_fib:")
	print(non_rec_fib(n))







