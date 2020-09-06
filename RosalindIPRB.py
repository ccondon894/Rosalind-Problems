
def IPRB(k,m,n):
	total=k+m+n

	pr_Aa_aa = 0.5
	pr_Aa_Aa = 0.75

	event1AA = (k/total)*((k-1)/(total-1)) + (k/total)*(m/(total-1)) + (k/total)*(n/(total-1))
	event1Aa = (m/total)*((m-1)/(total-1))*pr_Aa_Aa + (m/total)*(k/(total-1)) + (m/total)*(n/(total-1))*pr_Aa_aa
	event1aa = (n/total)*(k/(total-1)) + (n/total)*(m/(total-1))*pr_Aa_aa

	return event1AA + event1Aa + event1aa 

output = IPRB(28,17,25)

print(output)


