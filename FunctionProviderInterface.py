import time
import sys
from random import randint

class GlobalExchangeTable:
	def __init__(self):
		self.hashmap = {}
	def add_interface(self, IFEI):   #FunctionExchangeInterface
		if name not in self.hasmap:
			self.hashmap[name] =  IFEI
			return True
		else:
			return False

class FunctionTasker:
	def __init__(self, tasklist, function):
		self.tasklist = tasklist
		self.function = function
	def callable(self, *args, **kwargs):
		while True:
			identifier = id(self.function) + (time.time() % 100000) * 1000000 + len(tasklist) + randint(0, 10000000)
			if identifier not in tasklist:
				break
			else:
				print("[WARN] FunctionTasker found indentifier that is already in tasklist. Too much requests", file=sys.stderr)

		self.tasklist[identifier] = (self.function, args, kwargs)
		return identifier


class FunctionProviderInterface:
	def __init__(self, name, global_exchange_table):
		self.my_exchange_interface = global_exchange_table[name]
		self.name = name

class FunctionUserInterface:
	def __init__(self, UniversalExchangeData):
		self.provideble = UniversalExchangeData[0]
		self.tasklist   = UniversalExchangeData[1]
		self.resultlist = UniversalExchangeData[2]
	def task_function(self, function_name): #TODO: Make Working
		return  self.providing[function_name]()
	def get_function_result(self, callable_id, pause_time=0.1):
		while True:
			if callable_id in self.resultlist:
				return self.resultlist[callable_id]
			timee.sleep(pause_time)

class FunctionExchangeInterface:
	def __init__(self, name):
		self.name = name
		self.providing = {}
		self.tasklist = {}
		self.resultlist = {}
	def add_provideble(self, function_name, function):
		self.providing[function_name] = FunctionTasker(self.tasklist, function).callable





FPI = FunctionProviderInterface
FUI = FunctionUserInterface
FEI = FunctionExchangeInterface
	




if __name__ == "__main__":
	print("Testing mode active")
	print("Testing FunctionTasker")
	
	tasklist = {}
	callables = []
	n = 100
	m = 100
	
	for i in range(n):
		callables.append(FunctionTasker(tasklist, print).callable)
	print("Len of callables is", len(callables))
	print("Testing callables")
	for call in callables:
		for i in range(m):
			call()
	print("Done")
	print("Found", len(tasklist), "elements in tasklist")
	
	if len(tasklist) == n*m:
		print("Passed")
		time.sleep(1)
	else:
		print("Failed")
		time.sleep(1)

