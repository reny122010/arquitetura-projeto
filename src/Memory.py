import re
memory_dictionary = {}
payload = 0

def initMemory(amount_memory):
	memory = open("../data_handler/memory.txt", "w+")
	for x in xrange(0, amount_memory):
		memory.write("%s %s\n" % ('M['+str(x)+']', 0))
		memory_dictionary['M['+str(x)+']'] = '0'

def setPayload(amount):
	global payload 
	payload += amount

def getKeyPayload(key):
	print(key)
	local = int(re.search(r'\d+', key).group())
	key = "M["+str(int(local + payload))+"]"
	print(key)
	return key

def store(key, value):
	print("store")
	key = getKeyPayload(key)
	if memory_dictionary[key] == None:
		raise Exception('Location in memory is not defined: {}'.format(key))

	memory_dictionary[key] = value

def load(key):
	print("load")
	key = getKeyPayload(key)
	if memory_dictionary[key] == None:
		raise Exception('Location in memory is not defined: {}'.format(key))
	return memory_dictionary[key]

def loadInstruction(key):
	if memory_dictionary[key] == None:
		raise Exception('Location in memory is not defined: {}'.format(key))
	return memory_dictionary[key]

def getMemory():
	return memory_dictionary;

def isMemory(variable):
	if variable[0] == 'M' and variable[1] == '[' and variable[-1] == ']':
		return True
	else:
		return False


def flush():
	memory = open("../data_handler/memory.txt", "w+")
	for i in range(len(memory_dictionary)):
		memory.write("%s %s\n" % ('M['+str(i)+']', memory_dictionary['M['+str(i)+']']))


initMemory(20)