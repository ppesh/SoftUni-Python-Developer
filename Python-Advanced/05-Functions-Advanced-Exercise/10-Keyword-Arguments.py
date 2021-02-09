# 10. Keyword Arguments
def kwargs_length(**kwargs):
	return len(kwargs)


# Test Code:
dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))














