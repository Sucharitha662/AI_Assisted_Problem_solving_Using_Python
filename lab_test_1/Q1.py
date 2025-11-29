#Create a function to reverse a list in Python. Use different types of Implementations

# list_reverse_examples.py

# Implementation 1: Using slicing
def reverse_list_slicing(lst):
    """
    Reverse a list using slicing.
    
    Args:
        lst (list): The list to reverse.
        
    Returns:
        list: Reversed list.
    """
    return lst[::-1]


# Implementation 2: Using built-in reversed()
def reverse_list_reversed(lst):
    """
    Reverse a list using the built-in reversed() function.
    
    Args:
        lst (list): The list to reverse.
        
    Returns:
        list: Reversed list.
    """
    return list(reversed(lst))


# Implementation 3: Using a for-loop
def reverse_list_loop(lst):
    """
    Reverse a list using a for-loop and insert().
    
    Args:
        lst (list): The list to reverse.
        
    Returns:
        list: Reversed list.
    """
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst


# Implementation 4: In-place swap
def reverse_list_inplace(lst):
    """
    Reverse a list in place using two-pointer swap.
    
    Args:
        lst (list): The list to reverse.
        
    Returns:
        list: Reversed list.
    """
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst


# Test all implementations
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    
    print("Original list:", my_list)
    print("Slicing:", reverse_list_slicing(my_list))
    print("Reversed():", reverse_list_reversed(my_list))
    print("For-loop:", reverse_list_loop(my_list))
    print("In-place:", reverse_list_inplace(my_list[:]))  # copy for in-place
