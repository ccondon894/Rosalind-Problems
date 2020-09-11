#Rosalind Problem IEV: http://rosalind.info/problems/iev/

def readFile(filename):

	infile = open(filename, "rU")
	pairs = infile.read()
	#split each number into list
	pairs = pairs.split(" ")
	#convert numbers from string to int 
	pairs = [int(i) for i in pairs]

	#probability list of the likelihood of dominant trait for each allele pair
	prob = [1, 1, 1, 0.75, 0.5, 0]
	
	#calculate expected num of offspring that show dominant trait
	calc_prob = [2*x*y for x,y in zip(pairs,prob)]
	

	print(sum(calc_prob))

readFile('rosalind_iev.txt')