class Account(object):
	"""docstring for Account"""
	def __init__(self, rate):
		self._amt = 0
		self.rate = rate

	@property
	def amount(self):
	    return self._amt
	
	@property
	def cny(self):
	    return self._amt * self.rate

	def amount(self, value):
		if value < 0:
			print("Sorry, no negative amount in the account")
			return
		self._amt = value

if __name__ == '__main__':
	acc = Account(rate = 6.6)
	acc.amount = 20
	print('Dollar amount:', acc.amount)
	print("In CNY:", acc.cny)

	acc.amount = -100
	print('Dollar amount:', acc.amount)