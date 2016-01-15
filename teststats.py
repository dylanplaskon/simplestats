from stats import mean
from nose.tools import assert_equal, assert_almost_equals

def test_mean():	
	assert_equal(mean([2, 4]), 3.0)
#test_mean()
	
def test_empty_list():
	assert_equal(mean([]), 0.0), 'need to handle empty lists'
#test_empty_list()

def test_float():
	assert_almost_equals(mean([0.5, 0.5, 1]), 0.66666666), 'float is bad'
#test_float()

def test_str_list_mean():
	assert_equal(mean(['1', '2', '3']), 2.0), 'strings are bad'
#test_str_list_mean()