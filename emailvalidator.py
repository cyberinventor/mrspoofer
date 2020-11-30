import re

class maileremail:
	def __init__(self):
		self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

	def isvalid(self, email):
		if (re.search(self.regex, email)):
			return True
		else:
			return False


