# Shawn Golden


def not_string(str):
    """
    Given a string, return a new string where "not" has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    not_string("cat") returns "notcat"
    not_string("not") returns not
    """
    if str.startswith("not"):
        return str
    else:
        return "not" + str



def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    min_index = lst.index(min(lst))
    lst[0], lst[min_index] = lst[min_index], lst[0]
    return lst



def count_spaces(string):
    """
    Use comprehension to count the number of spaces in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_spaces("the cow jumped over the moon") returns 5
    """
    return sum(1 for char in string if char == ' ')

def sum67(nums):
    '''
    Return the sum of the numbers in the array, except ignore sections 
    of numbers starting with a 6 and extending to the next 7 
    (every 6 will be followed by at least one 7). 
    Return 0 for no numbers.
    sum67([1, 2, 2]) → 5
    sum67([1, 2, 2, 6, 99, 99, 7]) → 5
    sum67([1, 1, 6, 7, 2]) → 4
    '''
    
    total = 0
    ignore_section = False
    
    for num in nums:
        if num == 6:
            ignore_section = True
        elif ignore_section and num == 7:
            ignore_section = False
        elif not ignore_section:
            total += num
    
    return total
  
def build_heights_dict():
    '''
    Create a dictionary where the key is a person's name and the value is
    their height stored as an integer. 
    Read in the file, heights.txt, store the person's first name and 
    last name as the key (first and last name should have a space between them)
    and their height as the integer value.
    Your output should read:
     {'Thomas Jones': '70', 'Marcus Hansen': '68', 'Sarah Jenkins': '63', 
     'Abigail Ross': '65', 'Sebastian Adams': '70', 'Ella Rivera': '59', 
     'Luis Cruz': '71', 'Matt Patterson': '74', 'Jayden Cox': '67', 
     'Javier Alvaro': '69', 'Victoria Thompson': '62', 
     'Daniel Richardson': '68', 'Zoey Miller': '66'}
    '''
    height_dict = {}
    
    with open('heights.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 3:
                name = parts[0] + ' ' + parts[1]
                height = parts[2]
                height_dict[name] = height
    
    return height_dict


print('not_string("cat") expected: notcat')
print('not_string("cat") actual:', not_string("cat"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print('count_spaces("the cow jumped over the moon") expected: 5')
print('count_spaces("the cow jumped over the moon") actual:', count_spaces("the cow jumped over the moon"))

print('sum67([1, 2, 2, 6, 99, 99, 7]) expected: 5')
print('sum67([1,2,2]) actual:', sum67([1, 2, 2, 6, 99, 99, 7]))

print(build_heights_dict())