import math

def RabbitCalc(n,k):

	pairDic ={ 1: 1, 2: 1}
	total_pairs = 1
	for i in range(3,n+1):
		print(i)
		total_pairs = total_pairs + (pairDic[i-2]*k)
		pairDic[i] = total_pairs

	return pairDic, total_pairs

pairDic,total_pairs = RabbitCalc(32,3)
print(total_pairs)