from stats import mean

def test_mean():	
	assert mean([2,4]) == 3.0
test_mean()
	
def test_empty_list():
	assert mean([]) == 0.0, 'need to handle empty lists'
test_empty_list()

def test_float():
	assert mean([0.2, 0.4]) == 0.3, 'float is bad'
test_float()