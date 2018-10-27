def executeUla(name_instruction, first_value, second_value):
	if name_instruction == 'add':
		return first_value + second_value
	elif name_instruction == 'mul':
		return first_value * second_value
	elif name_instruction == 'sub':
		return first_value - second_value
	elif name_instruction == 'div':
		return first_value / second_value
	elif name_instruction == 'equal':
		if first_value == second_value:
			return True
		else:
			return False
	elif name_instruction == 'diff':
		if first_value != second_value:
			return True
		else:
			return False
	elif name_instruction == 'smaller':
		if first_value < second_value:
			return True
		else:
			return False
	elif name_instruction == 'greater':
		if first_value > second_value:
			return True
		else:
			return False


