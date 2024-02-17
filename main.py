"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    
    if x <= 1:
        #Base Case
        return x
    
    else:
        #Recursive Case
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb

def longest_run(mylist, key):
    
    count = 0
    m_count = 0

    for num in mylist:

        if (num == key):
            count += 1
        
        else:
            count = 0
        
        m_count = max(m_count, count)
    
    return m_count



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):

    def recurse(start, end): #Recursive helper function
        if start > end:
            return Result(0, 0, 0, False)
        if start == end: #Base case -> We have reached individual elements
            if mylist[start] == key: #It's the key -> Return 1
                return Result(1, 1, 1, True)
            else: #It's not the key -> return 0
                return Result(0, 0, 0, False)
        
        #We send both halves of the list to our recursive function
        mid = (start + end) // 2
        left_result = recurse(start, mid)
        right_result = recurse(mid + 1, end)
        
        #Left and right sizes to combine longest_run from both sides
        left_size = left_result.left_size if mylist[start] == key else 0
        right_size = right_result.right_size if mylist[end] == key else 0
        
        #Combining our halves
        if left_result.is_entire_range and mylist[mid] == key:
            left_size = left_result.left_size + right_result.left_size
        
        if right_result.is_entire_range and mylist[mid + 1] == key:
            right_size = right_result.right_size + left_result.right_size
        
        longest_size = max(left_result.longest_size, right_result.longest_size, left_result.right_size + right_result.left_size)
        
        is_entire_range = left_result.is_entire_range and right_result.is_entire_range and (mylist[mid] == key or mylist[mid + 1] == key)
        
        return Result(left_size, right_size, longest_size, is_entire_range)
    
    return recurse(0, len(mylist) - 1)

