def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    # return None
    # return True


    if isinstance(numbers, list):
        """
        Checks if the value passed in is a list,
        If the two numbers passed in are even and
        Return True if the number of evens is even, and False if it's not.
        """
        # return True
        if numbers == []:
            return False
        else:
            # return True
            noOfEvens = 0 # initialize a variable 'noOfEvens' to say that we currently have zero evens.
        
        for n in numbers:
            if n % 2 == 0:
                noOfEvens += 1
        
        if noOfEvens:
            return noOfEvens % 2 == 0
        else:
            return False

    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    """
    Checks to see if the the file is being run directly or as an import. 
    If an import, it will not run the instructions contained within.
    """
    print(even_number_of_evens(5))

# print(even_number_of_evens(5))