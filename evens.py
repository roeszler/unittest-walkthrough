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


# ------------ Pre Refactor 

    if isinstance(numbers, list):
        """
        Checks if the value passed in is a list,
        If the two numbers passed in are even and
        Return True if the number of evens is even, and False if it's not.
        """
        return True
        if numbers == []: # check for an empty list
            return False
        else:
            # return True
            noOfEvens = 0 # initialize a variable 'noOfEvens' to say that we currently have zero evens

        for n in numbers:
            if n % 2 == 0:
                noOfEvens += 1
        
        if noOfEvens:
            return noOfEvens % 2 == 0
        else:
            return False

    else:
        raise TypeError("A list was not passed into the function")


# ------------ Refactor 1 ------------

    if isinstance(numbers, list):
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


# ------------ Refactor 2 ------------

    if isinstance(numbers, list):
        noOfEvens = 0 # initialize a variable 'noOfEvens' to say that we currently have zero evens.

        # List comprehension: return a value of 1 each time a number (that is
        # evenly divisible by 2) appears in the numbers list, then sum() these values
        # ie how many times an even number appears in the list : 
        print(sum([1 for n in numbers if n % 2 == 0]))

        # for n in numbers:
        #     if n % 2 == 0:
        #         noOfEvens += 1
        
        if noOfEvens:
            return noOfEvens % 2 == 0
        else:
            return False

    else:
        raise TypeError("A list was not passed into the function")



# ------------ Refactor 3 ------------

    if isinstance(numbers, list):
        noOfEvens = sum([1 for n in numbers if n % 2 == 0])
        # print(noOfEvens)
        
        if noOfEvens:
            return noOfEvens % 2 == 0
        else:
            return False

    else:
        raise TypeError("A list was not passed into the function")


# ------------ Refactor 4 ------------

    if isinstance(numbers, list):
        noOfEvens = sum([1 for n in numbers if n % 2 == 0])

        # First we check if noOfEvens is not 0, using the 'truthy' check to do that:
        # truthy value is a value that is considered true when encountered in a Boolean context.
        # Second, noOfEvens % 2 == 0, so lets add that as well
        return True if noOfEvens and noOfEvens % 2 == 0 else False

        # if noOfEvens:
        #     return noOfEvens % 2 == 0
        # else:
        #     return False

    else:
        raise TypeError("A list was not passed into the function")


# ------------ Refactor 5 ------------

    if isinstance(numbers, list):
        noOfEvens = sum([1 for n in numbers if n % 2 == 0])
        return True if noOfEvens and noOfEvens % 2 == 0 else False
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    """
    Checks to see if the the file is being run directly or as an import. 
    If an import, it will not run the instructions contained within.
    """
    # print(even_number_of_evens([2, 1, 4]))
    # even_number_of_evens([2, 1, 4])
    print(even_number_of_evens([2, 1, 4]))
    

# print(even_number_of_evens(5))