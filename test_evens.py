import unittest
from evens import even_number_of_evens

class TestEvens(unittest.TestCase):
    # pass  # using the pass statement is valid and allows your code to run

    # def test_function_returns_True(self):
    #     """
    #     assertTrue that calling the function even_number_of_evens with an 
    #     empty list returns True
    #     """
    #     self.assertTrue(even_number_of_evens([])) 

    def test_throws_error_if_value_passed_in_is_not_list(self):
        """
        if a TypeError is raised  when the function is called with the value 4.
        """
        self.assertRaises(TypeError, even_number_of_evens, 4)


    def test_values_in_list(self):
        """
        Checks if an empty list has been passed in and should be expecting False.
        passing in the function with an empty list as an argument, and the expected
        return of False
        """
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([22]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == '__main__':
    """
    Checks to see if the the file is being run directly or as an import. 
    If an import, it will not run the instructions contained within.
    """
    unittest.main()

# unittest.main()
