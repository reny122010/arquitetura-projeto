cache_dictionary = {}
cache_ticket = {}

amount_total_cache = 0
cache_pointer = 0
cache_miss = 0
cache_hit = 0

def getKey():
	global cache_pointer
	key = "C["+str(int(cache_pointer))+"]"
	
	cache_pointer += 1
	if amount_total_cache == cache_pointer:
		cache_pointer = 0

	return key

def initCache(amount_cache):
	amount_total_cache = amount_cache
	cache = open("../data_handler/cache.txt", "w+")
	for x in xrange(0, amount_cache):
		cache.write("%s %s %s\n" % ('C['+str(x)+']', 0, 'NULL'))
		cache_dictionary['C['+str(x)+']'] = '0'

def store(ticket , value):
	key = getKey()
	if cache_dictionary[key] == None:
		raise Exception('Location in cache is not defined: {}'.format(key))

	cache_dictionary[key] = value
	cache_ticket[ticket] = key

def load(ticket):
	try:
		key = cache_ticket[ticket]
	except Exception as e:
		global cache_miss
		cache_miss = cache_miss + 1
		return None
	
	global cache_hit
	cache_hit = cache_hit + 1
	return cache_dictionary[key]

def update(ticket, value):
	try:
		cache_dictionary[cache_ticket[ticket]] = value
		return True
	except Exception as e:
		return False

def flush():
	cache = open("../data_handler/cache.txt", "w+")
	ticket = None
	for i in range(len(cache_dictionary)):
		for j in cache_ticket:
			if cache_ticket[j] == 'C['+str(i)+']':
				ticket = j
			
		cache.write("%s %s %s\n" % ('C['+str(i)+']', ticket, cache_dictionary['C['+str(i)+']']))
		ticket = None

initCache(10)