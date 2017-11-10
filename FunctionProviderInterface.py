import time
import sys
from random import randint
import threading



class TaskListExecutor:
	def __init__(self, tasklist, resultlist, lock, per_run=100):
		self.tasklist = tasklist
		self.resultlist = resultlist
		self.lock = lock
		self.per_run = per_run

	def thread_target(self):
		while True:
			self.lock.acquire()
			left = min(self.per_run, len(self.tasklist))
			for key in self.tasklist:
				if left == 0:
					break
				if key in self.resultlist:
					continue
				left -= 1
				task = self.tasklist[key]
				print("Executed", key)
				self.resultlist[key] = (task[0](*task[1], **task[2]), True)
			self.lock.release()



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



class FunctionUserInterface:
	def __init__(self, ExchangeFingerprint, lock):
		self.provideble = ExchangeFingerprint[0]
		self.tasklist   = ExchangeFingerprint[1]
		self.resultlist = ExchangeFingerprint[2]
		self.lock		= lock

	def task_function(self, function_name): #TODO: Make Working
		return  self.providing[function_name]()

	def get_function_result(self, callable_id, pause_time=0.1):
		while True:
			lock.acquire()
			if callable_id in self.resultlist:
				mem = self.resultlist[callable_id]
				self.tasklist[callable_id] = None
				self.resultlist[callable_id] = None
				lock.release()
				return mem[0]	
			lock.release()		
			time.sleep(pause_time)



class FunctionExchangeInterface:
	def __init__(self, name, global_exchange_table):
		self.name = name
		self.providing = {}
		self.tasklist = {}
		self.resultlist = {}
		self.ExchangeFingerprint = (self.providing, self.tasklist, self.resultlist)
		global_exchange_table[name] = self.ExchangeFingerprint
		self.lock = threading.lock()

	def add_provideble(self, function_name, function):
		self.providing[function_name] = FunctionTasker(self.tasklist, function).callable



FPI = FunctionProviderInterface
FUI = FunctionUserInterface
FEI = FunctionExchangeInterface



if __name__ == "__main__":
	print("Testing mode active")
	print("Testing FunctionTasker")
	
	tasklist = {}
	resultlist = {}
	callables = []
	n = 100
	m = 100
	
	for i in range(n):
		callables.append(FunctionTasker(tasklist, print).callable)

	print("Len of callables is", len(callables))
	print("Testing callables")

	for call in callables:
		for i in range(m):
			call(i)

	print("Done")
	print("Found", len(tasklist), "elements in tasklist")
	
	print("Making tasklist executor")
	lock = threading.Lock()
	executor = TaskListExecutor(tasklist, resultlist, lock)
	executor_thread = threading.Thread(target=executor.thread_target, daemon=True)
	executor_thread.start()
	time.sleep(1)
	
	print("Found", len(tasklist), "elements in tasklist")
	print("Found", len(resultlist), "elements in resultlist")
	
	if len(resultlist) == n*m:
		print("Passed")
		time.sleep(1)
	else:
		print("Failed")
		time.sleep(1)

