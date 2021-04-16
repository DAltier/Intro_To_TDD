import unittest

def reverseList(list) :
    for i in range(int(len(list) / 2)) :
        list[i], list[len(list)- i - 1] = list[len(list)- i - 1], list[i]
    return list
class reverseListTests(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def testTwo(self) :
        self.assertEqual(reverseList([8,4,6,4,3,7]), [7,3,4,6,4,8])
    def testThree(self):
        self.assertEqual(reverseList([5,3,7,1]), [1,7,3,5])
    def testFour(self):
        self.assertEqual(reverseList(["one","two","three","four"]), ["four","three","two","one"])
    def setUp(self):
        pass
        #print("running setUp")
    def tearDown(self):
        pass
        #print("running tearDown tasks")

def isPalindrome(word) :
    for i in range(int(len(word) / 2)) :
        if (word[i] != word[len(word)- i - 1]) :
            return False
    return True
class isPalindromeTests(unittest.TestCase) :
    def testOne(self) :
        self.assertTrue(isPalindrome("racecar"))
    def testTwo(self) :
        self.assertFalse(isPalindrome("rabcr"))
    def testThree(self):
        self.assertTrue(isPalindrome("kayak"))
    def testFour(self):
        self.assertTrue(isPalindrome("saippuakivikauppias"))
    def testFive(self) :
        self.assertFalse(isPalindrome("taco"))
    def testSix(self) :
        self.assertFalse(isPalindrome("window"))
    def testSeven(self) :
        self.assertFalse(isPalindrome("123214"))
    def setUp(self):
        pass
        #print("running setUp")
    def tearDown(self):
        pass
        #print("running tearDown tasks")

def coin(cents) :
    coins = [25,10,5,1]
    answer = []
    for coin in coins :
        count = 0
        while (cents >= coin) :
            cents -= coin
            count += 1
        answer.append(count)
    return answer
class coinTests(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(coin(87), [3,1,0,2])
    def testTwo(self) :
        self.assertEqual(coin(25), [1,0,0,0])
    def testThree(self):
        self.assertEqual(coin(50), [2,0,0,0])
    def testFour(self):
        self.assertEqual(coin(31), [1,0,1,1])
    def testFive(self):
        self.assertEqual(coin(7), [0,0,1,2])
    def testSix(self):
        self.assertEqual(coin(125), [5,0,0,0])
    def testSeven(self):
        self.assertEqual(coin(41), [1,1,1,1])
    def setUp(self):
        pass
        #print("running setUp")
    def tearDown(self):
        pass
        #print("running tearDown tasks")

def factorial(num) :
    if (num == 1) :
        return num
    else:
        return num*factorial(num-1)
class factorialTests(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(factorial(2), 2)
    def testTwo(self) :
        self.assertEqual(factorial(3), 6)
    def testThree(self):
        self.assertEqual(factorial(4), 24)
    def testFour(self):
        self.assertEqual(factorial(5), 120)
    def testFive(self) :
        self.assertEqual(factorial(6), 720)
    def setUp(self):
        pass
        #print("running setUp")
    def tearDown(self):
        pass
        #print("running tearDown tasks")

def fibonacci(n):
    if (n <= 1) :
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
class fibonacciTests(unittest.TestCase) :
    def testOne(self) :
        self.assertEqual(fibonacci(2), 1)
    def testTwo(self) :
        self.assertEqual(fibonacci(3), 2)
    def testThree(self):
        self.assertEqual(fibonacci(4), 3)
    def testFour(self):
        self.assertEqual(fibonacci(5), 5)
    def testFive(self) :
        self.assertEqual(fibonacci(6), 8)
    def setUp(self):
        pass
        #print("running setUp")
    def tearDown(self):
        pass
        #print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()

