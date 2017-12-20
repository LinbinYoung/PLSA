from random import gammavariate
from random import random

def Dirichlet(alpha):
	sample = [gammavariate(a,1) for a in alpha]
	samlpe = [v/sum(sample) for v in sample]
	return sample

def normalize(vec):
	s = sum(vec)
	assert(abs(s)!=0.0)
	for i in range(len(vec)):
		assert(vec[i]>=0) #it means that each element must  >= 0
		vec[i] = vec[i]*1.0/s

def choose(vec,pr):
	assert(len(vec) == len(pr))
	# normalize the distributions
	normalize(pr)
	r = random()
	index = 0
	while (r>0): 
		r = r - pr[index]
		index = index + 1
	return vec[index-1]
if __name__ == "__main__":
	print Dirichlet([1,1,1])