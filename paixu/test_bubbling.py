# -*-coding:UTF-8-*-

#有点问题，还未实现

import unittest
from bubbling import *

class TestBubbling(unittest.TestCase):
	
	def test_arr(self):
		
		self.assertEqual([1, 2, 3, 4, 5], arr[5, 4, 3, 2, 1])
		#self.assertNotEqual(3, add(2, 2))
		
if __name__=='__main__':
	unittest.main()