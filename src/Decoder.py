import Register, Memory, Ula, ControlUnit
def decoderInstruction(instruction, program_counter):
	instruction = str(instruction)
	splitedInstruction = instruction.split(' ')
	return executeInstruction(splitedInstruction, program_counter)

def getValue(instruction, index, value):
	if Register.isRegister(value):
		return Register.load(value)
	elif Register.isRegisterZero(value):
		return 0
	elif Memory.isMemory(value):
		return Memory.load(value)
	elif value.isdigit():
		return value
	else:
		raise Exception(index+' argument in instruction '+instruction+' is defined incorrectly: {}'.format(value))

def setValue(name_instruction, first_argument, result):
	if Register.isRegister(first_argument):
		Register.store(first_argument, result)
	elif Memory.isMemory(first_argument):
		Memory.store(first_argument, result)
	else:
		raise Exception('First argument in instruction '+name_instruction+' is defined incorrectly: {}'.format(first_argument))

def executeInstruction(splitedInstruction, program_counter):

	name_instruction = splitedInstruction[0]
	if name_instruction == 'add' or name_instruction == 'mul' or name_instruction == 'sub' or name_instruction == 'div':
		first_argument = splitedInstruction[1]
		second_argument = splitedInstruction[2]
		third_argument = splitedInstruction[3]

		first_value = getValue(name_instruction, 'Second', second_argument)
		second_value = getValue(name_instruction, 'Third', third_argument)

		result = Ula.executeUla(name_instruction, int(first_value), int(second_value))

		setValue(name_instruction, first_argument, result)

		return False

	elif name_instruction == 'equal' or name_instruction == 'diff' or name_instruction == 'smaller' or name_instruction == 'greater':
		first_argument = splitedInstruction[1]
		second_argument = splitedInstruction[2]
		third_argument = splitedInstruction[3]

		first_value = getValue(name_instruction, 'First', first_argument)
		second_value = getValue(name_instruction, 'Second', second_argument)

		if Ula.executeUla(name_instruction, int(first_value), int(second_value)) == True:
			ControlUnit.setProgramCounter(third_argument+':')

		return False

	elif name_instruction == 'jmp':
		first_argument = splitedInstruction[1]
		ControlUnit.setProgramCounter(first_argument+':')
		return False

	elif name_instruction[-1] == ':':
		ControlUnit.setGoToMap(name_instruction, program_counter)
		return False

	else:
		return True



