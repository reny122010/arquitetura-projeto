register_dictionary = {}

def initRegister(amount_temp, amount_register):
	register = open("../data_handler/register.txt", "w+")
	for x in xrange(0, amount_temp):
		register.write("%s %s\n" % ('t'+str(x), '0'))
		register_dictionary['t'+str(x)] = '0'

	for x in xrange(0, amount_register):
		register.write("%s %s\n" % ('r'+str(x), '0'))
		register_dictionary['r'+str(x)] = '0'

	register.write("%s %s\n" % ('zero', '0'))
	register_dictionary['zero'] = '0'

def store(key, value):
	if register_dictionary[key] == None:
		raise Exception('Register is not defined: {}'.format(key))

	if key == 'zero':
		raise Exception('Operation is not avaliable in: {}'.format(key))

	register_dictionary[key] = value

def load(key):
	if register_dictionary[key] == None:
		raise Exception('Register is not defined: {}'.format(key))
	return register_dictionary[key]

def isRegister(variable):
	if variable[0] == 't' or variable[0] == 'r' or variable == 'zero':
		return True
	else:
		return False

def isRegisterZero(variable):
	if variable == 'zero':
		return True
	else:
		return False

def flush():
	register = open("../data_handler/register.txt", "w+")
	for element in register_dictionary:
		register.write("%s %s\n" % (element, register_dictionary[element]))

initRegister(3, 4)