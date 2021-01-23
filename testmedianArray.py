# test cases for medianArray.py
from medianArray import Solution
import unittest

class TestMedian(unittest.TestCase):
	def test_oddArrays(self):
		'''
		Combine two arrays to make an odd numbered array. 
		'''
		list1 = [1,3]
		list2 = [2]
		#print(list1,list2)
		soln = Solution()
		result = soln.findMedianSortedArrays(list1,list2)
		self.assertEqual(result,2.00)

	def test_evenArrays(self):
		list1 = [1,2]
		list2 = [3,4]
		#print()
		soln = Solution()
		result = soln.findMedianSortedArrays(list1,list2)
		self.assertEqual(result,2.5)

if __name__=='__main__':
	unittest.main()