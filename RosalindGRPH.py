#Rosalind Problem GRPH: http://rosalind.info/problems/grph/


#input is fasta file of sequence header followed by sequence on following lines
#output is dict of {sequence header : sequence} 
def readFile(filename):

	#open file, create list of lines in txt file
	#create empty dict to contain seq header + seq
	seq_dict = {}
	infile = open(filename,"rU")
	lines = infile.readlines()

	lines = [line.strip('\n') for line in lines]

	#headers are every 3 lines in file, so pull every 3rd line
	headers = [x for x in lines[0::3]]
	#concatenate sequences into new list 
	sequences = [x+y for x,y in zip(lines[1::3], lines[2::3])]
	

	for i in range(len(headers)):
		#Get rid of '>' at start of header
		headers[i] = headers[i][1:]

		#join header and sequence in dictionary
		seq_dict[headers[i]] = sequences[i]

	return seq_dict

#iterate through each key in dictionary, comparing if seq suffix matches prefix of any other key  
def findOverlap(seq_dict):

	for key in seq_dict:

		for i in seq_dict:
			
			if seq_dict[key][-3:] == seq_dict[i][0:3] and seq_dict[key] != seq_dict[i]:
				print(key,i)


seq_dict = readFile('rosalind_grph.txt')

findOverlap(seq_dict)

