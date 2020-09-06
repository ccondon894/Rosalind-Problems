
def Hamm(a,b):

	n = 0

	for i in range(len(a)):
		if a[i] != b[i]:
			n += 1

	return n 

a = "TGTCATGTGCTAGGGAGTTCGTAATGGGTAATACTTTCCTTGCAGCCCATGTTTAGAGGACAAAGACATGACAAGCGCGTCCGGTCCCTCGGAGGGTAAACCCAGGACTTTCCTGCCGATGAGCGGACAAGAAGGTCTAGGCCTGAGATCCTGGTTCTAAGAGGGCTTGCGCGCCCGAGTCATATGCTTCTGGTAACCGTTCACTGTGTAGTATAAGTGAAGCAATACAGCCTGACCTGCGTTATAGGCTCGAGAATTCAGGACCTTAACGTCTGAGACTTCCGTGAAGTCCGTTGCAAATGTTATCACTCTCTCAGAAGGGGTAAAACATCAGCGGACTGCTCTTGGCGAATATACCAGTGTACAAGCCTTGTAGCGTCCGCTTCTCAGATGCTGATCTTACGCATGTGTGTCCTGTGTCGGCGCCGTTCTGTGTACTATTCTAGCAAATGTACGCCTTTATGAACCTAGAGCGGTTGTTAAGTTTCCCCCGCTAAAAATGCCTGTCCGCGGATCGTGGGCGTTCCTTCTTTCCCTTATTACATTACCGGACCTACTGGTTTCGGATCTGTGTATAACAAAAGTCTACGAAAAAGGCAAATTGTTACGAGATCATAGTAAAGCCGTCAGTCGTATACAGTTGACCGGAACTTGTATGTATCTAGATTTAGCACCACGTATTGGTTCCACTTATGAGTGTCTATGTCCATTTCCGAGTACGACCGACTGGGTGTTCAATGGGCCTTCTACAAGCGCGCCTCCTTATTAAGAAGTGATACGTGACGGCATGGCTAATGGGCCTTACAATCGGTGAACCAGGTAACGTGGGTCGCGCTGCTCCAGCGTCATCATAGACCGCGAGGCTGTCCCTGGGTGATGAATAATATCACAGCTTTCACGGCCAATCACGACATAGTA"
b = "ATCCGCGTTTAACTGAACTCGTAACAGTTTATATCTTATTTATAGAACAAGATTTAAGGGCTGAGGGCAGATAATCAACGCTGGTAGCTTACTTATTGGGTGAAGTAAATTGCCGCCGTCGCACAGACGAGCACCATTAGGCACCAGAACCTGGGTTGAGCATGGCCTGCGCACCGACGAGTCATGCTATCGGAAACCGTTGAGAACGCGCTCCAAAAGTCGCAATACATGCTTACATGGGCTCTACGCTTGGTTACGGCACTCCTCTTAGGTTTACTCCGGTAAGAAATTGGTTCCACGTGGGTTTAGTGTCTAGGGAGGGAAACACCTTCAAAGGGCGGGAGTGGGCTAAGCTAACCGCACATAGGCAGAACAGCGTCTGTATCAGAAGTTCAGGTAATACGCATGTGTGTACGGCGTGGCCGTCCACCTGGGAACTCAGTTATTCCTCGGCAGTGCTAATTTCTCAGGGACAGATTTTCATAATCGTCCGTTAAAAATGCGTCCCCGGATGTTGGGCCCTTTACTTCGGCCCCATCGTAAATATTTGCGCCTTCCGCTTTTGGATATATACATCAAAAAAGGCGACGGGAAGCATCCGTTGGGACGTGATCCTGTTCACTCCGTTATGCTTATCCCGAGTGCCGGAGCTCGTCTACCCCCAGATTTAGACTCAAGGATTGATTCCTTTTAGGAGTAACTTGGGCCATTGTCGAGCAAGAGTGACGGAGTATTTAACAATACGTAGATAAGCTCGGAATAGCATTTAGTAGTGATACGTGCCAGCATACCTGAGCGTCCTGACTCGATGTGATACGGAGACACTAGCTGTCGCTGCACCTTCGTCGTGAGAGTACACGAACCTGACGTTTCCGCTCTCATGCAAGTACATCCCCCCCACCCATTCTGAATATATTA"

print(len(a))
print(len(b))

n = Hamm(a,b) 
print(n)