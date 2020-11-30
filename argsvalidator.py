class arguments:
	def __init__(self, arguments):
		self.args = arguments
		self.argslist = []
		self.counter = []

	def isvalid(self):
		args = self.args
		argslist = self.argslist
		counter = self.counter
		for arg in vars(args):
				if getattr(args, arg) is None:
					counter.append(False)
					argslist.append(False)
				else:
					counter.append(True)
					argslist.append(True)

		if counter.count(True) > counter.count(False):
			return True
		elif counter.count(True) < len(argslist):
			return False
		else:
			return False
