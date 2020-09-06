

def printArray(a, n):

	for i in range(n):
		print(a[i],end =" ")
	print()

#generate permutations using Heap's algorithm
# a = array 
# n = length of array a
def heap_perm(a, size, n):

	#if size becomes 1 then prints the permutation
	if (size == 1):
		printArray(a, n)
		return

	for i in range(size):

		heap_perm(a, size-1, n);
		#if size is odd, swap first and last
		#if size is even, swap ith and last element
		if size&1:
			a[0], a[size-1] = a[size-1], a[0]
		else:
			a[i], a[size-1] = a[size-1], a[i]

a = [1, 2, 3, 4, 5, 6]
n = len(a)
fact = 1
for i in range(1,n+1):
	fact = fact * i


print(fact)
heap_perm(a,n,n)


