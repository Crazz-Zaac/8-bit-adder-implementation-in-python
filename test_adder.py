from adder import calculation

def test_calculation():
	assert (calculation(0, 0) == 0) #minimum value, passes 
	assert (calculation(12, 15) == 27) #normal value, passes
	assert (calculation(255, 255) == 510) #maximum value, passes
	assert (calculation('string', 45)) #must fail
	assert (calculation(0.5, 12.5) == 13) #must fail
	assert (calculation(-25, 15) == -10) #must fail