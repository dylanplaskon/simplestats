def mean(vals):
	"""Calculate the arithmetic mean of a list of numbers in vals"""
	assert type(vals) is list, 'input must be list'
	
	total = sum(vals)
	length = len(vals)
	return total/length

def test_mean():	
	assert mean([2,4]) == 3.0
test_mean()
	
#print(mean("hello"))