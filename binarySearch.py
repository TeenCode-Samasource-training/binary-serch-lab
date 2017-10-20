class BinarySearch(object):
	def __init__(self, list_size, list_step):
		self.list_step = list_step
		self.list_size = list_size

		# Creating our list that we are going to search through
		# Credits to JamesDindi
		# This block check number_list is within our scope
		# i.e, toTwenty is [1, 2, 3 . . . 20]
		if self.list_size in self.toTwenty():
			self.number_list = self.toTwenty()
		elif self.list_size in self.toForty():
			self.number_list = self.toForty()
		elif self.list_size in self.toOneThousand():
			self.number_list = self.toOneThousand()

		# creating a variable to get length of our list
		self.length = len(self.number_list)

	# we need this to pass ListComprehensionTest
	# look at this as a getter method.
	def __getitem__(self, index):
		return self.number_list[index] # equivalent to one_to_twenty[19]

	# methods to return list to search through
	def toTwenty(self):
		return list(range(1,21)) # returns [1, 2, 3 . . . 20]

	def toForty(self):
		return list(range(2,41))[::2] # returns [2, 4, 6 . . . 40]

	def toOneThousand(self):
		return list(range(10,1001))[::10] # returns [10, 20, 30 . . . 1000]

	# where the magic happens
	# binary search by iterative method
	# our test expects search to return a dictionary
	# this a standard method to do a binary search
	def search(self, number):
		firstIndex = 0
		lastIndex = len(self.number_list) - 1
		found = False
		count = 0
		while not found and firstIndex <= lastIndex:
			count += 1
			midpoint = (firstIndex + lastIndex) // 2
			if self.number_list[midpoint] == number:
				found = True
				return { "count": count, 'index': midpoint }
			elif self.number_list[midpoint] < number:
				firstIndex = midpoint + 1
			else:
				lastIndex = midpoint - 1

		# if the number to find is out of scope the index should be -1
		return {"count": 0, "index": -1}