

def subs(s,t):
	count = 0
	subs_list = []

	for i in range(0, len(s)):

		if s[i:i+len(t)] == t[0:len(t)]:		 
			 subs_list.append(i+1)
			 print(i+1,end=" ")
		

	return subs_list

subs_list = subs("GTATTAGACGATTAGACATTAGACGTTAATTAGACTCCGGGAATTAGACAGCGGCAATTAGACCATTAGACGACATTAGACATTAGACGTTAATATTAGACATTAGACATTAGACTCATTAGACATTAGACTATATTAGACAATTAGACATTAGACCTTAAATTAGACGGATTAGACGGGTCTACCGCGCTAATTAGACATTAGACTATTAGACTATTAGACATATTAGACGTGACATTAGACCATTAGACCGATTAGACTATTAGACGCCCCGCGCGGGCAGAATTAGACGATTAGACATTAGACAATTAGACTTGATTAGACTCTATTAGACAGATTAGACATTAGACCTTATTAGACCTATTAGACCATTAGACATTCATAATTAGACTCCGGGATTAGACAAGATTAGACGATTAGACCGATTAGACTATTAGACATTAGACGTATTAGACCCGGAATTAGACTGCCATTAGACATTAGACTATTAGACATTAGACTCATTAGACAATTAGACTGACATTAGACTAATAGTTTACGAATTAGACAATAAGTCGATTAGACATTAGACATGAATTAGACAATTAGACCGCAGAGAGGTGATTAGACATATTAGACGTACATTAGACAATTAGACGATTAGACATTAGACTAGATTAGACATTAGACAAACATTAGACCCCCGAATTAGACGTAAGATTAGACACTGATTAGACGACCGAAGTATTAGACCCCATTAGACATTAGACATATTAGACTGATTAGACCCCATTAGACTTGTTACCCGATTAGACGATTAGACATTAGACATTAGACATAATTAGACGATTAGACATTAGACTCTATTAGACATTAGACCGATTAGACTAGATTAGACAATTAGACGATTAGACATTAGACATTAGACATGGATTAGACATTAGACGTCATTAGACAGCTATTAGACCCA","ATTAGACAT")
#print(subs_list)