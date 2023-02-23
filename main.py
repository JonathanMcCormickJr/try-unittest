import unittest

def divide_by_7(a):
    return a / 7

class TestDivideBy7(unittest.TestCase):
    # Arrange
    def setUp(self):
        print("SETUP has been CALLED...")
        self.a = 259

    def tearDown(self):
        print("TEARDOWN has been CALLED...")
        self.a = 0
        
    
    def test_function_0(self):
        print("test_function_0(self) has been CALLED")
        # Act
        result = divide_by_7(self.a)
        # Assert
        self.assertEqual(result, self.a/7)

    def test_function_1(self):
        pass
        
class MySecondPythonTest(unittest.TestCase):
    def test_function_0(self):
        pass

    def test_function_1(self):
        pass
        
if __name__ == "__main__":
    unittest.main()