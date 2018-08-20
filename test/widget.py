class Widget:
	def __init__(self, size = (40, 40)):
		self.size = size
	def getSize(self):
		return self.size
	def resize(self, width, heigth):
		if width < 0 or heigth < 0:
			raise ValueError, "illegal size"
		self._sieze = (width, height)
	def dispose(self):
		pass
		