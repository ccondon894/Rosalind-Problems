
def readFile(filename):
	 
	#open file, get sequences and sequence length
	prevLine = ""
	sequence_list = []
	newSeq = ""
	infile = open(filename,'rU')
	lines = infile.readlines()
	last = lines[-1]
	for line in lines:
	 	if (line[0] != ">" and prevLine[0] == ">"):  
	 		#grab entire sequence and add as element in list
	 		#strip /n newline at end of each line
	 		sequence_list.append(newSeq)
	 		newSeq = "" + line.strip()

	 		if line is last:
	 			sequence_list.append(newSeq)


	 	elif line[0] != ">" and prevLine[0] != ">":
	 		newSeq = newSeq + line.strip()

	 		if line is last:
	 			sequence_list.append(newSeq)

	 	prevLine = line
	 	#print(newSeq)

	sequence_list.remove(sequence_list[0])
	#print("Number of sequences: " + str(len(sequence_list)))
	#print(sequence_list)

	#each sequence should be the same length, so just grab length of 1 sequence
	sequence_len = len(sequence_list[0])
	return sequence_list, sequence_len

def profileMatrix(sequence_list, sequence_len):
	#make lists of len = sequence length all equal to 0
	Alist = [0] * seq_len
	Clist = [0] * seq_len
	Glist = [0] * seq_len
	Tlist = [0] * seq_len

	#navigate thru each sequence 
	#print(sequence_list)
	for sequence in sequence_list:
		
		#update profile matrix rows at each index of seq length 
		for i in range(len(sequence)):
			if sequence[i] == 'A':
				Alist[i] = Alist[i] + 1

			elif sequence[i] == 'C':
				Clist[i] = Clist[i] + 1

			elif sequence[i] == 'G':
				Glist[i] = Glist[i] + 1

			elif sequence[i] == 'T':
				Tlist[i] = Tlist[i] + 1

	#create a max list that grabs the max number of each column in profile matrix
	max_list = [max(a,c,g,t) for a,c,g,t in zip(Alist,Clist,Glist,Tlist)]
	#print(max_list)
	cons_seq = ""
	
	#match max number with corresponding list to determine nucleotide
	#if 2 lists have the same max number at an index just take either one.
	for i in range(len(max_list)):
		
		if max_list[i] == Alist[i]:
			cons_seq = cons_seq + 'A'
		elif max_list[i] == Clist[i]:
			cons_seq = cons_seq + 'C'
		elif max_list[i] == Glist[i]:
			cons_seq = cons_seq + 'G'
		elif max_list[i] == Tlist[i]:
			cons_seq = cons_seq + 'T'

	#print(cons_seq)
	#print("Consensus sequence length is: " + str(len(cons_seq)))

	return Alist, Clist, Glist, Tlist, cons_seq 


seq_list, seq_len = readFile('rosalind_cons.txt')
#print("Sequence length is: " + str(seq_len))
Alist, Clist, Glist, Tlist, cons_seq = profileMatrix(seq_list,seq_len)

#convert each list to a string to create profile matrix
strA = "A: " + " ".join([str(elem) for elem in Alist])
strC = "C: " + " ".join([str(elem) for elem in Clist])
strG = "G: " + " ".join([str(elem) for elem in Glist])
strT = "T: " + " ".join([str(elem) for elem in Tlist])

f = open("rosalind_cons_output.txt","w")
f.write(cons_seq + "\n")
f.write(strA + "\n")
f.write(strC + "\n")
f.write(strG + "\n")
f.write(strT)
f.close()

h = open('rosalind_cons.txt',"rU")

strands = [x.strip() for x in h.readlines()]
#print(strands)
matrix = zip(*strands)
#print(list(matrix))
profile_matrix = map(lambda x: dict((base, x.count(base)) for base in "ACGT"), matrix)
print(list(profile_matrix))

'''
print(strA)
print(strC)
print(strG)
print(strT)
'''