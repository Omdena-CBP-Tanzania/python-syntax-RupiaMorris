def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return  f"My name is {name} and I am {age} years old"
    pass

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"
    pass

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0  # Initialize the total to 0
    for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
        total += i  # Add the current number to the total
    return total  # Return the calculated sum
    pass

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum = sum(numbers) #Calculate sum of the list
    max = max(numbers)#Find maximum value in the list
    min = min(numbers) # Find minimum value in the list
    return (sum, max, min) #Return results as a tuple
    pass

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    above_80 = [name for name, score in students_dict.items() if score > 80]
    return above_80
    pass

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements = set(list1) & set(list2)
    return common_elements
    pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    results = {
        'addition': a+b,
        'subtraction': a-b,
        'multiplication': a*b,
        'dividion': a/b if b != 0 else 'undefined', #This when divion base will be 0
    }
    return results
    pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    reuslts = {
    'and': x and y, #logical AND
    'or' : x or y, #logical OR
    'Not_x' : not x, #Logical not of x
    }
    return results
    pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    results = {
        "and": a & b,         # Bitwise AND
        "or": a | b,          # Bitwise OR
        "xor": a ^ b,         # Bitwise XOR
    }
    return results
    pass