import Memory, Decoder, Register, Cache
	
programCounter = 0
goToMap = {}
debug = True

def incrementProgramCounter():
	global programCounter
	programCounter += 1

def setProgramCounter(key):
	global programCounter
	programCounter = goToMap[key]

def setGoToMap(key, program_counter):
	goToMap[key] = program_counter

def executeProgram(memory_dictionary):
	
	for i in range(len(memory_dictionary)):
		if Decoder.decoderInstruction(Memory.loadInstruction('M['+str(programCounter)+']'), programCounter):
			Memory.flush()
			Register.flush()
			Cache.flush()
			print('Cache Miss')
			print(Cache.cache_miss)
			print('Cache Hit')
			print(Cache.cache_hit)
			print('Program was finished!')
			return
		if debug:
			Memory.flush()
			Register.flush()
			Cache.flush()
		incrementProgramCounter()

def initControlUnit(file_path):
	instructions = open(file_path)

	read_instructions = instructions.read()
	line_instructions = read_instructions.splitlines()

	for i in range(len(line_instructions)):
		Memory.store('M['+str(i)+']', line_instructions[i])

	Memory.setPayload(len(line_instructions))
	memory_dictionary = Memory.getMemory()
	executeProgram(memory_dictionary)




