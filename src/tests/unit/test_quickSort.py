import random

from unittest import TestCase
from core.quickSort import quickSort

class TestQuickSort(TestCase):

    def testSortArrayOf0(self):
        """ Sorts an array of 0 elements """
        arr = []
        self.assertEqual(quickSort(arr), [])
    def testSortArrayOf1(self):
        """ Sorts an array of 1 element """
        element = random.randint(0, 9999)
        arr = [element]
        self.assertEqual(quickSort(arr), [element])
    def testSortArrayOf2(self):
        """ Sorts an array of 2 elements """
        arr = [random.randint(0, 999) for i in range(2)]
        sortedArr = quickSort(arr)
        self.assertTrue(sortedArr[1] >= sortedArr[0])
    def testSortArrayOf3(self):
        """ Sorts an array of 3 elements """
        arr = [random.randint(0, 999) for i in range(3)]
        sortedArr = quickSort(arr)
        self.assertTrue(sortedArr[2] >= sortedArr[1])
        self.assertTrue(sortedArr[1] >= sortedArr[0])
    def testSortArrayOf4(self):
        """ Sorts an array of 4 elements """
        arr = [random.randint(0, 999) for i in range(4)]
        sortedArr = quickSort(arr)
        self.assertTrue(sortedArr[3] >= sortedArr[2])
        self.assertTrue(sortedArr[2] >= sortedArr[1])
        self.assertTrue(sortedArr[1] >= sortedArr[0])
    def testSortArrayOf5(self):
        """ Sorts an array of 5 elements """
        arr = [random.randint(0, 999) for i in range(5)]
        sortedArr = quickSort(arr)
        self.assertTrue(sortedArr[4] >= sortedArr[3])
        self.assertTrue(sortedArr[3] >= sortedArr[2])
        self.assertTrue(sortedArr[2] >= sortedArr[1])
        self.assertTrue(sortedArr[1] >= sortedArr[0])

    def testSortBadArray(self):
        """ Throws an exception for arrays that are not fully made by numbers """
        arr = ["apple"]
        with self.assertRaises(TypeError):
            quickSort(arr)
        arr2 = [1, "Saint Seya"]
        with self.assertRaises(TypeError):
            quickSort(arr2)