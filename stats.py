def mean(vals):
	"""Calculate the arithmetic mean of a list of numbers in vals"""
	assert type(vals) is list, 'input must be list'
	ivals = []
	for n in vals:
		ivals.append(float(n))
		
	if ivals == []:
		return 0
	else:
		total = sum(ivals)
		length = len(ivals)
		return total/length

	print(ivals)
	
#print(mean("hello"))