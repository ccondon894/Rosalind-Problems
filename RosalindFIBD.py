

def rabbits(n,m):

	ages = [0] * m
	#start with one rabbit pair with m months to live
	ages[-1] = 1

	for i in range(1, n):
		#print("month: " + str(i))
		#amount of newborns born this month
		new_rabbits = sum(ages[:-1])
		#print("before update: ")
		#print(ages)
		#shift all rabbits down one month
		ages[:-1] = ages[1:]
		#print("after all rabbits are shifted: ")
		#print(ages)
		#assign newborns(old rabbits get deleted during this step since they were shifted to this spot during previous line)
		ages[-1] = new_rabbits
		#print("after newborn rabbits are assigned: ")
		#print(ages)

	return sum(ages)

f = rabbits(87,20)
print(f)